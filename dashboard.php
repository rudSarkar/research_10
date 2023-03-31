<?php
    session_start();
    require 'db.php';

    if (!isset($_SESSION['user_id'])) {
    header("Location: index.php");
    exit();
    }

    $user_id = $_SESSION['user_id'];

    $query = "SELECT * FROM users WHERE id = '$user_id'";
    $result = mysqli_query($conn, $query);
    $row = mysqli_fetch_assoc($result);

?>

<!DOCTYPE html>
<html>
<head>
  <title>Dashboard</title>
</head>
<body>
  <h1>Welcome, <?php echo $row['username'] ?>!</h1>
  <p>Your user ID is: <?php echo $row['id'] ?></p>
  <p>Your email is: <?php echo $row['email'] ?></p>
  <p>Your phone number is: <?php echo $row['phone'] ?></p>
  <p>Your account was created on: <?php echo $row['created_at'] ?></p>
</body>
</html>
