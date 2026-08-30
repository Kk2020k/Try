import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '26872474'))
    API_HASH = str(getenv('API_HASH', 'f8d3a289bf28a13a7159ad0b2ed114e7'))
    BOT_TOKEN = str(getenv('BOT_TOKEN','6837885920:AAHYl2LNCS-pEqt9KL3ks4D2bFP8SWGlYbs'))
    name = str(getenv('name', 'filetolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002397408958'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "5211097531").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'RBEagle2k'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME','smdfile-to-link-f79fe378bc37'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv("FQDN", "file2link-assrsma56.koyeb.app"))
HAS_SSL = str(getenv("HAS_SSL", "True")).lower() == "true"

if HAS_SSL:
    URL = f"https://{FQDN}/"
else:
    URL = f"http://{FQDN}/"
DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://Test:test@cluster0.l3ul5li.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'Uptate2k'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split())) 
