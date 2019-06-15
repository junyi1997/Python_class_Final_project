<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta charset="utf-8">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
  <style>
  .table td {
   text-align: center;   
}
.table tr {
   text-align: center;   
}
  </style>
</head>
<body>

<div class="container">
<div class="dropdown">

  <div class="table-responsive">
    <table class="table table-bordered">
      <thead>
        <tr>
          <th>標籤</th>
          <th>標題</th>
          <th>日期</th>
        </tr>
      </thead>
      <tbody>
          <?php
            if (isset($_GET['search']))
            {
              $search= $_GET['search'];
              $sql = "SELECT * FROM `NEWS` WHERE `N_TAG` = '$search'";
            }

            $conn = new mysqli("sumcarm.myds.me:3307", "aaa", "aaa", "App");

            if ($conn->connect_error) {
                die("Connection failed: " . $conn->connect_error);
            } 
            if (!isset($_GET['search']))
            {
              $sql = "SELECT * FROM `NEWS` ";

            }
            $result = $conn->query($sql);
            if ($result->num_rows > 0) {
                while($row = $result->fetch_assoc()) {
                    echo "<tr>";
                    echo "<td>".$row['N_TAG']."</td>";
                    echo "<td>"."<a href=viewnews.php?N_ID=".$row['N_ID'].">".$row['N_SUBJECT']."</td>";
                    echo "<td>".$row['N_DATE']."</td>";
                    echo"</tr>";
                }
            } 
          ?>


      </tbody>
    </table>
  </div>
</div>

</body>
</html>
