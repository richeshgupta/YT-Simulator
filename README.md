#YTSimulator
A webApp which fetches Youtube videos on certain topic and saves it in database, where you can search it too.
## How to build Project
    I. Clone the Project
    II. Install Python 3
    III. Run
            pip3 install -r requirements.txt
    IV. go to YT_simulator directory
    V. Run
            python3 manage.py runserver
            or
            python manage.py runserver
     UI - http://127.0.0.1:8000

## API endpoints - 
     GET /api/getVideoData/
                It returns all the video stored in the data base.
    GET /api/getSearch/?query=dog
                It searches the DB for the query in title or description

## Deployed in
    http://ytsim.pythonanywhere.com/
            
    
        

     

