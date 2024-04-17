from os import getenv

API_ID      = int(getenv("API_ID", "28542813"))
API_HASH    = getenv("API_HASH", "02ce7c339f7776844ff4ab03da338ccd")
BOT_TOKEN   = getenv("BOT_TOKEN", "6390531573:AAFGIa3id_mQ9-u6E2WvGTrj9qipwcd_H3g")
LOG_CHANNEL = int(getenv("API_ID", "-1002002020654")) # chat where you want to store videos
ADMINS      = []

# FSUB VARIABLE
CHAT1       = "@synaxnetwork" # only username supported
CHAT2       = "@synaxbots" # only username supported

## TERABOX COOKIES
COOKIES     = "PANWEB=1; csrfToken=jtTLiTvGBxl_IFTle3hwgd06; browserid=oCpAO0XIcEXS61MAHq_S0gea3v-MrA7ZbuYgHcSypkPMjODJI2Yfnbm91DI=; lang=en; TSID=yEwVKMH3QRfeVasoZ2rLwqUDae3tGNdU; __bid_n=18dcc331eb3d5363504207; _ga=GA1.1.2132560438.1708527920; __stripe_mid=bce13f2e-8150-4080-b99f-c602ab9289d26acc64; ndus=Y-R0se7teHui-W2HBiWYGD11Y6j6V_cUIkDTmbRI; _ga_06ZNKL8C2E=GS1.1.1709701123.4.0.1709702212.52.0.0; ndut_fmt=A533422E05B3AA6868B57C3F11A827DD07A068D233C9AC3D2D6907B2472401D4" # get from chrome dev tools ex: "PANWEB=1; csrfToken=; lang=en; TSID=; __bid_n=; _ga=; __stripe_mid=; ndus=; browserid==; ndut_fmt=; _ga_06ZNKL8C2E=" (don't use this)

# REDIS DATABASE [https://redis.com/try-free]
HOST        = "redis-16969.c274.us-east-1-3.ec2.cloud.redislabs.com"
PORT        = 16969
PASSWORD    = "4c2EP43VcEWklp9DpI6Zv5kfPJfecH4w"


# ---------- DON'T TOUCH THIS ---------- #
for admin in getenv("ADMINS", "1034599258 6231550362").split():
    ADMINS.append(int(admin))
