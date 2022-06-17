## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BACAgwny9rzqH-w360H37CA5qTJ4LThQAS6RfHIr03B6579_uf8WJ8cbbymYHe7NgsIn90d9OzOrDnVyhC2YMNnlqmHDYksr08T0b7r9WLPlCpWLX8WpNhgi3-xtrs25naJd2C4QtAEQzULNfEjv8lM0wEDbiCZ_LpV__w1FAJbYeNs_TCg1nCMF19HTqQ8bvI03ePERvrA3_KeGaDUvK15-pPVO11Xo0Y-Vz3qR0KYqgbziNAXn9jwGv2N5EQUMFD-_ZfQmCIEp9MFXrB2kmfNBcIiq0ZwTsQREslQzpsDJ5Tb4sTPVNUhojLwdT2ZhnMnlBUpjY28HD2lEjKuCmyeiAAAAATNWuRMA")
BOT_TOKEN = getenv("BOT_TOKEN", "5478359768:AAGqW2wRaj4JrDNOpuelgQsZjC7ZYrCDGiI")
BOT_NAME = getenv("BOT_NAME", "music")
API_ID = int(getenv("API_ID", "9839694"))
API_HASH = getenv("API_HASH", "483b64b20a54ba55ec40ede3b44f70d6")
OWNER_NAME = getenv("OWNER_NAME", "Ahmed")
OWNER_USERNAME = getenv("OWNER_USERNAME", "A_h_m_e_dE")
ALIVE_NAME = getenv("ALIVE_NAME", "Ahmed")
BOT_USERNAME = getenv("BOT_USERNAME", "mero_musicbot")
OWNER_ID = getenv("OWNER_ID", "5300856245")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Ahmednnt")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "G6_9R")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "G6_9R")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
