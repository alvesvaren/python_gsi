from . import GSIConnection
from signal import pause


if __name__ == "__main__":
    server = GSIConnection()

    @server.on_post
    def handle_post(data):
        print(data)


    server.start()
    print("hello world")
    server.block()