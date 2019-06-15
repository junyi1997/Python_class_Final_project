<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
<script src="http://cdn.quilljs.com/1.2.0/quill.js"></script>
<script src="http://cdn.quilljs.com/1.2.0/quill.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>

<!-- Theme included stylesheets -->
<link href="http://cdn.quilljs.com/1.2.0/quill.snow.css" rel="stylesheet">
<link href="http://cdn.quilljs.com/1.2.0/quill.bubble.css" rel="stylesheet">
  
    <title>Document</title>
</head>
<body>
  <form action="" method="get">
                        <div class="form-group">
                          <label for="Subject">公告標題</label>
                          <input  class="form-control"  class="Subject"  id="Subject" placeholder="請輸入標題" required>
                          <div id="state" style="color:red;"></div>
                        </div>
                        <div class="form-group">
                          <label for="exampleFormControlSelect1">職員單位</label>
                          <input  class="form-control"  class="Dep"  id="Dep" placeholder="職員單位">
                        </div>
                        <div class="form-group">
                          <label for="exampleFormControlSelect2">公告類別</label>
                          <select class="form-control" id="tag" class="tag">
                            <option>公告</option>
                            <option>單位</option>
                            <option>焦點</option>
                            <option>徵才</option>
                            <option>活動</option>
                            <option>競賽</option>
                            <option>研習</option>
                            <option>會議</option>
                          </select>
                        </div>
                        <div class="form-group">
                          <label for="exampleFormControlTextarea1">公告日期</label>
                          <?php

                          $date=date('Y-m-d');
                          echo "<input  class='form-control' id='Date' class='Date'  value='$date' readonly>";
                          ?>
                        </div>
                      
                      <div id="toolbar"></div>
                  <div id="editor"></div>
                          </div>

                      </div>
                  </body>
                  </form>

<script>

        var toolbarOptions = [
        ['bold', 'italic', 'underline', 'strike'],
        ['blockquote', 'code-block'],
        [{'header': 1}, {'header': 2}],
        [{'list': 'ordered'}, {'list': 'bullet'}],
        [{'script': 'sub'}, {'script': 'super'}],
        [{'indent': '-1'}, {'indent': '+1'}],
        [{'direction': 'rtl'}],
        [{'size': ['small', false, 'large', 'huge']}],
        ['link', 'image', 'video', 'formula'],
        [{'color': []}, {'background': []}],
        [{'font': []}],
        [{'align': []}]
        ];
        var options = {
          debug: 'info',
          modules: {
            toolbar: toolbarOptions
          },
          placeholder: 'Textttt',
          readOnly: false,
          theme: 'snow'
        };
        var editor = new Quill('#editor', options);
          editor.insertText(0, 'Hello', 'bold', true);//set init value
        function callMe() //display current HTML
          {
            var Subject =document.getElementById("Subject").value;
            var Dep =document.getElementById("Dep").value;
            var tag =document.getElementById("tag").value;
            var Date =document.getElementById("Date").value;
            if (Subject =="")
            {
              var state = document.getElementById("state").innerText ="必填項目";
              document.getElementById("Subject").style="border-color: red;";
              
            }
            else
            {
              var html = editor.root.innerHTML;
              //document.location.href="save.php?data="+html;
              document.location.href="save.php?Subject="+Subject+"&Dep="+Dep+"&data="+html+"&tag="+tag+"&Date="+Date;
            }
           

          }
        </script>
        
        <div>HTML: </div>
        <button  id="btn1" type="button" onClick="callMe()" class="btn btn-primary">送出資料</button>
        <script>
        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
          (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
          m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
          })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
        
        ga('create', 'UA-1656750-34', 'auto');
        ga('require', 'linkid', 'linkid.js');
        ga('require', 'displayfeatures');
        ga('send', 'pageview');
        
        </script>
</html>