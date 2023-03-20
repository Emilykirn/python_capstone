
from crypt import methods
import email
from flask import Flask, render_template, request, flash, session, redirect, url_for
import crud
from forms import CreateAccount, TrainingLinkForm, LoginForm, PlayerForm, RosterForm
from model import Player, Training, connect_to_db, db, User, Roster
from jinja2 import StrictUndefined
from flask_login import UserMixin, LoginManager,current_user, login_user, login_required, logout_user



app = Flask(__name__)
app.config['SECRET_KEY'] = 'asecret'
app.jinja_env.undefined = StrictUndefined
login_manager = LoginManager()
login_manager.init_app(app, add_context_processor=True)

@login_manager.user_loader
def load_user(user_id):  
    return User.query.get(user_id)

@app.route("/")
def home():

    return render_template('homepage.html')


@app.route("/create-account", methods=["POST", "GET"])
def register():
    form = CreateAccount()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")
        if user: 
            flash("Unable to create account!")
        return redirect(url_for("home"))
    return render_template("create-account.html", form = form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        print('**************') 
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email, password = password).first()
        if user:
            if user == user:
                login_user(user)
                
                return redirect("/")
        return "Try again"
    else:
        return render_template("login.html", form=form)

@login_required
@app.route("/add-player", methods=["POST", "GET"])
def add_player():
    form = PlayerForm()
    form.roster_fill(current_user.rosters)
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name =  form.last_name.data
        player_number =  form.player_number.data
        player_position =  form.player_position.data
        roster_selection = form.roster_selection.data
        new_player = crud.create_player(first_name, last_name, player_number, player_position, roster_selection)
        flash("Added Player")
    return render_template("add_player.html", form=form)

@login_required
@app.route("/players")
def list_players():
    players = crud.get_players()
    return render_template('players.html', players=players)

@login_required
@app.route("/players/<player_id>")
def player(player_id):
    player = crud.get_player(player_id)
    return render_template('player.html', player=player)

@login_required
@app.route('/update-player/<player_id>', methods=["POST", "GET"])
def update_player_number(player_id):
    player = crud.get_player(player_id)
    form = PlayerForm(obj=player)
    form.roster_fill(current_user.rosters)
    if form.validate_on_submit():
        print('******************')
        first_name = form.first_name.data
        last_name = form.last_name.data
        player_number = form.player_number.data
        player_position = form.player_position.data
        roster_selection = form.roster_selection
        player = crud.update_player(player_id, first_name, last_name, player_number, player_position, roster_selection)
        flash("Player Updated")
    return render_template("update_player.html", form = form, player = player)

@login_required
@app.route('/delete-player/<player_id>')
def delete_player(player_id):

    player = crud.delete_player(player_id)
    
    return redirect(url_for("list_players"))

@login_required
@app.route("/add-roster", methods=["GET", "POST"])
def add_roster():
    rosters = crud.get_rosters()
    form = RosterForm()

    if form.validate_on_submit():
        print("****************")
        coach_name = form.coach_name.data
        team_name =  form.team_name.data

        roster = crud.create_roster(coach_name, team_name, current_user.id)

        flash("Added Roster")
   
    return render_template("add_roster.html", form=form, rosters=rosters)

@login_required
@app.route("/rosters")
def list_rosters():
    rosters = crud.get_rosters()
    return render_template("rosters.html", rosters=rosters)

@login_required
@app.route("/roster/<roster_id>")
def roster(roster_id):
    roster = crud.get_roster(roster_id)
    return render_template("roster.html", roster=roster)

@login_required
@app.route("/update-roster/<roster_id>", methods=['GET','POST'])
def update_roster(roster_id):
    roster = crud.get_roster(roster_id)
    form = RosterForm(obj=roster)
    if form.validate_on_submit():
        coach_name = form.coach_name.data
        team_name = form.team_name.data
        coach_name = crud.update_roster(roster_id, coach_name, team_name)
        flash("Updated!")
    return render_template("update_roster.html", form = form, roster=roster )

@login_required
@app.route('/delete-roster/<roster_id>')
def delete_roster(roster_id):

    roster = crud.delete_roster(roster_id)
    return redirect(url_for("list_rosters"))

@login_required
@app.route("/add-training", methods=['GET', 'POST'])
def add_trainings():
    form = TrainingLinkForm()
    if form.validate_on_submit():
        link = form.link.data
        # current_user.id with session as argument in new_link= 
        new_link = crud.add_training_link(link, 1)   
        flash("Added Link")         
    return render_template("add_trainings.html", form=form)    

@login_required
@app.route("/trainings")
def list_trainings():

    trainings = crud.get_links()
    return render_template("trainings.html", trainings=trainings)

@login_required
@app.route('/delete-training/<training_id>')
def delete_training(training_id):

    training = crud.delete_training(training_id)
    return redirect(url_for("list_trainings"))

@app.route("/logout")
def logout():
    logout_user()
    flash("Logged out.")
    return redirect("/login")


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, port=8000, host="localhost")

