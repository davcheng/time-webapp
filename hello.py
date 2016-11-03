from flask import Flask, render_template
import time
import calendar
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    seconds = get_time()
    return render_template('index.html', time=seconds)

def get_time():
    seconds = time.time()
    # format to un-scientific notation it
    unsci_sec = '{:.0f}'.format(seconds)
    return unsci_sec
