<!-- การสร้างแอปพลิเคชัน App Inventor โดยเชื่อมต่อ กับ ไฟล์ PHP -->
<html>

<head>
    <meta name="viewport" content="width=device-width" />
    <title>Control LED with Raspberry Pi using Apache Webserver </title>
</head>
<style>
    body {
        background-color: rgb(212, 250, 252);
        font-family: 'Arial';
    }

    .green {
        background-color: green;
        width: 10em;
        height: 4em;
        font-size: 20px;
    }

    .black {
        background-color: red;

        color: #fff;

        width: 10em;
        height: 4em;
        font-size: 20px;
    }
</style>

<body>
    <center>
        <form method="get">
            <input class="green" type="submit" value="ON" name="on1">
            <input class=" black" type="submit" value="OFF" name="off1">
            <br /> <br />
            <input class="green" type="submit" value="ON" name="on2">
            <input class="black" type="submit" value="OFF" name="off2">
            <br /> <br />
            <input class="green" type="submit" value="ON" name="on3">
            <input class="black" type="submit" value="OFF" name="off3">
            <br /> <br />
            <input class="green" type="submit" value="ON" name="on4">
            <input class="black" type="submit" value="OFF" name="off4">
            <br /> <br />
        </form>
    </center>
    <?php
//------------------ หลอด 1 ----------------------------
if(isset($_GET['on1']))
{
    shell_exec("/usr/bin/sudo raspi-gpio set 17 op pn dh");
}
else if(isset($_GET['off1']))
{
    shell_exec("/usr/bin/sudo raspi-gpio set 17 op pn dl");
}
//------------------ หลอด 2 ----------------------------
if(isset($_GET['on2']))
{
    shell_exec("/usr/bin/sudo raspi-gpio set 2 op pn dh");
}
else if(isset($_GET['off2']))
{
    shell_exec("/usr/bin/sudo raspi-gpio set 2 op pn dl");
}
//------------------ หลอด 3 ----------------------------
if(isset($_GET['on3']))
{
    shell_exec("/usr/bin/sudo raspi-gpio set 23 op pn dh");
}
else if(isset($_GET['off3']))
{
    shell_exec("/usr/bin/sudo raspi-gpio set 23 op pn dl");
}
//------------------ หลอด 4 ----------------------------
if(isset($_GET['on4']))
{
    shell_exec("/usr/bin/sudo raspi-gpio set 24 op pn dh");
}
else if(isset($_GET['off4']))
{
    shell_exec("/usr/bin/sudo raspi-gpio set 24 op pn dl");
}
?>
</body>

</html>