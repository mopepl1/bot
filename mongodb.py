import traceback
import pymongo

client = pymongo.MongoClient(
        "mongodb+srv://noodfi:A5QGyd921roJGMaJ@cluster0.tkgs4h4.mongodb.net/myDatabase?retryWrites=true&w=majority&appName=Cluster0"

)
result = str(client)

if "connect=True" in result:
    try:
        print("MONGODB CONNECTED SUCCESSFULLY ✅")
    except:
        pass
else:
    try:
        print("MONGODB CONNECTION FAILED ❌")
    except:
        pass

folder = client["XCC_DATABASE"]
usersdb = folder.USERSDB
chats_auth = folder.CHATS_AUTH
super_chat = folder.SUPER_CHAT
gcdb = folder.GCDB
sksdb = client["SKS_DATABASE"].SKS
confdb = client["SKS_DATABASE"].CONF_DATABASE