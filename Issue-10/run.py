from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base_index.html')

@app.route('/shedule_event', methods=['POST', 'GET'])
def shedule_event():
    return render_template('shedule_event.html')

@app.route('/register', methods=['POST', 'GET'])
def register():

    return render_template('register.html')

@app.route('/added_events', methods=[ 'GET'])
def event():
    return render_template('event.html', title=title, date=date, time=time, location=location, description=description)

@app.route('/submit_shedule_event', methods=['POST'])
def submit():
    global title, date, time, location, description
    title = request.form['title']
    date = request.form['date']
    time = request.form['time']
    location = request.form['location']
    description = request.form['description']
    
    return render_template('home.html', title=title, date=date, time=time, location=location, description=description)

if __name__ == '__main__':
    app.run(debug=True)

