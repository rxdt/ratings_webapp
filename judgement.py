from flask import Flask, render_template, redirect, request
import model

from model import User, Movie, Rating, session as db_session

app = Flask(__name__)

@app.route("/")
def index():
    user_list = db_session.query(User).limit(5).all()
    return render_template("user_list.html", users=user_list)

@app.route("/movies/<int:id>", methods=['GET', 'POST'])
def show_movies(id):

    if request.method == 'GET':
        users_ratings = db_session.query(User).get(id).ratings
        movies = []
        for user_rating in users_ratings:
            movie = db_session.query(Movie).get(user_rating.movie_id)
            movies.append((movie, user_rating))
        return render_template("movies.html", movies=movies, user_rating=user_rating)


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html")
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        u = User(email=email, password=password)
        db_session.add(u) 
        db_session.commit()
        return redirect("/")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email is None and password is None:
            error = 'Invalid Credentials. Please try again.'
        else:
            return render_template('welcome.html', email=email)
    if request.method == 'GET':
        return render_template('login.html')


if __name__ == "__main__":
    app.run(debug = True)