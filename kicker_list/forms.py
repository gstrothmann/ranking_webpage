from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from kicker_list.db_models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                           validators = [DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                                     validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')
            
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('There is already is account using this email.')
    
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')
    
    
class UpdateAccountForm(FlaskForm):
    username = StringField('Username', 
                           validators = [DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators = [FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')
    
    def validate_username(self, username):
        if username.data!= current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')
            
    def validate_email(self, email):
        if email.data!= current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('There is already is account using this email.')

nameChoices = [(None, ''),('firas','Firas'), ('gidi','Gidi'), ('timo','Timo'), ('eric','Eric')]
resultChoices = [(None, ''),('0','0'), ('1','1'), ('2','2')]

def unique_players(form, field):
    players_set = set([form.player1.data, form.player2.data, form.player3.data, form.player4.data])
    if len(players_set)<4:
        raise ValidationError('Please select four unique players.')
        
def validate_result(form, field):
    scores = [form.scoreTeam1.data, form.scoreTeam2.data]
    possible_score = True
    if '2' not in scores:
        possible_score = False
    if ('1' not in scores) and ('0' not in scores):
        possible_score = False
    if possible_score == False:
        raise ValidationError('Not a valid result.')
        

class GameResultForm(FlaskForm):
    player1 = SelectField('Player 1', choices = nameChoices, validators = [DataRequired(), unique_players])
    player2 = SelectField('Player 2', choices = nameChoices, validators = [DataRequired(), unique_players])
    player3 = SelectField('Player 3', choices = nameChoices, validators = [DataRequired(), unique_players])
    player4 = SelectField('Player 4', choices = nameChoices, validators = [DataRequired(), unique_players])
    scoreTeam1 = SelectField('Score Team 1', choices = resultChoices, validators = [DataRequired(), validate_result])
    scoreTeam2 = SelectField('Score Team 2', choices = resultChoices, validators = [DataRequired(), validate_result])
    submit = SubmitField('Save Game Result')
    
