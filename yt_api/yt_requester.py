from googleapiclient.discovery import build #Google package method for building api objects
from googleapiclient.errors import HttpError

import json

# Global Variables 
# DEVELOPER_KEY = "AIzaSyDhGRDCLOwXndCOZhJLq6XFXTi5JOUqlxU"
# DEVELOPER_KEY ="AIzaSyCq5-gn3kx69Fxy_3Ee9IywglfD4fgMg14"
# DEVELOPER_KEY="AIzaSyB-Gq2kFnNTbODAHqOLNwdLvc5fYWWD9sQ"
DEVELOPER_KEY = "AIzaSyDBKwqAXrxvpwvoKzB5M7pU38kYl90ec5g"
SERVICE_VERSION = 'v3'
SERVICE_NAME="youtube"
QUERY = "Games or food or fashion or Tutorial"
# End of var

def youtube_search(query=QUERY):
    yt_obj = build(SERVICE_NAME,SERVICE_VERSION,developerKey=DEVELOPER_KEY) #Creating yt obj to perform operations
    search_req = yt_obj.search().list(
        part="snippet",
        q=QUERY,
        maxResults=6,
        order="date",
        type="video",
        )
    search_res = search_req.execute()
    # print("search_type : ",type(search_res))
    return search_res






