from flask import Flask
import effects

app = Flask(__name__)

effects.raw.info()

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/api/set/<effect_name>')
def effect_handler(effect_name):
	if(hasattr(effects, effect_name)):
		getattr(effects, effect_name).info()
		return 'idiot'
	else:
		return effect_name + ' - no luck'

if __name__ == '__main__' :
	app.run()