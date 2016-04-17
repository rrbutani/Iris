from flask import Flask, request
import effects
import lights

app = Flask(__name__)

effects.raw.info()

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/api/set/<effect_name>')
def effect_handler(effect_name):
	if(hasattr(effects, effect_name)):
		getattr(effects, effect_name).info()
		getattr(effects, effect_name).run(lights.strip, request.args)
		return effect_name + 'idiot'
	else:
		return effect_name + ' - no luck'

if __name__ == '__main__' :
	app.run(host='0.0.0.0', port=80)
