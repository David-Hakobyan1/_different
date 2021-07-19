from flask import Flask,render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,SubmitField
from wtforms.validators import DataRequired
import random

app = Flask(__name__)
app.config["SECRET_KEY"] = "fasht"

tvyalner = [{'harc': 'eleq qajer...?', 'pat': 'haykazun', 'cur': [i for i in '########']},
            {'harc': 'gexecik(homanish)?', 'pat': 'sirun', 'cur': [i for i in '#####']},
            {'harc': 'vaxenalu(homanish)?', 'pat': 'sarsapeli', 'cur': [i for i in '#########']}]
patahakan = random.randrange(0,len(tvyalner))
cur_harc  =  tvyalner[patahakan]

class PLAY_Form(FlaskForm):
    play = SubmitField("PLAY")

class PLAY_Form1(FlaskForm):
    play1 = SubmitField("OK")
    fnum = StringField("Mutq tar:",validators = [DataRequired()])

class PLAY_Form2(FlaskForm):
    play2 = SubmitField("PLAY")

@app.route("/",methods=["GET","POST"])
@app.route("/index",methods=["GET","POST"])
def index():
    form = PLAY_Form()
    form1 = PLAY_Form1()
    fnum = form1.fnum.data
    har = cur_harc['harc']
    vand = cur_harc['cur']
    pat = cur_harc['pat']
    HARC = "HARC"
    if form.play.data and form.validate_on_submit():
        return render_template("file1.html",form1=form1,fnum=fnum,har=har,vand=vand,pat=pat,HARC=HARC)
    if form1.play1.data and form1.validate_on_submit():
        c=-1
        if "#" not in vand:
            return "<h1>duq haxtel eq avart</h1>"
        else:
            for i in pat:
                c+=1
                if fnum==i:
                    vand[c]=i
                else:
                    continue
            return render_template("file1.html",form1=form1,fnum=fnum,har=har,vand=vand,pat=pat,HARC=HARC)
    return render_template("file.html",form=form)

if __name__=="__main__":
    app.run(debug=True)
