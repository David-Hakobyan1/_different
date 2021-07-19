from project import db

class User(db.Model):
    __tablename__ = 'users'
    harc = db.Column(db.String(150),unique=True,index=True)
    patasxanner = db.Column(db.String(150),unique=True,index=True)
    chisht_patasxan = db.Column(db.String(150))

    def __init__(self,harc,patasxanner,chisht_patasxan):
        self.harc = harc
        self.patasxanner = patasxanner
        self.chisht_patasxan = chisht_patasxan

    def __repr__(self):
        return "harc : {}, patasxanner : {}, chisht_patasxan : {}".format(self.harc,self.patasxanner,self.chisht_patasxan)
