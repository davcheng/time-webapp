# Time-webapp

Build a web app that prints out the number of milliseconds since the start of January 1st, 1970, Coordinated Universal Time (UTC). (50%)

Hint: that start time is also called the “epoch” or “Unix time”.

Build it using Flask.

Deploy to Heroku.

The site must be available at `<NET_ID>-time.herokuapp.com`. In other words, the third-level domain needs to be prefixed with your NetID. (50%)


how to push a flask app to heroku:
1. create requirements.txt
include: 
	
	```
	Flask==0.11.1
	Jinja2==2.7.3
	MarkupSafe==0.23
	Werkzeug==0.10.1
	gunicorn==19.6
	```

2. create a Procfile

	```
	web: gunicorn [app name, e.g., if main.py, use "main"]:app
	```

2. create heroku app

	```
	heroku create [app name, more importantly [WHATEVER YOU TYPE].heroku.com]
	```

3. deply code

	```
	git push heroku master
	```	
note, this will fail if requirements.txt is not created (will say no flask)

4. ensure at least one instance of app is running

	```
	heroku ps:scale web=1
	```	
if so, will show something like "Scaling dynos... done, now running web at 1:Free"

6. revel in glory

	```bash
	heroku open
	```

