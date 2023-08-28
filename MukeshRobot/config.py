
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "13958802" # integer value, dont use ""
    API_HASH = "f6d2d3b04309e9660a0be5b2a6195a7c"
    TOKEN = "BQCeCBOWwUkPmeulBIU7PDp7fsrkxduI8L31RzBCNqo3VcetWe07nEkM"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 5838967403 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    
    SUPPORT_CHAT = "dong_di"  # Your own group for support, do not add the @
    START_IMG = ""
    EVENT_LOGS = (-1001816641523)  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://minhquang24071996:2407@music.jz0q4j9.mongodb.net/?retryWrites=true&w=majority"
    # RECOMMENDED
    DATABASE_URL = "postgres://fbaxoftf:SjvlF8ZKeFbSWmWaqqqe9ornkjR12-lB@rain.db.elephantsql.com/fbaxoftf"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "8V0ZC4HG72JTQSOE"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "ZXG90QJ2I7Z5"
    # Get your API key from https://timezonedb.com/api

    # Optional fields
    CHATBOT_API="" # get it from @FallenChat_Bot using /token
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
