<!DOCTYPE html>
<html>
<head>
    <title>Teams</title>
</head>
<body>
    <h1>Teams</h1>
    <a href="/">Home</a>
    <table border="1">
        <tr>
            <th>Team ID</th>
            <th>Team Name</th>
        </tr>
        % for team in teams:
            <tr>
                <td>{{ team[0] }}</td>
                <td>{{ team[1] }}</td>
            </tr>
        % end
    </table>
</body>
</html>
