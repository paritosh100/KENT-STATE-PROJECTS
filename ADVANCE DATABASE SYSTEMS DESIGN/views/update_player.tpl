<!DOCTYPE html>
<html>
<head>
    <title>Update Player</title>
</head>
<body>
    <h1>Update Player</h1>
    <a href="/">Home</a>
    <form action="/update_player/{{ player[0] }}" method="post">
        <label for="player_name">Player Name:</label>
        <input type="text" name="player_name" value="{{ player[1] }}" required><br>

        <label for="position">Position:</label>
        <input type="text" name="position" value="{{ player[2] }}" required><br>

        <label for="team_id">Team:</label>
        <select name="team_id" required>
            % for team in teams:
                <option value="{{ team[0] }}" % if team[0] == player[3]: selected % end>{{ team[1] }}</option>
            % end
        </select><br>

        <input type="submit" value="Update Player">
    </form>
</body>
</html>
