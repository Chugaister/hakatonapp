from uvicorn import run

from app.app import app


def main():
    run(app, host="192.168.1.105", port=80)


if __name__ == "__main__":
    main()
