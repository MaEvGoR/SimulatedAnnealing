from src.dash.asgi import get_app


def main():
    app = get_app()
    app.run_server(debug=True)

if __name__ == '__main__':
    main()