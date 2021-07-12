from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path

app = Flask(__name__) # __name__ is the name of the file i believe
app.secret_key = 'fagadfasdf'

# home route along with home function which says which one is the homepage
@app.route('/')
def home():
	return render_template('index.html') # render template allows you to render html pages

# route for allowing the webpage to share the input given by the user
# Using POST allows us to hide the info from the search engine but GET shows them
# We have put both the methods inside the methods params of route so that we can make conditional statements for them to avoid the users/webpage from making GET requests...
@app.route('/your-url', methods=["GET", "POST"])
def your_url():
	if request.method == 'POST':
		urls = {}

		if os.path.exists('urls.json'):
			with open('urls.json') as urls_file:
				urls = json.load(urls_file)

		if request.form['code'] in urls.keys():
			flash("That short name has already been taken.") # flashing messages
			return redirect(url_for('home'))


		urls[request.form["code"]] = {'url': request.form["url"]}
		with open('urls.json', 'w') as url_file: # with open allows you to open/create a file with another param 'w' to specify that you are writing to the file
			json.dump(urls, url_file)

		return render_template('your_url.html', code=request.form["code"]) # request.form allows you to request for inputs which has name="code"
	else:
		return redirect(url_for('home')) # redirect will redirect user to the url. url_for is being used so that it can get the home url automatically from home() function 
		# doing www.localhost.com/your-url will take the user to homepage because of this else statement
