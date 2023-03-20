from model import db, User, Player, Roster, Training, connect_to_db

##### ACCOUNT LOGIN

def create_user(email, password):

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()
    return user 

def user_email(email):
    return User.query.filter(User.email == email).first()

####### Create

def create_player(first_name, last_name, player_number, player_position, roster_id): 
    player = Player(first_name=first_name, last_name=last_name, player_number=player_number, player_position=player_position, roster_id=roster_id)
    db.session.add(player)
    db.session.commit()
    return player

def create_roster(coach_name, team_name, user_id):
    roster = Roster(coach_name=coach_name, team_name=team_name, user_id=user_id)
    db.session.add(roster)
    db.session.commit()

    return roster
    
### HOW TO ADD A LINK ###

def add_training_link(link, user_id):

    link = Training(link=link, user_id=user_id)
    db.session.add(link)
    db.session.commit()
    return link

########  Retrieve 

def get_players():
    player = Player.query.all()
    return player

def get_player(player_id):
    player = Player.query.get(player_id)
    return player

def get_rosters():
    rosters = Roster.query.all()
    return rosters

def get_roster(roster_id):
    roster = Roster.query.get(roster_id)
    return roster

def get_links():
    return Training.query.all()
    

####### Update

def update_player(player_id, new_first_name, new_last_name, new_player_number, new_player_position, new_roster_selection):
    player = Player.query.get(player_id)
    player.first_name = new_first_name
    player.last_name = new_last_name
    player.player_number = new_player_number
    player.player_position = new_player_position
    player.roster_selection = new_roster_selection

    db.session.commit()
    return player

def update_roster(roster_id, new_coach_name, new_team_name):
    roster = Roster.query.get(roster_id)
    roster.coach_name = new_coach_name
    roster.team_name = new_team_name 
    
    db.session.commit()
    return roster

###### Delete

def delete_player(player_id):
    player = Player.query.get(player_id)
    db.session.delete(player)
    db.session.commit()
    

def delete_roster(roster_id):
    roster = Roster.query.get(roster_id)
    db.session.delete(roster)
    db.session.commit()

def delete_training(training_id):
    training = Training.query.get(training_id)
    db.session.delete(training)
    db.session.commit()