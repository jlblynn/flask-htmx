from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

@app.route('/', methods=['GET', 'POST', 'DELETE'])
def index():
    if request.method == 'POST':
        if request.form.get('todo_text'):
            todo_text = request.form['todo_text']
            new_todo = Todo(text=todo_text)
            db.session.add(new_todo)
            db.session.commit()
        todos = Todo.query.all()
        return render_template('index.html', todos=todos)
    elif request.method == 'DELETE':
        todo_id = request.form['todo_id']
        todo = Todo.query.filter_by(id=todo_id).first()
        if todo:
            db.session.delete(todo)
            db.session.commit()
            return '', 204
        else:
            return '', 404
    else:
        todos = Todo.query.all()
        return render_template('index.html', todos=todos)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)