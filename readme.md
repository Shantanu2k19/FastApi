#basic setup 

python3.8 -m venv latest
pip install fastapi uvicorn
#Uvicorn is a lightning-fast ASGI server for Python web frameworks

#runserver
uvicorn myapi:app --reload #--port 9000
# myapi:file name, app: FastAPI instance (app=FastAPI()), --reload: auto reload server on code changes 
#In production, it’s common to use both,Gunicorn for process management, and Uvicorn as the async worker.

#postman of fastApi 
http://127.0.0.1:9000/docs
"""
GET return info
POST create something new 
PUT update a data 
DELETE delete a data 
"""


---------------------------------------------
other commands 

git remote -v

git config user.name
git config user.email

git clone git@githb-per:Shantanu2k19/FastApi.git

git config user.name "Shantanu2k19"
git config user.email "shan@gmail.com"