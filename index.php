<?php
    session_start();
    require 'db.php';

    $csrf_token = bin2hex(random_bytes(32));

    if (isset($_POST['submit'])) {
        $username = mysqli_real_escape_string($conn, $_POST['username']);
        $password = mysqli_real_escape_string($conn, $_POST['password']);
        $hashed_password = password_hash($password, PASSWORD_DEFAULT);

        $token = mysqli_real_escape_string($conn, $_POST['csrf_token']);

        if (isset($_POST['csrf_token']) && $token === $_POST['csrf_token']) {
            $query = "SELECT * FROM users WHERE username = '$username';";
            $result = mysqli_query($conn, $query);
            $row = mysqli_fetch_assoc($result);

            if ($row && password_verify($password, $row['password_hash'])) {
                $_SESSION['user_id'] = $row['id'];
                header("Location: dashboard.php");
                exit();
            } else {
                $error_msg = "Invalid username or password";
            }
        } else {
            $error_msg = "CSRF token validation failed";
        }
    }

?>

<form method="POST" action="index.php">
  <input type="hidden" name="csrf_token" value="<?php echo $csrf_token ?>">
  <label>Username:</label>
  <input type="text" name="username" value="admin" required>

  <label>Password:</label>
  <input type="password" name="password" value="verySecurePassword" required>

  <button type="submit" name="submit">Log in</button>

  <?php if (isset($error_msg)) { ?>
    <p class="error"><?php echo $error_msg ?></p>
  <?php } ?>
</form>
