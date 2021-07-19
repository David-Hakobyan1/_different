from flask import Flask,render_template,make_response,url_for,request,session

app=Flask(__name__)
app.config['SECRET_KEY']='dwdwd33fdfefe3535gsdgsdd456'


@app.route("/")
def index():
    if 'visits' in session:
        session['visits']=session.get('visits')+1
    else:
        session['visits']=1
    return f"<h1>Main Page</h1><p>prasmotr:{session['visits']}"

if __name__=="__main__":
    app.run(debug=True)
