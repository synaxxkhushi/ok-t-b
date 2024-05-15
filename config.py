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
COOKIES     = "PANWEB=1; csrfToken=Aib-iThW-6-vc1tk3h76BHvZ; browserid=VHTZhOscJptCPoAVrDLdoD1gE4lErsXeDB_Elcc-lc9HczX1PYC3w_9zDIQ=; lang=en; bid_n=18f753c1c3635204fd4207; ab_sr=1.0.1_MDljNmU5NWRlMTlkN2RlOWMzNzVhNzI1MmZlMWE5NTQzODQzM2IwZDNjZGI0ODVlM2FmMDhmMWMxMDVjMDc0NDI0YzMyMjFjZTIyYTJhNjczN2NhZGMzYWQxYzQwZGQ1YWRiOWI3ZjU4NWQ3MDZiY2NjMDM5NGRlZWU5YjNhYzRkMmVjYmFkZGE0ZTA5YjRmNmRlMDg3Y2IwYzA3NmVhZg==; ndus=Yz_k7K3teHuiq2aTON0jEAxh4uwhaNMK0pAXVnb-; ndut_fmt=67039EAB0C881A957473530301AC907BE9BC8FD2BB007C2D112CF229CBE20EFA" # get from chrome dev tools 

# REDIS DATABASE [https://redis.com/try-free]
HOST        = "redis-10693.c278.us-east-1-4.ec2.redns.redis-cloud.com"
PORT        = 10693
PASSWORD    = "aLYDdunvCU0I0wY3Jrq6s3ehqabHl3Qf"


# ---------- DON'T TOUCH THIS ---------- #
for admin in getenv("ADMINS", "1034599258 6231550362").split():
    ADMINS.append(int(admin))
