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
COOKIES     = "PANWEB=1; csrfToken=MkqT6gDAocZzpanwxC_qcIQw; browserid=fUSzfZnsfR1v8T0y_C10IUL-DWeJOtfbk54grUAVM47hH5lKtVPR94kTgl0=; lang=en; bid_n=18f391807aeb6405dd4207; stripe_mid=e48c3be4-aa47-471b-8947-da14cd3da49696ddd0; __stripe_sid=26866037-610b-4451-892b-1b83e5e2883739099e; ndus=Y4ZW53CteHuiZEVNT9iX5E4DAdRsCk4v4Inzu5-3; ndut_fmt=B017DAC69BBE8BF18A90900727665A6D45F0C4233898CD62183F562720F53CF3" # get from chrome dev tools ex: "PANWEB=1; csrfToken=; lang=en; TSID=; __bid_n=; _ga=; __stripe_mid=; ndus=; browserid==; ndut_fmt=; _ga_06ZNKL8C2E=" (don't use this)

# REDIS DATABASE [https://redis.com/try-free]
HOST        = "redis-10693.c278.us-east-1-4.ec2.redns.redis-cloud.com"
PORT        = 10693
PASSWORD    = "aLYDdunvCU0I0wY3Jrq6s3ehqabHl3Qf"


# ---------- DON'T TOUCH THIS ---------- #
for admin in getenv("ADMINS", "1034599258 6231550362").split():
    ADMINS.append(int(admin))
