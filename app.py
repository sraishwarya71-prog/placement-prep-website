from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///placement.db'
db = SQLAlchemy(app)

class AptitudeQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(300), nullable=False)
    answer = db.Column(db.String(300), nullable=False)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/aptitude')
def aptitude():
    questions = AptitudeQuestion.query.all()
    return render_template('aptitude.html', questions=questions)

@app.route('/coding')
def coding():
    return render_template('coding.html')

@app.route('/interview')
def interview():
    return render_template('interview.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/companies')
def companies():
    return render_template('companies.html')

@app.route('/roadmap')
def roadmap():
    return render_template('roadmap.html')

if __name__ == '__main__':
    app.run(debug=True)