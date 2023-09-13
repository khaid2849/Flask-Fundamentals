from flask import render_template, request, url_for, redirect
from app.models import db, Todo
from flask import Blueprint

todo_bp = Blueprint(
    "todo_bp",
    __name__,
    url_prefix="/todo",
)


@todo_bp.route("/")
def index():
    incomplete = Todo.query.filter(Todo.complete == False).all()
    complete = Todo.query.filter(Todo.complete == True).all()

    return render_template("index.html", incomplete=incomplete, complete=complete)


@todo_bp.route("/add", methods=["POST"])
def add():
    todo = Todo(text=request.form["todoitem"], complete=False)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for("todo_bp.index"))


@todo_bp.route("/complete/<id>")
def complete(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = True
    db.session.commit()

    return redirect(url_for("todo_bp.index"))
