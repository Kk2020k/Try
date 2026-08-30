import os
from os import getenv, environ

from dotenv import load_dotenv

load_dotenv()


class Var:
    MULTI_CLIENT = False

    API_ID = int(getenv("API_ID", "0"))
    API_HASH = getenv("API_HASH", "")
    BOT_TOKEN = getenv("BOT_TOKEN", "")

    name = getenv("name", "filetolinkbot")

    SLEEP_THRESHOLD = int(
        getenv("SLEEP_THRESHOLD", "60")
    )

    WORKERS = int(
        getenv("WORKERS", "4")
    )

    BIN_CHANNEL = int(
        getenv("BIN_CHANNEL", "0")
    )

    PORT = int(
        getenv("PORT", "8080")
    )

    BIND_ADRESS = getenv(
        "WEB_SERVER_BIND_ADDRESS",
        "0.0.0.0",
    )

    PING_INTERVAL = int(
        getenv("PING_INTERVAL", "1200")
    )

    OWNER_ID = {
        int(x)
        for x in getenv("OWNER_ID", "").split()
        if x.strip()
    }

    NO_PORT = (
        getenv("NO_PORT", "False").lower()
        == "true"
    )

    OWNER_USERNAME = getenv(
        "OWNER_USERNAME",
        "RBEagle2k",
    )

    APP_NAME = getenv("APP_NAME", "")

    ON_HEROKU = "DYNO" in environ

    # Koyeb domain
    FQDN = getenv(
        "FQDN",
        "file2link-assrsma56.koyeb.app",
    )

    HAS_SSL = (
        getenv("HAS_SSL", "True").lower()
        == "true"
    )

    if HAS_SSL:
        URL = f"https://{FQDN}/"
    else:
        URL = f"http://{FQDN}/"

    DATABASE_URL = getenv(
        "DATABASE_URL",
        "",
    )

    UPDATES_CHANNEL = getenv(
        "UPDATES_CHANNEL",
        "None",
    )

    BANNED_CHANNELS = [
        int(x)
        for x in getenv(
            "BANNED_CHANNELS",
            "",
        ).split()
        if x.strip()
    ]
