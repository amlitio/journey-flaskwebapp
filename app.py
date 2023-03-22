from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///journal.db'
db = SQLAlchemy(app)

class JournalEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(1000))

@app.route('/')
def index():
    entries = JournalEntry.query.all()
    return render_template('index.html', entries=entries)

@app.route('/create', methods=['GET', 'POST'])
def create_entry():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        entry = JournalEntry(title=title, content=content)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)
