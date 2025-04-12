from flask import Blueprint, render_template, redirect, url_for, request
from run import db
from run.models import Task
from run.forms import TaskForm

main = Blueprint("main", __name__)

@main.route("/")
def index():
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)

@main.route("/add", methods=["GET", "POST"])
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data, description=form.description.data)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("main.index"))
    return render_template("add_task.html", form=form)

@main.route("/delete/<int:id>")
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("main.index"))

