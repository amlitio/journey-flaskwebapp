from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///journal.db'
db = SQLAlchemy(app)

class JournalEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(500), nullable=False)

@app.route('/')
def index():
    entries = JournalEntry.query.all()
    return render_template('index.html', entries=entries)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        entry = JournalEntry(title=request.form['title'], content=request.form['content'])
        db.session.add(entry)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)
