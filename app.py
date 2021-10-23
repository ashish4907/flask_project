from flask import Flask, render_template, request, redirect, url_for
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(100))
    day = db.Column(db.String(100))
    time = db.Column(db.String(100))
    times = db.Column(db.String(100))
    duration = db.Column(db.String(100))
    subject = db.Column(db.String(100))

    def __repr__(self):
        return f"{self.date} - {self.time} - {self.times} - {self.duration} "


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        date = request.form.get('date')
        day = request.form.get('day')
        time = request.form.get('time')
        times = request.form.get('times')
        duration = request.form.get('duration')
        subject = request.form.get('subject')

        todo = User(date=date, day=day, time=time, times=times,
                    duration=duration, subject=subject)
        db.session.add(todo)
        db.session.commit()
    alltodo = User.query.all()
    return render_template('index.html', alltodo=alltodo)


@app.route('/delete/<int:sno>', methods=['GET', 'POST'])
def delete(sno):
    todo = User.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
