import json
from flask import Flask,render_template,request,redirect,flash,url_for,abort
from datetime import datetime

def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

def load_other(our_club):
    return  [club for club in clubs if club != our_club]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def showSummary():
    club = [club for club in clubs if club['email'] == request.form['email']]
    if not club: return abort(404)
    return render_template('welcome.html',club=club[0],competitions=competitions, other_clubs=load_other(club[0]))


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club]
    if not foundClub : return abort(404)
    foundCompetition = [c for c in competitions if c['name'] == competition]
    if not foundCompetition : return abort(404)
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub[0],competition=foundCompetition[0])
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=foundClub[0], competitions=competitions, other_clubs=load_other(foundClub[0]))


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']]
    if not competition:return abort(404) #added prevent crash

    club = [c for c in clubs if c['name'] == request.form['club']]
    if not club: return abort(404) #added prevent crash

    if datetime.strptime(competition[0]["date"], "%Y-%m-%d %H:%M:%S") < datetime.now():
        flash('Can\'t buy, the competion has ended!')#added for issue 5
        return render_template('welcome.html', club=club[0], competitions=competitions, other_clubs=load_other(club[0]))
    
    placesRequired = int(request.form['places'])
    if placesRequired > int(competition[0]["numberOfPlaces"]):
        flash('Can\'t buy more than available places!')
        return render_template('welcome.html', club=club[0], competitions=competitions, other_clubs=load_other(club[0]))
    
    pointsclub = int(club[0]["points"]) #added for issue 2
    if pointsclub < placesRequired or placesRequired > 12: #added for issue 2  and issue 4
        flash('Can\'t buy more than your points or more than 12 places!')#added for issue 2  and issue 4
        return render_template('welcome.html', club=club[0], competitions=competitions, other_clubs=load_other(club[0]))#added for issue 2
    
    competition[0]['numberOfPlaces'] = int(competition[0]['numberOfPlaces'])-placesRequired
    club[0]["points"] = int(club[0]["points"])-placesRequired#issue 6
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club[0], competitions=competitions, other_clubs=load_other(club[0]))


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))