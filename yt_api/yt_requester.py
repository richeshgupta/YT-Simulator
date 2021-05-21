from googleapiclient.discovery import build #Google package method for building api objects
from googleapiclient.errors import HttpError

import json

# Global Variables 
DEVELOPER_KEY = "AIzaSyDhGRDCLOwXndCOZhJLq6XFXTi5JOUqlxU"
SERVICE_VERSION = 'v3'
SERVICE_NAME="youtube"
QUERY = "Cute Dog Videos"
# End of var

def youtube_search(query=QUERY):
    yt_obj = build(SERVICE_NAME,SERVICE_VERSION,developerKey=DEVELOPER_KEY) #Creating yt obj to perform operations
    search_req = yt_obj.search().list(
        part="snippet",
        q=QUERY,
        maxResults=15,
        order="date"
        )
    search_res = search_req.execute()
    print("search_type : ",type(search_res))
    return search_res






