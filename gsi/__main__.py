from . import GSIConnection
from signal import pause


if __name__ == "__main__":
    server = GSIConnection()

    @server.on_data
    def handle_post(data):
        print(data)

    print("hello world")
    server.start()
    