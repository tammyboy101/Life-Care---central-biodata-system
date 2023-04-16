<?php

$servername = "localhost"; // Replace with your database server name
$username = "username"; // Replace with your database username
$password = "password"; // Replace with your database password
$dbname = "database_name"; // Replace with your database name

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

?>
<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $name = $_POST["name"];
  $email = $_POST["email"];
  $phone = $_POST["phone"];
  $notes = $_POST["notes"];

  // Prepare and bind the SQL statement
  $stmt = $conn->prepare("INSERT INTO medical_records (name, email, phone, notes) VALUES (?, ?, ?, ?)");
  $stmt->bind_param("ssss", $name, $email, $phone, $notes);

  // Execute the SQL statement
  if ($stmt->execute() === TRUE) {
    echo "Medical record added successfully!";
  } else {
    echo "Error: " . $sql . "<br>" . $conn->error;
  }

  // Close the prepared statement and the database connection
  $stmt->close();
  $conn->close();
}

?>