from flask import Flask #import Flask class
app = Flask(__name__) # the new instance of Flask is called 'app'

@app.route('/') # names the route for flask framework
def hello_world():
    return 'Hello World!'

@app.route('/dojo') # route named dojo
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>') #must be a string
def say_hi(name):
    return f"Hi, {name.capitalize()}!" # case corrects proper nouns

@app.route('/repeat/<int:num>/<string:msg>')
def repeat_msg(num,msg):
    html = ""
    for i in range(1,num +1):
        html += f"<h1>{msg}"
    return html

@app.errorhandler(404) # customize response to particular errors
def page_not_found(e): # e is the actual error message 
    return f"Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=8000)