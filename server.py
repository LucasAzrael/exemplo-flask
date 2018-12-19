from flask import Flask, render_template, request, url_for
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['programas']
users = db['users']

app = Flask(__name__, template_folder='template')

title = "cadastro"
framework = "Flask!"

@app.route("/")
def home():
	return render_template(
		'index.html',
		framework=framework,
		title=title
		)

@app.route('/users', methods=['GET', 'POST'])
def users2():
	nomes = [user for user in users.find()]

	if request.method == 'POST':
		nome = request.form['nome']
		users.insert_one({'user': nome})
		nomes = [user for user in users.find()]
		return render_template('index.html', nomes=nomes)
	return render_template('index.html', nomes=nomes)


app.run(debug=True)
