import os
import model 
import crud 
import server

os.system('dropdb ballers')
os.system('createdb ballers')

model.connect_to_db(server.app)
with server.app.app_context():
    model.db.create_all()

    #dummy data user

    #1
    email = 'frank.r@mail.com'
    password = 'asdf'
    user = crud.create_user(email, password)

    #2
    email = 'testb@mail.com'
    password = 'asdf'
    user = crud.create_user(email, password)

    #3
    email = 'testc@mail.com'
    password = 'asdf'
    user = crud.create_user(email, password)
    
    #4
    email = 'testd@mail.com'
    password = 'asdf'
    user = crud.create_user(email, password)

    #5
    email = 'teste@mail.com'
    password = "abcd"
    user = crud.create_user(email, password)

    # dummy data roster

    coach_name = "Matthew Mara"
    team_name = "The Crickets"
    user_id = 3

    coach_name = "Frank Reynolds"
    team_name = "Daymen"
    user_id = 1
    roster = crud.create_roster(coach_name, team_name)
    model.db.session.add(roster)
    model.db.session.commit()

    coach_name = "Bruce Mathis"
    team_name = "Really Good People"
    user_id = 2
    roster = crud.create_roster(coach_name, team_name)
    model.db.session.add(roster)
    model.db.session.commit()
    
    # dummy data player

    first_name = "Dee"
    last_name = "Reynolds"
    player_number = 1
    player_position = "catcher"
    roster_id = 1
    roster_selection = "Daymen"
    player = crud.create_player(first_name, last_name, player_number, player_position, roster_selection)
    model.db.session.add(player)
    model.db.session.commit()

    first_name = "Dennis"
    last_name = "Reynolds"
    player_number = 2
    player_position = "pitcher"
    roster_selection = "Daymen"
    player = crud.create_player(first_name, last_name, player_number, player_position, roster_selection)
    model.db.session.add(player)
    model.db.session.commit()

    first_name = "Charlie"
    last_name = "Kelly"
    player_number = 3
    player_position = "right field"
    roster_selection = "Daymen"
    player = crud.create_player(first_name, last_name, player_number, player_position, roster_selection)
    model.db.session.add(player)
    model.db.session.commit()

    first_name = "Mac"
    last_name = "McDonald"
    player_number = 4
    player_position = "left field"
    roster_selection = "Daymen"
    player = crud.create_player(first_name, last_name, player_number, player_position, roster_selection)
    model.db.session.add(player)
    model.db.session.commit()

    first_name = "Maureen"
    last_name = "Ponderosa"
    player_number = 11
    player_position = "outfield"
    roster_selection = "The Crickets"
    player = crud.create_player(first_name, last_name, player_number, player_position, roster_selection)

    first_name = "The"
    last_name = "Waitress"
    player_number = 12
    player_position = "infield"
    roster_selection = "The Crickets"
    player = crud.create_player(first_name, last_name, player_number, player_position, roster_selection)

    first_name = "Gayle"
    last_name = "The Snail"
    player_number = 13
    player_position = "catcher"
    roster_selection = "The Crickets"
    player = crud.create_player(first_name, last_name, player_number, player_position, roster_selection)

    # dummy data trainings

    link = "https://www.youtube.com/watch?v=CRIxAy6RV7o"
    user_id = 2
    training = crud.add_training_link(link,user_id)
    model.db.session.add(training)
    model.db.session.commit()
    
