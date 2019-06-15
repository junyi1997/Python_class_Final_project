<?php
$N_NAME=$_GET["N_NAME"];
$N_ID=$_GET["N_ID"];
$S_ID=$_GET["S_ID"];
$S_PHONE=$_GET["S_PHONE"];
$S_MAIL=$_GET["S_MAIL"];
$Q_CONTENT=$_GET["Q_CONTENT"];
$conn = new mysqli("sumcarm.myds.me:3307", "aaa", "aaa", "App");
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sql = "INSERT INTO `ACT_QUESTION`( `N_NAME`, `N_ID`, `S_ID`, `S_PHONE`, `S_MAIL`, `Q_CONTENT`) VALUES ( '$N_NAME', '$N_ID','$S_ID',$S_PHONE,'$S_MAIL','$Q_CONTENT')";
echo $sql;
if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>