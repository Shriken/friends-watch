from flask import Flask, render_template, request, flash
import db
import secrets

app = Flask(__name__)
app.secret_key = secrets.secret_key

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form = request.form
        if form['submit-type'] == 'add-media':
            return 'adding media'
        elif form['submit-type'] == 'add-person':
            # add person to the database
            result = db.add_person(form['person-name'])

            # inform user of results
            if result is False:
                flash('person already exists', 'error')
            else:
                flash('person added', 'success')
        else:
            flash('bad form input format', 'error')

    return render_template('home.html', people=db.get_people())

app.run('0.0.0.0', 8000, debug=True)
