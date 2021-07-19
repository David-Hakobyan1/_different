from flask import Flask,render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "fasht"

class Calc_Form(FlaskForm):
    fnum = StringField("first number:",validators = [DataRequired()])
    act = StringField("enter action:",validators = [DataRequired()])
    snum = StringField("secound number:",validators = [DataRequired()])
    calc = SubmitField("calculate")

@app.route("/",methods=["GET","POST"])
@app.route("/index",methods=["GET","POST"])
def index():
    summ = ""
    act = None
    fnum = None
    snum = None
    form = Calc_Form()
    if form.validate_on_submit():
        fnum = form.fnum.data
        snum = form.snum.data
        act = form.act.data
    if act == "+":
        summ = int(fnum)+int(snum)

    return render_template("f1.html",form=form,summ=summ)

if __name__=="__main__":
    app.run(debug=True)
