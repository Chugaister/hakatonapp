from uvicorn import run

from app.app import app


def main():
    run(app, host="127.0.0.1", port=80)


if __name__ == "__main__":
    main()
