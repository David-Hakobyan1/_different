from project import db
from project.models import User

harc = Blueprint('harc',__name__)

harcer = {'harc':"amenamec shun@?",'patasxanner':['dev','mastif','arj'],'chisht_patasxan':'mastif'}
harcs = harcer['harc']
pat = harcer['patasxanner']
chpat = harcer['chisht_patasxan']
user = User(harc=harcs,patasxanner=pat,chisht_patasxan=chpat)
db.session.add(user)
db.commit()

@harcer.route('/register',methods=['GET','POST'])
def home():
    ls = User.query.all()
    return ls
