<!DOCTYPE html>
<html>
<head>
    <title>Add Player</title>
</head>
<body>
    <h1>Add Player</h1>
    <a href="/">Home</a>
    <form action="/add_player" method="post">
        <label for="player_name">Player Name:</label>
        <input type="text" name="player_name" required><br>

        <label for="position">Position:</label>
        <input type="text" name="position" required><br>

        <label for="team_id">Team:</label>
        <select name="team_id" required>
            % for team in teams:
                <option value="{{ team[0] }}">{{ team[1] }}</option>
            % end
        </select><br>

        <input type="submit" value="Add Player">
    </form>
</body>
</html>
