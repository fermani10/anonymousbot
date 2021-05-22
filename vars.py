import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class var:
    BOT_TOKEN = os.getenv("1819801273:AAE3gMgS8EG8kuT0ERL_IJDS3g4erRsM0is")  # from @botfather
    API_ID = int(os.getenv("2327121"))  # from https://my.telegram.org/apps
    API_HASH = os.getenv("e2c38ca4942c1b54735ce0c980841c5e")  # from https://my.telegram.org/apps
    START_MESSAGE = os.getenv("START_MESSAGE", None)  # Not Mandatory
