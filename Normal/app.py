from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
app.run()






# its giving enter a number error because i had a module created somewhere name something like that