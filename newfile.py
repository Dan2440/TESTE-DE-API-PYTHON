from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def homepage():
	return 'A api está no ar.'

@app.route('/home')
def show():
	valor = [
		{'nome': 0, 'cod': 0}
	]
	return jsonify(valor)

if __name__ == "__main__":	
	app.run(debug=True)