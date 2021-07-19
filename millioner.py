from flask import Flask,render_template,request,url_for,redirect
from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,SubmitField
from wtforms.validators import DataRequired
import random

app = Flask(__name__)
app.config["SECRET_KEY"] = "fasht343dgdfgr"


with open("file1.txt") as f:
    fc = f.read().strip().split("\n")

lis=[]
for i in fc:
    lis.append(i.split(":"))
rands = random.randrange(len(lis))
num = lis[rands]
number = 0

class PLAY_Form(FlaskForm):
    fnum = StringField("Your Answer:",validators = [DataRequired()])
    play = SubmitField("Ok")


@app.route("/",methods=["GET","POST"])
def home():
    global num
    form = PLAY_Form()
    fnum = form.fnum.data
    info=""
    return render_template("home.html",form=form,fnum=fnum,mylis=num,info=info)

@app.route("/about",methods=["GET","POST"])
def about():
    global num
    global number
    form = PLAY_Form()
    fnum = form.fnum.data
    for i in lis:
        if i == num:
            lis.remove(i)
    if len(lis) != 0:
        if fnum == num[2]:
            info = "Right"
            number+=1
            rands = random.randrange(len(lis))
            num = lis[rands]
            return render_template("home.html",form=form,fnum=fnum,mylis=num,info=info)
        else:
            rands = random.randrange(len(lis))
            num = lis[rands]
            info = "Wrong"
            return render_template("home.html",form=form,fnum=fnum,mylis=num,info=info)
    else:
        return render_template("endmil.html",info="END",number=number)

if __name__=="__main__":
    app.run(debug=True)
