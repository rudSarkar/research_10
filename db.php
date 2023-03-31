<?php

$servername = "db";
$username = "root";
$password = "SecurePasswordEasyToGuess";
$dbname = "research_10_db";

$conn = new mysqli($servername, $username, $password, $dbname, 3306);

// Check connection
if ($conn -> connect_errno) {
  echo "Failed to connect to MySQL: " . $mysqli -> connect_error;
  exit();
}

?>
