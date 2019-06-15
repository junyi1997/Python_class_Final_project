<?php

$data=$_GET['data'];
$Subject=$_GET['Subject'];
$Dep=$_GET['Dep'];
$tag=$_GET['tag'];
$Date=$_GET['Date'];



echo "標題".$Subject."<br>";
echo "職員".$Dep."<br>";
echo "標籤".$tag."<br>";
echo "日期".$Date."<br>";

echo "內容".$data."<br>";

$conn = new mysqli("sumcarm.myds.me:3307", "aaa", "aaa", "App");
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sql = "INSERT INTO `NEWS`( `N_SUBJECT`, `N_DEP`, `N_TAG`, `N_DATE`, `N_CONT`) VALUES ( '$Subject', '$Dep','$tag','$Date','$data')";
echo $sql;
if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}
?>