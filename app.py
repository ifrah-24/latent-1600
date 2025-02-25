import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return "Hello , Devops Noobs!"

@app.route('/health')
def health():
   return {"status":"up"},200

@app.route('/test')
def tests():
   return "How are you dear ?"

if __name__ == "__main__":
   port = int(os.getenv("FLASK_PORT",5000))
   app.run(host='0.0.0.0',port=port)
