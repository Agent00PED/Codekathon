<!-- การเขียน PHP Script เพื่อควบคุม LED ผ่านเว็บ -->
<html> 
<head>
<meta name="viewport" content="width=device-width" />
<title>Control LED with Raspberry Pi using Apache Webserver </title>
</head>
    <style>
    body
    {
    background-color: rgb(212,250,252);
    font-family: 'Arial';
    }
    .red {
    background-color: red;
    width: 10em; height: 4em;
    font-size: 20px;
    }
    .green {
    background-color: green;
    width: 10em; height: 4em;
    font-size: 20px;
    }
    </style>
<body>
    <center><h1>ควบคุม LED ผ่านเว็บไซต์</h1>
        <form method="get">
            <input class ="red" type="submit" value="เปิด Red LED" name="ron">
                <input class=" red" type="submit" value="ปิด Red LED" name="roff">
                <br /> <br />
                <input class="green" type="submit" value="เปิด Green LED" name="yon">
                <input class="green" type="submit" value="ปิด Green LED" name="yoff">
            <br /> <br />
        </form>
    </center>
<?php
if(isset($_GET['ron']))
{
        shell_exec("/usr/bin/sudo raspi-gpio set 20 op pn dh");
}
else if(isset($_GET['roff']))
{
        shell_exec("/usr/bin/sudo raspi-gpio set 20 op pn dl");
}
else if(isset($_GET['yon']))
{
        shell_exec("/usr/bin/sudo raspi-gpio set 21 op pn dh");
}
else if(isset($_GET['yoff']))
{
        shell_exec("/usr/bin/sudo raspi-gpio set 21 op pn dl");
}
?>
</body>
</html>