from flask import Flask, render_template
import time
import calendar
import datetime

app = Flask(__name__)

# epoch = datetime.datetime.utcfromtimestamp(0)

@app.route('/')
def index():
    milliseconds = get_time()
    return render_template('index.html', time=milliseconds)

def get_time():
    milli = time.time() * 1000
    unsci_milli = '{:.0f}'.format(milli)
    return unsci_milli

# def get_time():
#     return (time.time() - epoch).total_seconds() * 1000.0
