# Read bot token from file

def read_bot_token_from_file(filename: str) -> str:
    with open(filename, "r") as file:
        bot_token = file.read()
        return bot_token

