#basic setup 

python3.8 -m venv latest
pip install fastapi uvicorn

#runserver
uvicorn myapi:app --reload #--port 9000

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

git config user.name
git config user.email
