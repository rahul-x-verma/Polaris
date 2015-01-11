from polaris import polaris
from flask import render_template, request
from polaris.static.algorithm.main import find_directions 
from polaris.static.algorithm.codenames import codenames
from datetime import datetime

@polaris.route('/')
@polaris.route('/index')
def index():
    return render_template('index.html')

@polaris.route('/results', methods=['POST', 'GET'])
def results():
    start = request.form.get('Start')
    dest = request.form.get('Destination')
    now = datetime.now()
    weekday = datetime.today().weekday()
    hour = now.hour
    minute = now.minute
    time = hour * 60 + minute - 360

    if time < 0:
        time += 24 * 60
        weekday -= 1
    if weekday == 6:
        weekday = "sunday"
    elif weekday == 5:
        weekday = "saturday"
    else:
        weekday = "monday"


    
    if start.startswith('Mof'):
        if time > 13 * 60:
            start_code = "MOFFITM"
        else:
            start_code = "MOFFIT"
    else:
        start_code = codenames[start]

    if dest.startswith('Mof'):
        if time > 13 * 60:
            end_code = "MOFFITM"
        else:
            end_code = "MOFFIT"
    else:
        end_code = codenames[dest]

    result = find_directions(time, weekday, start_code, end_code)
    if result:
        return render_template('results.html', results=result)
    else:
        return render_template('sorry.html')
