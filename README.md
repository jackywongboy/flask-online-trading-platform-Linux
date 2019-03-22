# flask-online-trading-platform-Linux
This file is for Linux based platform. <br><br>
Using python 3.7 and Flask 1.0.2 and Mysql Database.
<br><hr>
If you are Windows users, you may use this version.<a href="https://github.com/jackywongboy/flask-online-trading-platform-windows" target="_blank">Link</a><br>
<hr>
<h1><b>How to run the app</b></h1><br>
<p>you need ae local host and database, so download XAMPP</p>
<a href="https://www.apachefriends.org/download.html" target="_blank">Download Link</a>
<p>Please follow the instruction to install Xampp</p>
<p>After you install, please try to start the local host.</p>
<p>You may have problem on starting the server.</p>
<p>Remember that you need to start the "MySql server" and "Apache2"</p>
<p>If you cannot start the above functions, you may :</p>
<ol>
    <li>sudo '/opt/lampp/manager-linux-64.run'</li><p>Start the XAMPP</p>
    <li>sudo service mysql stop</li><p>Stop the service of mysql and re-start by clicking start in XAMPP</p>
    <li>sudo /etc/init.d/apache2 stop</li><p>Stop the apache2, if your version is "apache", no need to add 2 after apache</p>
    <p> re-start by clicking start in XAMPP </p>
    <li>Ater that, click the button "Go to application" on the XAMPP </li>
</ol>
<p>you may then able to start, go to "localhost/phpmyadmin/"</p>
<hr>
<p>create a new data base name : "oceanshopdb"</p>
<p>import my SQL into Mysql</p>
<p>If it success, you may see 5 column in oceanshopdb</p>
<hr>
<p>Install python3 and pip3</p>
<p>Use pip3 install all the feathers that are need, all feathers are on the top in "app.py"</p>
<p>After import all the needed feathers, you may run the app</p>
<p>remember to add sudo before the command to update and install tools</p>
<p>go to the link of the file, command to run is:</p>
<p>python3 app.py</p>
<p>It should run successfully</p>
<h1>ENJOY!</h1>
<hr>
