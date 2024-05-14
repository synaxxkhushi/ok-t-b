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
COOKIES     = "PANWEB=1; csrfToken=mNxTLcj23_Q55MO4yN-ROk5h; browserid=VHTZhOscJptCPoAVrDLdoD1gE4lErsXeDB_Elcc-lc9HczX1PYC3w_9zDIQ=; lang=en; bid_n=18f753c1c3635204fd4207; ab_sr=1.0.1_YWZkMWUzOTMxYWVjOWI3MDVkMWI4MzUxYjJhNTlmMGY0ZTZhMDU2ZjZmZGYwNDg4YmJmODE1NzE0NDk4NWYxNTliMmI1ZmRmODU0MGRjNDNjNGZkYzcyZjliNTViNzhjZDk2MWQ4M2M1OTFhODZlNjc5OTFmZTEzMzg2M2U3ODAxMmE1YjE1YWE4OGRhNWQzMjExYjJmYWJjNzZjNjE0ZA==; ndus=YvimKCyteHui_C4IO_iGlRG7xoIrwwki-_NiA5Am; ndut_fmt=9CF479BD2004D860F35758BC00B3CF9883784F352A58D8F79656C21D54DE972C" # get from chrome dev tools 

# REDIS DATABASE [https://redis.com/try-free]
HOST        = "redis-10693.c278.us-east-1-4.ec2.redns.redis-cloud.com"
PORT        = 10693
PASSWORD    = "aLYDdunvCU0I0wY3Jrq6s3ehqabHl3Qf"


# ---------- DON'T TOUCH THIS ---------- #
for admin in getenv("ADMINS", "1034599258 6231550362").split():
    ADMINS.append(int(admin))
