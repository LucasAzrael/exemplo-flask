from flask import Flask
from flask.ext.pymongo import PyMongo


app = flask(__name__)
client = MongoClient('localhost', 27017)
app.config['MONGO_DBNAME'] = 'CRUD'
app.config['MONGO_URI'] = 'mongodb://<dbuser>:<dbpassword>@ds063919.mlab.com:63919/crud7'

mongo = PyMongo(app)

@app.route('/create')
def create():
     user = mongo.db.users
     user.insert({'nome':'lucas','espécie': 'humano'})
     return 'usuário adicionado'
@app.route('/read')
def read():
    user = mongo.db.users
    return nome.user

@app.route('/update')
def update():
     user = mongo.db.users
     lucas = user.find.one({'nome':'lucas'})
     lucas['espécie']='lobo'
     user.save(lucas)
     return 'atualizado'
@app.route('/delete')
def delete():
     user = mongo.db.users
     lucas = user.find.one({'nome':'lucas'})
     lucas.remove()
     return 'deletado'

if __name__ =='__main__ ':
    app.run(debug=true)
