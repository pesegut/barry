from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/index')
def index():
    course_name = 'DBMS'
    output = 'This course is ' + course_name    
    return output

@app.route('/example')
def world():    
    return render_template('hello.html')

if __name__=='__main__':
    app.run(debug=True)
