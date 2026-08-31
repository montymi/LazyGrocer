"""Request handler middleware and decorators."""
import functools
import logging
from flask import current_app, g, request, jsonify
from sqlalchemy.orm import Session
from src.middleware.errors import DatabaseError, ValidationError

logger = logging.getLogger(__name__)


def get_db_session():
    """Get database session for the current request."""
    if 'db_session' not in g:
        g.db_session = current_app.Session()
    return g.db_session


def close_db_session(error=None):
    """Close database session at the end of request."""
    db_session = g.pop('db_session', None)
    if db_session is not None:
        if error is None:
            db_session.commit()
        else:
            db_session.rollback()
        db_session.close()


def error_handler(func):
    """Decorator to handle errors in route functions."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {str(e)}", exc_info=True)
            close_db_session(error=e)
            raise

    return wrapper


def validate_request(*required_fields):
    """Decorator to validate required fields in request."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            data = request.get_json()
            if not data:
                raise ValidationError("No JSON data provided")

            missing_fields = []
            for field in required_fields:
                if field not in data or data[field] is None:
                    missing_fields.append(field)

            if missing_fields:
                raise ValidationError(
                    f"Missing required fields: {', '.join(missing_fields)}"
                )

            return func(*args, **kwargs)

        return wrapper

    return decorator


def paginate(default_page=1, default_per_page=20, max_per_page=100):
    """Decorator to add pagination to route functions."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            page = request.args.get('page', default_page, type=int)
            per_page = request.args.get('per_page', default_per_page, type=int)

            if page < 1:
                raise ValidationError("Page must be greater than 0")
            if per_page < 1:
                raise ValidationError("Per page must be greater than 0")
            if per_page > max_per_page:
                raise ValidationError(f"Per page cannot exceed {max_per_page}")

            kwargs['page'] = page
            kwargs['per_page'] = per_page
            return func(*args, **kwargs)

        return wrapper

    return decorator


def transaction(func):
    """Decorator to wrap function in database transaction."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        session = get_db_session()
        try:
            result = func(*args, **kwargs)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            logger.error(f"Transaction failed in {func.__name__}: {str(e)}")
            raise DatabaseError(f"Transaction failed: {str(e)}")
        finally:
            session.close()

    return wrapper