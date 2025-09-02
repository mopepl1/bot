# from pymongo import MongoClient

# # MongoDB connection string
# mongo_url = "mongodb+srv://root:HQxAuNYG23zGJvEL@grandpaa.nuj12ox.mongodb.net/?retryWrites=true&w=majority"
# client = MongoClient(mongo_url)

# # Define your database and collection
# folder = client["XCC_DATABASE"]
# usersdb = folder.USERSDB

# # Reset details for all users
# result = usersdb.update_many(
#     {},  # Empty filter matches all documents
#     {
#         "$set": {"status": "FREE", "plan": "N/A","expiry": "N/A"},  # Update fields
#     }
# )

# print(f"{result.modified_count} user(s) were updated successfully.")
