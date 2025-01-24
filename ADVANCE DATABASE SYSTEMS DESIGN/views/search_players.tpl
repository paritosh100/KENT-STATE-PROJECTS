<!DOCTYPE html>
<html>
<head>
    <title>Search Players</title>
</head>
<body>
    <h1>Search Players</h1>
    <a href="/">Home</a>
    <form action="/search_players" method="get">
        <label for="search">Search:</label>
        <input type="text" name="search" placeholder="Enter player name">
        <input type="submit" value="Search">
    </form>

    % if players:
        <table border="1">
            <tr>
                <th>Name</th>
                <th>Position</th>
                <th>Team</th>
                <th>Action</th>
            </tr>
            % for player in players:
                <tr>
                    <td>{{ player[0] }}</td>
                    <td>{{ player[1] }}</td>
                    <td>{{ player[2] }}</td>
                    <td>
                        <a href="/update_player/{{ player[0] }}">Update</a>
                        <a href="/delete_player/{{ player[0] }}">Delete</a>
                    </td>
                </tr>
            % end
        </table>
    % else:
        <p>No results found for '{{ search_query }}'</p>
    % end
</body>
</html>
