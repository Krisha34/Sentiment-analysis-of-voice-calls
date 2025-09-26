<?php
session_start();

if (!isset($_SESSION['loggedin']) || $_SESSION['loggedin'] !== true) {
    header("location: login.php");
    exit;
}
?>

<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
          integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
          crossorigin="anonymous">
          <title>Sentiment Analysis of voice calls</title>
    <style>
        body {
            background-image: url('https://media.licdn.com/dms/image/C4E12AQFreLvC3_y0lw/article-cover_image-shrink_720_1280/0/1560799295125?e=2147483647&v=beta&t=_TbbVemMMfhOnThbZcHtWN-2sTA_lpUDXVbg-Gv7qS0');
            background-size: cover;
            background-repeat: no-repeat;
        }

        .container {
            text-align: center;
            margin-top: 50px;
        }

        .button {
            display: inline-block;
            background-color: #4CAF50;
            color: white;
            padding: 14px 28px;
            margin: 8px 0;
            border: none;
            cursor: pointer;
            border-color: rgb(8, 133, 243);
            border-radius: 4px;
            text-decoration: none;
        }

        .button:hover {
            background-color: #f70707;
        }

        h1 {
            text-align: center;
            margin-top: 30px;
            color: rgb(248, 246, 250);
        }
    </style>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <a class="navbar-brand" href="#">Admin Login System</a>

    <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav ml-auto">
            <?php if(isset($_SESSION['loggedin']) && $_SESSION['loggedin'] === true): ?>
                <li class="nav-item">
                    <a class="nav-link" href="logout.php">Logout</a>
                </li>
            <?php endif; ?>
        </ul>
    </div>
</nav>


<div class="container mt-4">
    <h3><?php echo isset($_SESSION['username']) ? "Welcome " . $_SESSION['username'] : "Welcome"; ?>! You can now
        use this website</h3>
    <hr>

    
    <!-- Button to launch the GUI -->
    
</div>
<h1>Sentiment Analysis of voice calls</h1>
    <div class="container">
    <button class="btn btn-primary" onclick="browse()">Browse</button>
        <button class="btn btn-primary" onclick="launchGUI()">Live Recording</button>
    </div>

<!-- Bootstrap JS (optional, only needed if you want to use Bootstrap features) -->
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
        crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
        integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
        crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
        integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
        crossorigin="anonymous"></script>

<script type="text/javascript">
    function launchGUI() {
        // Replace with the appropriate URL to launch your GUI (app.py)
        window.location.href = "http://127.0.0.1:5000/"; // Change the URL if needed
    }
</script>

<script type="text/javascript">
    function browse() {
        // Replace with the appropriate URL to launch your GUI (app.py)
        window.location.href = "http://127.0.0.1:5000/result"; // Change the URL if needed
    }
</script>

</body>
</html>
