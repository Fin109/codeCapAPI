from flask import Flask, jsonify # Import Flask and jsonify to return JSON info
import requests
app = Flask(__name__)

@app.route('/')
def index():
	return "Welcome to my API!"

@app.route('/get',methods=['GET'])
def get():
	FIXER_URL = 'https://openexchangerates.org/api/latest.json?app_id=b833cea4b2854e46ad377d019eeba7da'
	FIXER_PARAMS = {'symbols':'ZAR,EUR,CAD'}
	fixer = requests.get(FIXER_URL,params=FIXER_PARAMS)  # <---- PINGS API, gets data

	WEATHERSTACK_URL = 'http://api.weatherstack.com/current?access_key=521c56c1b05548e72c0591eb77478d04'
	WEATHERSTACK_PARAMS = {'query':'Cape Town'}
	weather = requests.get(WEATHERSTACK_URL,params=WEATHERSTACK_PARAMS) # <---- PINGS API, gets data 

	return jsonify({'usd_rates':fixer.json()['rates'],'curr_temp':weather.json()['current']['temperature']})

if __name__ == '__main__':
	app.run()
