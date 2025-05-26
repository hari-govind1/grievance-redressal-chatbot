import chromadb

try:
    client = chromadb.PersistentClient(path="D:/New folder1") #path="D:/New folder1"
    collections = client.list_collections()
    print("Collections in the database:", collections)
except Exception as e:
    print("Error connecting to the database:",e)