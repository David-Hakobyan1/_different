from flask import Flask,jsonify,request

app = Flask(__name__)

stores = [{'name':'My Wonderful Store','items':[{'name':'My item','price':15.90}]}]

# Post - used to receive data
#Get - used to send data back only

#Post/store data:{name:}
@app.route('/store',methods=['POST'])
def create_store():
    pass

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    pass

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})

#Post /store/<string:name>/item{name:,price:}
@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
    pass

# GET /store/<string:name>/item
#@app.route('/store/<string:name>/item')

if __name__=='__main__':
    app.run(debug=True)
