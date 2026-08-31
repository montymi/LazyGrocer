"""Exception handlers for the Flask application."""
import logging
from flask import jsonify
from sqlalchemy.exc import IntegrityError, DataError, OperationalError
from psycopg2 import errors as pg_errors
from src.middleware.errors import (
    BaseAPIError,
    ValidationError,
    DatabaseError,
    ConflictError
)

logger = logging.getLogger(__name__)


def handle_api_error(error):
    """Handle custom API errors."""
    logger.error(f"API Error: {error.message}", exc_info=True)
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


def handle_integrity_error(error):
    """Handle database integrity errors."""
    logger.error(f"Database Integrity Error: {str(error)}", exc_info=True)

    # Check for specific PostgreSQL error codes
    if hasattr(error.orig, 'pgcode'):
        if error.orig.pgcode == '23505':  # Unique violation
            return jsonify({
                'error': {
                    'message': 'A record with this value already exists',
                    'status_code': 409
                }
            }), 409
        elif error.orig.pgcode == '23503':  # Foreign key violation
            return jsonify({
                'error': {
                    'message': 'Referenced record does not exist',
                    'status_code': 400
                }
            }), 400

    return jsonify({
        'error': {
            'message': 'Database constraint violation',
            'status_code': 400
        }
    }), 400


def handle_data_error(error):
    """Handle database data errors."""
    logger.error(f"Database Data Error: {str(error)}", exc_info=True)
    return jsonify({
        'error': {
            'message': 'Invalid data format',
            'status_code': 400
        }
    }), 400


def handle_operational_error(error):
    """Handle database operational errors."""
    logger.error(f"Database Operational Error: {str(error)}", exc_info=True)
    return jsonify({
        'error': {
            'message': 'Database connection error',
            'status_code': 503
        }
    }), 503


def handle_value_error(error):
    """Handle value errors."""
    logger.error(f"Value Error: {str(error)}", exc_info=True)
    return jsonify({
        'error': {
            'message': str(error),
            'status_code': 400
        }
    }), 400


def handle_404(error):
    """Handle 404 errors."""
    return jsonify({
        'error': {
            'message': 'Endpoint not found',
            'status_code': 404
        }
    }), 404


def handle_500(error):
    """Handle 500 errors."""
    logger.error(f"Internal Server Error: {str(error)}", exc_info=True)
    return jsonify({
        'error': {
            'message': 'Internal server error',
            'status_code': 500
        }
    }), 500


def register_error_handlers(app):
    """Register all error handlers with the Flask app."""
    app.register_error_handler(BaseAPIError, handle_api_error)
    app.register_error_handler(IntegrityError, handle_integrity_error)
    app.register_error_handler(DataError, handle_data_error)
    app.register_error_handler(OperationalError, handle_operational_error)
    app.register_error_handler(ValueError, handle_value_error)
    app.register_error_handler(404, handle_404)
    app.register_error_handler(500, handle_500)