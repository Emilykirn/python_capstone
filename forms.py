
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, SubmitField, SelectField

class LoginForm(FlaskForm):
    email = StringField('Email', [validators.InputRequired()])
    password = PasswordField('Password', [validators.InputRequired()])
    submit = SubmitField('Submit')

class RosterForm(FlaskForm):
    coach_name = StringField("Coach Name", [validators.InputRequired()])
    team_name = StringField("Team Name", [validators.InputRequired()])
    submit = SubmitField('submit')

class PlayerForm(FlaskForm):
    first_name = StringField("First Name", [validators.InputRequired()])
    last_name = StringField("Last Name", [validators.InputRequired()])
    player_number = StringField("Player Number", [validators.InputRequired()])
    player_position = StringField("Player Position", [validators.InputRequired()])
    roster_selection = SelectField("Select Team")
    submit = SubmitField('Submit')

   
    def roster_fill(self, rosters):
        self.roster_selection.choices = [ (roster.roster_id, roster.team_name) for roster in rosters ]

class TrainingLinkForm(FlaskForm):
    link = StringField("Link", [validators.InputRequired()])
    submit = SubmitField('Submit')


class CreateAccount(FlaskForm):
    email = StringField('Email', [validators.InputRequired()])
    password = PasswordField('Password', [validators.InputRequired()])
    submit = SubmitField('Submit')
