from flask import Flask, render_template, request, flash, redirect, url_for
import db
import secrets

app = Flask(__name__)
app.secret_key = secrets.secret_key

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', people=db.get_people())

@app.route('/watch-something')
def watch_something():
    form = request.args
    people = [
        key[len('wants-to-watch:'):]
        for key in form.keys()
        if 'wants-to-watch:' in key
    ]
    return render_template(
        'watch-something.html',
        media=db.get_media(form['time-to-watch'], people)
    )

@app.route('/action/<action>')
def action(action=None):
    form = request.args
    if action == 'add-media':
        people = [
            key[len('wants-to-watch:'):]
            for key in form.keys()
            if 'wants-to-watch:' in key
        ]
        result = db.add_media(
            form['media-name'],
            form['media-length'],
            people
        )

        if result is True:
            flash('media added', 'success')
        else:
            flash(result, 'error')

    elif action == 'add-person':
        # add person to the database
        result = db.add_person(form['person-name'])

        # inform user of results
        if result is True:
            flash('person added', 'success')
        else:
            flash(result, 'error')

    else:
        flash('bad action', 'error')

    return redirect(url_for('home'))

app.run('0.0.0.0', 8000, debug=True)
