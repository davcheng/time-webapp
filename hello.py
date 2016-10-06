from flask import Flask, render_template
import time
import calendar
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    milliseconds = get_time()
    return render_template('index.html', time=milliseconds)

def get_time():
    milli = time.time() * 1000
    # format to un-scientific notation it
    unsci_milli = '{:.0f}'.format(milli)
    return unsci_milli
