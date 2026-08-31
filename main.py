"""Main application entry point."""

from src.app import create_app


def main():
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
