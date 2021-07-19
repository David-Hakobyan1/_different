from flask import Flask,render_template,request,url_for,redirect,url_for,session
from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "fasht343dgdfgr"

cname = None
with open("bararan.txt") as f:
    fc = f.read().strip().split("\n")
    s = sorted(fc)

class PLAY_Form1(FlaskForm):
    fnum1 = StringField("Show Translation:",validators = [DataRequired()])
    play = SubmitField("Submit")

class PLAY_Form2(FlaskForm):
    fnum2 = StringField("Add Word:",validators = [DataRequired()])
    play = SubmitField("OK")

class PLAY_Form3(FlaskForm):
    play = SubmitField("word search")

@app.route("/",methods=["GET","POST"])
@app.route("/bararan",methods=["GET","POST"])
def bararan():
    form3 = PLAY_Form3()
    if form3.play.data and form3.validate_on_submit():
        return redirect(url_for("members"))
    return render_template("das.html",form3=form3,info=s)

@app.route("/members",methods=["GET","POST"])
def members():
    global cname
    form1 = PLAY_Form1()
    fnum1 = form1.fnum1.data
    form2 = PLAY_Form2()
    fnum2 = form2.fnum2.data
    if form1.play.data and form1.validate_on_submit():
        for i in s:
            for j in i.split(" "):
                if fnum1 in j:
                    info = i.replace(" ",",")
                    cname = info
                    return render_template("dasss.html",form2=form2,fnum2=fnum2,info=info)
        info = "sorry this word not in Vocabulary"
        return render_template("dasss.html",info=info)
    return render_template("dass.html",form1=form1,fnum1=fnum1)

@app.route("/Addto",methods=["GET","POST"])
def Addto():
    global cname
    st=""
    num=0
    form2 = PLAY_Form2()
    req = form2.fnum2.data
    for i in range(len(s)):
        if s[i]==cname.replace(","," "):
            s[i]=s[i]+" "+req
            num=i
    if form2.play.data and form2.validate_on_submit():
        return render_template("end.html",s=s[num])

if __name__=="__main__":
    app.run(debug=True)
