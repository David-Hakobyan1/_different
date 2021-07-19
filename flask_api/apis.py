from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

names=[]

class Name(Resource):
    def get(self,name):
        for nm in names:
            if nm['name'] == name:
                return nm
        return {'name':None},404

    def post(self,name):
        data = request.get_json()
        nm = {'name':name}
        names.append(nm)
        return names,201

class NameList(Resource):
    def get(self):
        return {'all_name':names}


api.add_resource(Name,'/<string:name>')
api.add_resource(NameList,'/names')

if __name__=="__main__":
    app.run(debug=True)
