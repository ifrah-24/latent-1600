from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return "Hello , Devops Noobs!"

@app.route('/test')
def tests():
   return "How are you dear ?"

if __name__ == "__main__":
   app.run(host='0.0.0.0',port=5000)
