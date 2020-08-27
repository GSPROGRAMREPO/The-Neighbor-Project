index="""\

<!DOCTYPE html>
<html>
<head>
<title>The Neighbor</title>
<li style="float:right"><a class="active" href="https://www.theneighborflorida.com/">Home</a></li>

<style>

* {
    margin:0;
    padding:0;
    border:0;
}

label {
  font : 50em "Arial", sans-serif;
}


h1{
    font-family: Arial,Helvetica,sans-serif !important;
    font-size:40px;
    padding: 10px;
    background-color: rgba(255, 255, 255,.2);
}

li { font-family: Arial,Helvetica,sans-serif !important;
    font-size:30px;
    padding: 20px;
    color: black;
    display: block;
    text-align: center;
    text-decoration: none;
}

#currentTime{
    font-family: Arial,Helvetica,sans-serif !important;
    font-size: 20px;
    border-left: 1px solid #000;
    padding: 5px 5px 25px 5px;
    line-height: 1em;
    background-color: rgba(255, 255, 255,.2);
    z-index: -1;
}

#liveView{

    padding: 5px;
    height: 480;
    width: 620;
}

input[type=text] {
    font-family: Arial,Helvetica,sans-serif !important;
    font-size: 20px;
    border: 2px solid red;
    border-radius: 4px;
}

input[type=password] {
    font-family: Arial,Helvetica,sans-serif !important;
    font-size: 20px;
    border: 2px solid red;
    border-radius: 4px;
}


body{
    font-family: Arial,Helvetica,sans-serif !important;
    background-image: url('https://i.ibb.co/gFQM65Q/A-81970-VJ-6-6.jpg');
    background-repeat: no-repeat;
    background-position: center;
    background-attachment: fixed;
    background-size: 75% 50%;
}


form{
    font-family: Arial,Helvetica,sans-serif !important;
    font-size: 20px;
    font-weight: bold;
    margin : 0 auto;
    box-sizing: border-box;
    background-color: rgba(255, 255, 255,.2);
 }
 
input[type=button] {
    background-color: #4CAF50;
    border: none;
    color: white;
    padding: 8px 16px;
    text-decoration: none;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 5px;
}



input[type=submit] {

    background-color: #4CAF50;
    border: none;
    color: white;
    padding: 8px 16px;
    text-decoration: none;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 5px;

    
}


.clearer {
    clear: both;
}

</style>

</head>

<body>

<h1 style="text-align:left;">The Neighbor</h1>

<div id="liveView"></div>
<div id="currentTime"></div>

        
<form name="login">
    Username<input type="text" name="userid"/>
    Password<input type="password" name="pswrd"/>
    <input type="button" onclick="check(this.form)" value="Login"/>
</form>

<script language="javascript">

    function addCode(){  
        var img = document.createElement("img");
        img.src = "stream.mjpg";
        var src = document.getElementById("liveView");
        src.appendChild(img);
        
        
    } 

    function check(form){
        if(form.userid.value == "admin" && form.pswrd.value == "admin"){
        
            var x = document.getElementById('feedbutton');
            
            if (x.style.visibility === 'hidden') {
                x.style.visibility = 'visible';
            } else {
                x.style.visibility = 'hidden';
            }

            
            addCode()
            
        }else{ alert("Error Password or Username")}
    }
    
</script>

<script>
    function startTime() {
      var today = new Date();
      var h = today.getHours();
      var m = today.getMinutes();
      var s = today.getSeconds();
      var title = "Current Time: "
      m = checkTime(m);
      s = checkTime(s);
      document.getElementById('currentTime').innerHTML =
      title + h + ":" + m + ":" + s;
      var t = setTimeout(startTime, 500);
    }
    function checkTime(i) {
      if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
      return i;
    }
</script>


<body onload="startTime()">


<form action="http://neighbor001.ddns.net:5000/" target="_blank" id="feedbutton" style="visibility:hidden;">
    <input type="submit" value="Feed a Treat" />
</form>
   
</body>

</html>

"""
