import json
from flask import Flask,render_template,request,redirect,flash,url_for,abort


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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def showSummary():
    club = [club for club in clubs if club['email'] == request.form['email']]
    if not club: return abort(404)
    return render_template('welcome.html',club=club[0],competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']]
    if not competition:return abort(404) #added prevent crash
    club = [c for c in clubs if c['name'] == request.form['club']]
    if not club: return abort(404) #added prevent crash
    placesRequired = int(request.form['places'])
    pointsclub = int(club[0]["points"]) #added for issue 2
    if pointsclub < placesRequired: #added for issue 2
        flash('Can\'t buy more than your points!')#added for issue 2
        return render_template('welcome.html', club=club[0], competitions=competitions)#added for issue 2
    competition[0]['numberOfPlaces'] = int(competition[0]['numberOfPlaces'])-placesRequired
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club[0], competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))