from flask import Flask

def create_app(test_config=None):
	app = Flask(__name__) # __name__ is the name of the file i believe
	app.secret_key = 'fagadfasdf'

	# import blueprint
	from . import urlshort
	app.register_blueprint(urlshort.bp)

	return app 
