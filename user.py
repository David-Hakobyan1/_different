from flask import Flask,render_template,request,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,SubmitField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "fasht343dgdfgr"

DATA={}
if os.path.isfile('file.txt'):
    with open("file.txt") as f:
        fc = f.read().strip()
        for l in fc.split("\n"):
            DATA[l.split(',')[0].split(':')[1]] = {}
            for el in l.split(','):
                DATA[l.split(',')[0].split(':')[1]][el.split(':')[0]] = el.split(":")[1]

class PLAY_Form(FlaskForm):
    play = SubmitField("LOGIN")

class PLAY_Form1(FlaskForm):
    play1 = SubmitField("REGISTER")

class PLAY_Form2(FlaskForm):
    fnum1 = StringField("FULL NAME:",validators = [DataRequired()])
    fnum2 = StringField("USER NAME:",validators = [DataRequired()])
    fnum3 = StringField("PASSWORD:",validators = [DataRequired()])
    play = SubmitField("SUBMIT")

class PLAY_Form3(FlaskForm):
    fnum4 = StringField("USER NAME:",validators = [DataRequired()])
    fnum5 = StringField("PASSWORD:",validators = [DataRequired()])
    play = SubmitField("SUBMIT")

@app.route("/",methods=["GET","POST"])
@app.route("/index",methods=["GET","POST"])
def index():
    form = PLAY_Form()
    form1 = PLAY_Form1()
    if form1.play1.data and form.validate_on_submit():
        form2 = PLAY_Form2()
        fnum1 = form2.fnum1.data
        fnum2 = form2.fnum2.data
        fnum3 = form2.fnum3.data
        return render_template("files1.html",form2=form2,fnum1=fnum1,fnum2=fnum2,fnum3=fnum3)
    if form.play.data and form.validate_on_submit():
        form3 = PLAY_Form3()
        fnum4 = form3.fnum4.data
        fnum5 = form3.fnum5.data
        return render_template("files2.html",form3=form3,fnum4=fnum4,fnum5=fnum5)
    return render_template("files.html",form=form,form1=form1)

@app.route("/register",methods=["GET","POST"])
def register():
    form2 = PLAY_Form2()
    fnum1 = form2.fnum1.data
    fnum2 = form2.fnum2.data
    fnum3 = form2.fnum3.data
    if fnum2 not in DATA:
        DATA[str(fnum2)]={}
        DATA[str(fnum2)]['login'] = str(fnum2)
        DATA[str(fnum2)]['parol'] = str(fnum3)
        DATA[str(fnum2)]['fullname'] = str(fnum1)
        text = "login:" + str(fnum2) + ",parol:" + \
            str(fnum3) + ",fullname:" + str(fnum1) + "\n"
        if not os.path.isfile('file.txt'):
            with open("file.txt","w+") as f:
                f.write(text)
        else:
            with open("file.txt","a") as f:
                f.write(text)
        return render_template('homes.html',info="register",fnum1=fnum1,fnum2=fnum2,fnum3=fnum3)
    else:
        return render_template('homes.html',info="allready exists")

@app.route("/login",methods=["GET","POST"])
def login():
    form3 = PLAY_Form3()
    fnum4 = form3.fnum4.data
    fnum5 = form3.fnum5.data
    if str(fnum4) not in DATA:
        return render_template("homes.html",info="dos not exists",fnum4=fnum4)
    else:
        if str(fnum5) == DATA[str(fnum4)]['parol']:
            return render_template('homes.html',info=DATA[str(fnum4)]['fullname'], fnum4=fnum4,fnum5=fnum5)
        else:
            return render_template('homes.html',info="wrong password",fnum5=fnum5)

@app.route("/about/<login>/<password>/<info>",methods=["GET","POST"])
def about(login=None, password=None, info=None):
    return "Fullname:"+str(info)+"\n"+"Login:"+str(login)+"\n"+"Password:"+str(password)

if __name__=="__main__":
    app.run(debug=True)
