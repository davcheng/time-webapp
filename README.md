# Time-webapp

Homework assignment: Build a web app that prints out the number of milliseconds since the start of January 1st, 1970, Coordinated Universal Time (UTC). (50%)

Build it using Flask.

Deploy to Heroku/Aws

The site must be available at `<NET_ID>-time.herokuapp.com`. In other words, the third-level domain needs to be prefixed with your NetID. (50%)

## How to push a flask app to aws:
http://www.datasciencebytes.com/bytes/2015/02/24/running-a-flask-app-on-aws-ec2/

1. create amazon account
2. Connect to instance
- install CLI
- http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html
- IAM group (download key )
- get .pem
- configure AWS CLI with IAM download (need to run aws configure and type in your IAM credentials)
- ssh in with:
```
chmod 600 /path/my-key-pair.pem
ssh -i /path/my-key-pair.pem ubuntu@ec2-198-51-100-1.compute-1.amazonaws.com
```

3. setup the instance
	```
	$ sudo apt-get update
	$ sudo apt-get install apache2
	$ sudo apt-get install libapache2-mod-wsgi
	```

4. install flask on ec2 instance
	```
	$ sudo apt-get install python-pip
	$ sudo pip install flask
	```

5. create app directory and symlink
	```
	$ mkdir ~/flaskapp
	$ sudo ln -sT ~/flaskapp /var/www/html/flaskapp
	```
6. test things are working with static page:
	```
	$ cd ~/flaskapp
	$ echo "Hello World" > index.html
	```

7. Create .wsgi file locally (to be pulled into folder)

	``` python
	import sys
	sys.path.insert(0, '/var/www/html/flaskapp')

	from [hello.py file => "hello"] import app as application
	```

8. git pull app into your app folder on your ec2 instance (remove test file too)

9. enable mod_wsgi
nav into folder containing your app folder and run vim to edit
```bash
vim ../../etc/apache2/sites-enabled/000-default.conf
```
insert this after the ```DocumentRoot /var/www/html``` line:
```
WSGIDaemonProcess flaskapp threads=5
WSGIScriptAlias / /var/www/html/flaskapp/flaskapp.wsgi

<Directory flaskapp>
    WSGIProcessGroup flaskapp
    WSGIApplicationGroup %{GLOBAL}
    Order deny,allow
    Allow from all
</Directory>
```

if you have issues writing the file:
```
:w !sudo tee % > /dev/null
```
source: http://stackoverflow.com/questions/8253362/etc-apt-sources-list-e212-cant-open-file-for-writing

10. restart web server
```bash
sudo apachectl restart
```

11. check it out at your public dns
http://ec2-xx-xxx-xx.us-[region]-2.compute.amazonaws.com/

12. error logs:
located here:
```
/var/log/apache2/error.log
```

### to configure domain
https://aws.amazon.com/getting-started/tutorials/get-a-domain/

1. click elastic ips in console
2. click allocate New Address
3. copy your new ip:
35.162.184.28
35.162.184.28
4. go associate
5. go to domain registration
https://console.aws.amazon.com/route53/home?region=us-east-1#
6. buy/transfer a domain
7.https://aws.amazon.com/getting-started/tutorials/get-a-domain/
8. create subdomain hosting zone
Sign in to the Route 53 console, and select Hosted Zones from the navigation pane on the left.
Choose Create Hosted Zone.
Enter the following information into the corresponding fields:
For Domain Name, type your domain name; for example, “subdomain.example.com”.
For Type, choose Public.
Choose Create.
9. create an A record for your subdomain, using the IP of whatever your subdomain points to
10. copy your subdomain ns' and create a new record in your main domain (example.com) and add the ns' of your sub to the main with the subdomain.example.com as the hosted zone name
11. check subdomain



## How to push a flask app to heroku:
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

3. create heroku app

	```
	heroku create [app name, more importantly [WHATEVER YOU TYPE].heroku.com]
	```

4. deply code

	```
	git push heroku master
	```	
note, this will fail if requirements.txt is not created (will say no flask)

5. ensure at least one instance of app is running

	```
	heroku ps:scale web=1
	```	
if so, will show something like "Scaling dynos... done, now running web at 1:Free"

6. revel in glory

	```bash
	heroku open
	```

source: https://devcenter.heroku.com/articles/getting-started-with-python#introduction