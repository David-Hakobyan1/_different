from flask import Flask,redirect,url_for,render_template,request,session
from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,SubmitField
from wtforms.validators import DataRequired


app= Flask(__name__)
app.config["SECRET_KEY"] = "fasht343dgdfgr"


class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    play = SubmitField("GO")

@app.route("/",methods=["POST","GET"])
@app.route("/home",methods=["POST","GET"])
def submit():
    form = MyForm()
    fnum = form.name.data
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('submit.html', form=form,fnum=fnum)

if __name__=="__main__":
    app.run(debug=True)
