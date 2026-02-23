
from flask import Flask
from flask import render_template
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def show_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz)
    formatted_time = moscow_time.strftime('%d.%m.%Y %H:%M:%S')
    return render_template('index.html', time=formatted_time)



if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)