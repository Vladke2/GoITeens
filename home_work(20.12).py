from . import app, login_manager
from flask import render_template, request, redirect, url_for, flash, session
from .models.database import session
from .models.user import User
# from .app import db, Article, User
from werkzeug.security import generate_password_hash
from flask_login import login_required
from .forms import LoginForm


@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        username = request.form["name"]
        password = request.form["password"]

        user = session.query(User).where(User.username == username).first()

        if user:
            flash('цей користувач вже існує')
            return redirect(url_for("login"))

        new_user = User(
            username=username,
            password=generate_password_hash(password)
        )
        try:
            session.add(new_user)
            session.commit()
        except Exception as exc:
            return f"При збереженні користувача виникла помилка: {exc}"
        finally:
            session.close()
            return redirect("/login")
    else:
        return render_template("signup.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm
    return render_template("login.html", form=form)


@login_manager.user_loader
def load_users(user_id):
    return session.query(User).get(int(user_id))


@app.route('/logout')
@login_required
def logout():
    load_users()
    return redirect('main')
