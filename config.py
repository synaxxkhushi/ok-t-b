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
COOKIES     = "PANWEB=1; csrfToken=SlG3EHVGdauCDO4Rl8YJkRF4; browserid=me9b3gO3KyIcbje9j0HeWmSC-u_Vty-TzJBElBySlbVLAuJko3Kz_wQKPzw=; lang=en; bid_n=18f753c1c3635204fd4207; ab_sr=1.0.1_Y2IwMDcxNDc1Yjc5NmM2NzRjMDA1NjRhN2YzYjk3MjQwZDAxMjMzZmRjNjViMzdmY2IxN2VmNGU2MWE1MjE3MDA5MTRhMjc4ZjM1NDI1NWQ1MmRkZGY0Y2JmOTkwZDFmMmI3NGUzZjFlNTUyZTdiYzRiNWZhZDA2MDI0MGNlYmYxYmNkZjExNzFmOWZhYmRlZjY5MmZkNWIzODQyMDQ0OQ==; ndus=Yfoxfv7teHuiIHLB5W1wSoAP8G7_l8pAhmWIAYFu; ndut_fmt=F973758CA4D9E5B17CDC91EEF01BFAE050E4FF332F993ECC9E849F9304680D55" # get from chrome dev tools 

# REDIS DATABASE [https://redis.com/try-free]
HOST        = "redis-10693.c278.us-east-1-4.ec2.redns.redis-cloud.com"
PORT        = 10693
PASSWORD    = "aLYDdunvCU0I0wY3Jrq6s3ehqabHl3Qf"


# ---------- DON'T TOUCH THIS ---------- #
for admin in getenv("ADMINS", "1034599258 6231550362").split():
    ADMINS.append(int(admin))
