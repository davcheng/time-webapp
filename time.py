from flask import Flask, render_template
import time
import calendar


app = Flask(__name__)

@app.route('/')
def index():
    # millimeter = get_time()
    millimeter = 3
    return render_template('index.html', time=millimeter)

def get_time():
    # seconds = calendar.timegm(time.gmtime())
    return 3
