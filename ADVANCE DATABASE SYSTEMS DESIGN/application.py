from bottle import Bottle, template, request, redirect,route,run
import sqlite3



conn = sqlite3.connect("soccer.db")
cursor = conn.cursor()

@route('/')
def home():
    return template('home')

@route('/players')
def players():
    cursor.execute("SELECT players.id, players.name, players.position, teams.name FROM players JOIN teams ON players.team_id = teams.id")
    players = cursor.fetchall()
    return template('players', players=players)

@route('/teams')
def teams():
    cursor.execute("SELECT * FROM teams")
    teams = cursor.fetchall()
    return template('teams', teams=teams)

@route('/add_player', method='GET')
def add_player_form():
    cursor.execute("SELECT * FROM teams")
    teams = cursor.fetchall()
    return template('add_player', teams=teams)

@route('/add_player', method='POST')
def add_player():
    player_name = request.forms.get('player_name')
    position = request.forms.get('position')
    team_id = request.forms.get('team_id')

    cursor.execute("INSERT INTO players (name, position, team_id) VALUES (?, ?, ?)", (player_name, position, team_id))
    conn.commit()

    redirect('/players')

@route('/update_player/<player_id>', method='GET')
def update_player_form(player_id):
    cursor.execute("SELECT * FROM players WHERE id=?", (player_id,))
    player = cursor.fetchone()

    cursor.execute("SELECT * FROM teams")
    teams = cursor.fetchall()

    return template('update_player', player=player, teams=teams)

@route('/update_player/<player_id>', method='POST')
def update_player(player_id):
    player_name = request.forms.get('player_name')
    position = request.forms.get('position')
    team_id = request.forms.get('team_id')

    cursor.execute("UPDATE players SET name=?, position=?, team_id=? WHERE id=?", (player_name, position, team_id, player_id))
    conn.commit()

    redirect('/players')

@route('/delete_player/<player_id>')
def delete_player(player_id):
    cursor.execute("DELETE FROM players WHERE id=?", (player_id,))
    conn.commit()

    redirect('/players')

@route('/search_players')
def search_players_form():
    return template('search_players', players=None, search_query=None)

@route('/search_players', method='get')
def search_players():
    search_query = request.query.get('search', '').strip()

    if search_query:
        # If there's a search query, filter players based on the name
        cursor.execute("SELECT players.name, players.position, teams.name FROM players JOIN teams ON players.team_id = teams.id WHERE players.name LIKE ?", ('%' + search_query + '%',))
        players = cursor.fetchall()
    else:
        # If no search query, set players to None
        players = None

    return template('search_players', players=players, search_query=search_query)

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
