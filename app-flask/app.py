from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_word():
    return "<h1>MINHA PRIMEIRA API</h1><p>Hey Jailson!</p>"

@app.get("/login")
def login_get():
    return "mostrou login"

@app.post("/login")
def login_post():
    data = request.json
    return {
       "name" : data['name'],
       "idade" : data['idade'],
       "cidade" : data['cidade']
    }

if __name__ == "__main__":
	app.run()
      
