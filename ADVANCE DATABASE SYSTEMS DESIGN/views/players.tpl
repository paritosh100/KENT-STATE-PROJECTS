<!DOCTYPE html>
<html>
<head>
<style>
body{
        width:70%;
        font-size:20px;
        margin:0 auto;
    }
    td{
        padding:10px;
    }

</style>
    <title>Players</title>
</head>
<body>
    <h1>Players</h1>
    <a href="/" >Home</a>
    <table border="1">
        <tr>
            <th>ID</th>
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
                <td>{{ player[3] }}</td>
                <td>
                    <a href="/update_player/{{ player[0] }}">Update</a>
                    <a href="/delete_player/{{ player[0] }}">Delete</a>
                </td>
            </tr>
        % end
    </table>
<a href="/add_player">Add Player</a>

</body>
</html>
