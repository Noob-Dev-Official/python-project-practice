from flask import render_template, request, redirect, url_for, flash, abort, session, jsonify, Blueprint
import json
import os.path
from werkzeug.utils import secure_filename

bp = Blueprint('urlshort', __name__)

# home route along with home function which says which one is the homepage
@bp.route('/')
def home():
	return render_template('index.html', codes=session.keys()) # render template allows you to render html pages

# route for allowing the webpage to share the input given by the user
# Using POST allows us to hide the info from the search engine but GET shows them
# We have put both the methods inside the methods params of route so that we can make conditional statements for them to avoid the users/webpage from making GET requests...
@bp.route('/your-url', methods=["GET", "POST"])
def your_url():
	if request.method == 'POST':
		urls = {}

		if os.path.exists('urls.json'):
			with open('urls.json') as urls_file:
				urls = json.load(urls_file)

		# check if the key has been taken and saved in JSON file
		if request.form['code'] in urls.keys():
			flash("That short name has already been taken.") # flashing messages
			return redirect(url_for('urlshort.home'))

		# check if it is a file or URL
		if 'url' in request.form.keys():
			urls[request.form["code"]] = {'url': request.form["url"]}
		else:
			# save the file
			f = request.files['file']
			full_name = request.form['code'] + secure_filename(f.filename) # secure_file checks whether if the file is secure and not a virus

			f.save('/home/bimec/Python-project-practice/url_shortener_flask/urlshort/static/user_files/' + full_name)

			# save the file url request inside JSON file
			urls[request.form["code"]] = {'file': full_name}


		
		with open('urls.json', 'w') as url_file: # with open allows you to open/create a file with another param 'w' to specify that you are writing to the file
			json.dump(urls, url_file)

			# add shortcodes to cookies
			session[request.form['code']] = True

		return render_template('your_url.html', code=request.form["code"]) # request.form allows you to request for inputs which has name="code"
	else:
		return redirect(url_for('urlshort.home')) # redirect will redirect user to the url. url_for is being used so that it can get the home url automatically from home() function 
		# doing www.localhost.com/your-url will take the user to homepage because of this else statement

# it says, look for any sort of string after the '/' then put them in variable 'code'
@bp.route('/<string:code>')
def redirect_to_url(code):
	if os.path.exists('urls.json'):
		with open('urls.json') as urls_file:
			urls = json.load(urls_file)

			# checks if the code is in the URLs dict/JSON file
			if code in urls.keys():
				# checks if its an url or file to open
				if 'url' in urls[code].keys():
					return redirect(urls[code]['url'])
				else:
					# load the file statically
					file_url = url_for('static', filename='user_files/' + urls[code]['file'])

					return redirect(file_url)

	# if nothing works/if the code is wrong or if it is something not found inside the JSON file, then we abort/show proper error mssg
	return abort(404)

# custom route for error 404 page
@bp.errorhandler(404)
def page_not_found(error):
	return render_template('error_404.html'), 404


# for api
@bp.route('/api')
def session_api():
	return jsonify(list(session.keys()))

				

