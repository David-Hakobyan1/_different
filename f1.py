from flask import Flask,render_template,url_for,request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("f1.html")

@app.route("/about")
def about():
    name = request.args.get("name")
    surname = request.args.get("surname")
    login = request.args.get("login")
    password = request.args.get("password")
    return render_template("F1.html",name=name,surname=surname)

if __name__=="__main__":
    app.run(debug=True)
