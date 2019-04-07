
#work period : 1 week
#created by : student ID : 55202288
#Assisgnment for 205com Developing the Modern Web
#created on : 11st March 2019
#coded by : VS Code
#Useing : Flask 1.0.2 & Python 3.7.2 & MySQL Database

#import features
import os
import random

from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory, flash
from flask_mail import Mail, Message
from flask_mysqldb import MySQL,MySQLdb
from flask_avatars import Avatars
from flask_uploads import UploadSet, configure_uploads, IMAGES
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField

import bcrypt
import datetime

#re-direct picture saving path
basedir = os.path.abspath(os.path.dirname(__name__))

app = Flask(__name__)

#Mysql database setting
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'oceanshopdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

#Avatars picture path setting
app.config['AVATARS_SAVE_PATH'] = os.path.join(basedir, 'avatars')
avatars = Avatars(app)

#re-direct picture saving path
app.config['UPLOADED_PHOTOS_DEST'] = 'static/image/products'
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

#Flask-Mail setting for sending Email
app.config['MAIL_SERVER'] = "smtp.outlook.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USE_TLS'] = True,
app.config['MAIL_USERNAME'] = 'ilovepython2018@outlook.com'
app.config['MAIL_PASSWORD'] = 'python123'
app.config['MAIL_DEFAULT_SENDER'] = 'ilovepython2018@outlook.com'
app.config['FLASKY_ADMIN']  = 'ilovepython2018@outlook.com'
mail = Mail(app)
#Error may cause by Google Upgrading the Security Level which cause less secure apps cannot access to gmail account

@app.route('/')
def main():#main page random show up different types of products
    cur = mysql.connection.cursor()
    values = 'tshirt'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY RAND() LIMIT 4", (values,))
    tshirt = cur.fetchall()
    values = 'jeans'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY RAND() LIMIT 4", (values,))
    jeans = cur.fetchall()
    values = 'games'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY RAND() LIMIT 4", (values,))
    games = cur.fetchall()
    values = 'mobile'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY RAND() LIMIT 4", (values,))
    mobile = cur.fetchall()
    values = 'home'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY RAND() LIMIT 4", (values,))
    home = cur.fetchall()
    return render_template('main.html', tshirt=tshirt, jeans=jeans, games=games, mobile=mobile, home=home)

@app.route('/login', methods=["GET", "POST"])
def login():#after login , return data from database to the main page
    cur = mysql.connection.cursor()
    values = 'tshirt'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY RAND() LIMIT 4", (values,))
    tshirt = cur.fetchall()
    values = 'jeans'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY RAND() LIMIT 4", (values,))
    jeans = cur.fetchall()
    values = 'games'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY RAND() LIMIT 4", (values,))
    games = cur.fetchall()
    values = 'mobile'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY RAND() LIMIT 4", (values,))
    mobile = cur.fetchall()
    values = 'home'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY RAND() LIMIT 4", (values,))
    home = cur.fetchall()

    if request.method == 'POST': # getting input from users
        inputemail = request.form['inputemail']
        inputpassword = request.form['inputpassword'].encode('utf-8')

        # start to check the username and pw are correct
        user = []
        curz = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curz.execute("SELECT * FROM users WHERE useremail=%s", (inputemail,))
        user = curz.fetchone()

        userlogin = []
        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curl.execute("SELECT * FROM users WHERE useremail=%s", (inputemail,))
        try:
            for q in curl.fetchone():
                userlogin.append(q)
        except TypeError :
            userlogin.append("1")
        curl.close()

        if  len(userlogin) > 1 :
            if bcrypt.hashpw(inputpassword, user["userpw"].encode('utf-8')) == user["userpw"].encode('utf-8'):
                session['inputid'] = user['userID']
                session['inputname'] = user['username']
                session['inputemail'] = user['useremail']

                ppic = user['profilepicture']

                session['mmobile'] = user['usermobile']
                session['aaddress'] = user['useraddress']

                if ppic == "none":
                    session['ppic'] = "/avatars/nopic.png"
                else:
                    session['ppic'] = ppic

                flash('Log In success', 'success')
                return render_template("main.html",tshirt=tshirt, jeans=jeans, games=games, mobile=mobile, home=home)
            else:
                error = "Password  Incorrect "
                session['error'] = error
                return redirect(url_for('error'))
        else:
            error = "User not Found "
            session['error'] = error
            return redirect(url_for('error'))
    else:
        return render_template("main.html",tshirt=tshirt, jeans=jeans, games=games, mobile=mobile, home=home)

@app.route('/logout')
def logout():
    cur = mysql.connection.cursor()
    values = 'tshirt'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY RAND() LIMIT 4", (values,))
    tshirt = cur.fetchall()
    values = 'jeans'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY RAND() LIMIT 4", (values,))
    jeans = cur.fetchall()
    values = 'games'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY RAND() LIMIT 4", (values,))
    games = cur.fetchall()
    values = 'mobile'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY RAND() LIMIT 4", (values,))
    mobile = cur.fetchall()
    values = 'home'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY RAND() LIMIT 4", (values,))
    home = cur.fetchall()

    session.clear()
    flash('Log Out success', 'success')
    return render_template("main.html",tshirt=tshirt, jeans=jeans, games=games, mobile=mobile, home=home)

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        inputname = request.form['inputname']
        inputemail = request.form['inputemail']
        inputpassword1 = request.form['inputpassword1'].encode('utf-8')
        inputpassword2 = request.form['inputpassword2'].encode('utf-8')
        hash_password = bcrypt.hashpw(inputpassword1, bcrypt.gensalt())
        inputmobile = request.form['inputmobile']
        inputaddress = request.form['inputaddress']

        errornumber = 0

        #check and counting how many field wasn't full in
        if len(inputname) == 0 :
            errornumber += 1
        else:
            pass

        if len(inputemail) == 0 :
            errornumber += 1
        else:
            pass

        if len(inputpassword1) == 0 :
            errornumber += 1
        else:
            pass

        if len(inputmobile) == 0 :
            errornumber += 1
        else:
            pass

        if len(inputaddress) == 0 :
            errornumber += 1
        else:
            pass

        now = datetime.datetime.now()
        now_time = now.strftime("%y-%m-%d %H:%M:%S")

        useremaillist = []
        curs = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curs.execute("SELECT * FROM users WHERE useremail=%s", (inputemail,))
        try:
            for e in curs.fetchone():
                useremaillist.append(e)
        except TypeError :
            useremaillist.append("1")
        curs.close()

        usernamelist = []
        curn = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curn.execute("SELECT * FROM users WHERE username=%s", (inputname,))
        try:
            for w in curn.fetchone():
                usernamelist.append(w)
        except TypeError :
            usernamelist.append("2")
        curn.close()

        mobilecheck = []
        try:
            int(inputmobile)
        except ValueError :
            mobilecheck.append("3")

        if errornumber == 0 :
            if len(useremaillist) == 1 :
                if len(usernamelist) == 1:
                    if len(mobilecheck) == 0:
                        if inputpassword1 == inputpassword2:
                            link_pic = "/avatars/nopic.png"

                            cur = mysql.connection.cursor()
                            cur.execute("INSERT INTO users (username, useremail, userpw, usermobile, useraddress, registerdate, profilepicture) "
                                        "VALUES (%s,%s,%s,%s,%s,%s,%s)",
                                        (inputname, inputemail, hash_password, inputmobile, inputaddress,now_time,link_pic))
                            mysql.connection.commit()

                            session['inputname'] = request.form['inputname']
                            session['inputemail'] = request.form['inputemail']
                            flash('Sign up successful', 'success')
                            return redirect(url_for('main'))

                        else:
                            error = "Retype password not correct "
                            session['error'] = error
                            return redirect(url_for('error'))
                    else:
                        error = "Mobile Number not correct "
                        session['error'] = error
                        return redirect(url_for('error'))
                else:
                    error = "Username has been used "
                    session['error'] = error
                    return redirect(url_for('error'))
            else:
                error = "Email has been used "
                session['error'] = error
                return redirect(url_for('error'))
        else:
            error = "Missing Information : " , errornumber
            session['error'] = error
            return redirect(url_for('error'))

@app.route('/error')
def error():
    return render_template("error.html")

@app.route('/success')
def success():
    return render_template("success.html")

@app.route('/personal')
def personal():
    # personal page for user to update their information
    try:
        email = session['inputemail']

        details = []
        curk = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curk.execute("SELECT * FROM users WHERE useremail=%s", (email,))
        for e in curk.fetchall():
            details.append(e['userID'])
            details.append(e['username'])
            details.append(e["usermobile"])
            details.append(e["useraddress"])
            details.append(e["registerdate"])
            details.append(e["profilepicture"])
        curk.close()

        session['userID'] = details[0]
        session['username'] = details[1]
        session['usermobile'] = details[2]
        session['useraddress'] = details[3]
        session['registerdate'] = details[4]
        session['useremail'] = email

        if details[5] == "none": #check the profile picture aren't in the correct path
            session['profilepicture'] = "/avatars/nopic.png"
        else:
            session['profilepicture'] = details[5]

        return render_template("personal.html")

    except KeyError:
        error = "Please Login"
        session['error'] = error
        return render_template("error.html")

@app.route('/avatars/<path:filename>')
def get_avatar(filename): #save the raw picture which upload by user who want to change his profile picture
    return send_from_directory(app.config['AVATARS_SAVE_PATH'], filename)

@app.route('/upload', methods=['GET', 'POST'])
def upload(): #upload page to catch up and re-direct to the above function to save the picture
    if request.method == 'POST':
        f = request.files.get('file')
        raw_filename = avatars.save_avatar(f)
        session['raw_filename'] = raw_filename
        return redirect(url_for('crop'))
    return render_template('upload.html')

@app.route('/crop', methods=['GET', 'POST'])
def crop(): #after saving the raw picture , user can crop the picture into different size base on their own
    if request.method == 'POST':
        #cropper direction info
        x = request.form.get('x')
        y = request.form.get('y')
        w = request.form.get('w')
        h = request.form.get('h')
        filenames = avatars.crop_avatar(session['raw_filename'], x, y, w, h)
        #avatars will return 3 different sizes of the cropped picture , i need the large one only
        url_l = url_for('get_avatar', filename=filenames[2])

        link = url_l
        userID = session['userID']

        # after cropping are new profile picture , upload the new filename and path to database
        curk = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curk.execute("UPDATE users SET profilepicture = %s WHERE userID = %s",(link,userID,))
        mysql.connection.commit()
        curk.close()

        return render_template('done.html', url_l=url_l)
    return render_template('crop.html')

class OrderForm(Form):  # Create Order Form for user to order product
    name = StringField('', [validators.length(min=1), validators.DataRequired()],
                       render_kw={'autofocus': True, 'placeholder': 'Full Name'})

    quantity = SelectField('', [validators.DataRequired()],
                           choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])


@app.route('/tshirt' , methods=['GET', 'POST'])
def tshirt():
    form = OrderForm(request.form)

    #from database take out all t-shirt products info
    cur = mysql.connection.cursor()
    values = 'tshirt'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY pID ASC", (values,))
    tshirt = cur.fetchall()

    if request.method == 'POST' and form.validate(): #when order action get by post , start to run the purchase process
        try:
            uuid = session['inputid']
        except KeyError:
            error = "You need to Login before ordering. "
            session['error'] = error
            return render_template('error.html')
        ppid = session['proid']
        truename = form.name.data
        howmany = form.quantity.data
        place = session['aaddress']
        mobilen = session['mmobile']
        now = datetime.datetime.now()
        time_needed = datetime.timedelta(days=5)
        arrdate = now + time_needed
        arrdate2 = arrdate.strftime("%y-%m-%d %H:%M:%S")
        special_opition = "none"

        curs = mysql.connection.cursor()
        curs.execute("INSERT INTO orders(uuid, ppid, truename, howmany, place, mobilen, buydate, arrdate, sopition) "
                     "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (uuid, ppid, truename, howmany, place, mobilen, now, arrdate2, special_opition))
        mysql.connection.commit()
        cur.close()

        session.pop('proid')
        success = "Purchase successful"
        session['success'] = success
        return render_template('success.html', oproduct=tshirt, form=form)

    if 'pid' in request.args: #product detail page , directed by the product ID
        list = []
        list2 = []
        product_id = request.args['pid']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE pID=%s", (product_id,))
        productID = curso.fetchall()

        for e in productID :
            list.append(e['uploader'])
        uploaderid = list[0]
        curid = mysql.connection.cursor()
        curid.execute("SELECT username FROM users WHERE userID=%s", (uploaderid,))
        username = curid.fetchall()
        for e in username :
            list2.append(e['username'])
        name = list2[0]

        #similar product get in database
        cur.execute("SELECT * FROM products WHERE category=%s AND pID !=%s ORDER BY RAND() LIMIT 2", (values,product_id,))
        similar = cur.fetchall()

        #add comment which re-direct to function : addcomment()
        curcom = mysql.connection.cursor()
        curcom.execute("SELECT comments.cid, comments.proid ,comments.userID, comments.ctime,comments.comment,users.username, users.profilepicture FROM comments, users WHERE comments.userID = users.userID AND comments.proid=%s ORDER BY comments.cid DESC ", (product_id,))

        comment = curcom.fetchall()
        return render_template('viewproduct.html', productID=productID, name=name ,similar=similar ,comment=comment )

    elif 'orderpid' in request.args: #if the user hit the order button , re-direct to order page by product ID

        product_id = request.args['orderpid']
        session['proid'] = product_id

        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE pID=%s", (product_id,))
        product = curso.fetchall()
        return render_template('orderproduct.html', oproduct=product, form=form)

    return render_template("tshirt.html", tshirt=tshirt)

@app.route('/jeans' , methods=['GET', 'POST'])
def jeans(): #same as the above , but different category
    form = OrderForm(request.form)

    cur = mysql.connection.cursor()
    values = 'jeans'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY pID ASC", (values,))
    jeans = cur.fetchall()
    if request.method == 'POST' and form.validate():
        try:
            uuid = session['inputid']
        except KeyError:
            error = "You need to Login before ordering. "
            session['error'] = error
            return render_template('error.html')
        ppid = session['proid']
        truename = form.name.data
        howmany = form.quantity.data
        place = session['aaddress']
        mobilen = session['mmobile']
        now = datetime.datetime.now()
        time_needed = datetime.timedelta(days=5)
        arrdate = now + time_needed
        arrdate2 = arrdate.strftime("%y-%m-%d %H:%M:%S")
        special_opition = "none"

        curs = mysql.connection.cursor()
        curs.execute("INSERT INTO orders(uuid, ppid, truename, howmany, place, mobilen, buydate, arrdate, sopition) "
                     "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (uuid, ppid, truename, howmany, place, mobilen, now, arrdate2, special_opition))
        mysql.connection.commit()
        cur.close()

        session.pop('proid')
        success = "Purchase successful"
        session['success'] = success
        return render_template('success.html', oproduct=tshirt, form=form)

    if 'pid' in request.args:
        list = []
        list2 = []
        product_id = request.args['pid']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE pID=%s", (product_id,))
        productID = curso.fetchall()

        for e in productID :
            list.append(e['uploader'])
        uploaderid = list[0]
        curid = mysql.connection.cursor()
        curid.execute("SELECT username FROM users WHERE userID=%s", (uploaderid,))
        username = curid.fetchall()
        for e in username :
            list2.append(e['username'])
        name = list2[0]

        cur.execute("SELECT * FROM products WHERE category=%s AND pID !=%s ORDER BY RAND() LIMIT 2", (values,product_id,))
        similar = cur.fetchall()

        curcom = mysql.connection.cursor()
        curcom.execute("SELECT comments.cid, comments.proid ,comments.userID, comments.ctime,comments.comment,users.username, users.profilepicture FROM comments, users WHERE comments.userID = users.userID AND comments.proid=%s ORDER BY comments.cid DESC ", (product_id,))

        comment = curcom.fetchall()

        return render_template('viewproduct.html', productID=productID, name=name ,similar=similar ,comment=comment )

    elif 'orderpid' in request.args:

        product_id = request.args['orderpid']
        session['proid'] = product_id

        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE pID=%s", (product_id,))
        product = curso.fetchall()
        return render_template('orderproduct.html', oproduct=product, form=form)

    return render_template("jeans.html", jeans=jeans)

@app.route('/games' , methods=['GET', 'POST'])
def games():
    form = OrderForm(request.form)

    cur = mysql.connection.cursor()
    values = 'games'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY pID ASC", (values,))
    games = cur.fetchall()

    if request.method == 'POST' and form.validate():
        try:
            uuid = session['inputid']
        except KeyError:
            error = "You need to Login before ordering. "
            session['error'] = error
            return render_template('error.html')
        ppid = session['proid']
        truename = form.name.data
        howmany = form.quantity.data
        place = session['aaddress']
        mobilen = session['mmobile']
        now = datetime.datetime.now()
        time_needed = datetime.timedelta(days=5)
        arrdate = now + time_needed
        arrdate2 = arrdate.strftime("%y-%m-%d %H:%M:%S")
        special_opition = "none"

        curs = mysql.connection.cursor()
        curs.execute("INSERT INTO orders(uuid, ppid, truename, howmany, place, mobilen, buydate, arrdate, sopition) "
                     "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (uuid, ppid, truename, howmany, place, mobilen, now, arrdate2, special_opition))
        mysql.connection.commit()
        cur.close()

        session.pop('proid')
        success = "Purchase successful"
        session['success'] = success
        return render_template('success.html', oproduct=tshirt, form=form)

    if 'pid' in request.args:
        list = []
        list2 = []
        product_id = request.args['pid']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE pID=%s", (product_id,))
        productID = curso.fetchall()

        for e in productID :
            list.append(e['uploader'])
        uploaderid = list[0]
        curid = mysql.connection.cursor()
        curid.execute("SELECT username FROM users WHERE userID=%s", (uploaderid,))
        username = curid.fetchall()
        for e in username :
            list2.append(e['username'])
        name = list2[0]

        cur.execute("SELECT * FROM products WHERE category=%s AND pID !=%s ORDER BY RAND() LIMIT 2", (values,product_id,))
        similar = cur.fetchall()

        curcom = mysql.connection.cursor()
        curcom.execute("SELECT comments.cid, comments.proid ,comments.userID, comments.ctime,comments.comment,users.username, users.profilepicture FROM comments, users WHERE comments.userID = users.userID AND comments.proid=%s ORDER BY comments.cid DESC ", (product_id,))

        comment = curcom.fetchall()

        return render_template('viewproduct.html', productID=productID, name=name ,similar=similar ,comment=comment )

    elif 'orderpid' in request.args:

        product_id = request.args['orderpid']
        session['proid'] = product_id

        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE pID=%s", (product_id,))
        product = curso.fetchall()
        return render_template('orderproduct.html', oproduct=product, form=form)

    return render_template("games.html", games=games)

@app.route('/mobile' , methods=['GET', 'POST'])
def mobile():
    form = OrderForm(request.form)

    cur = mysql.connection.cursor()
    values = 'mobile'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY pID ASC", (values,))
    mobile = cur.fetchall()

    if request.method == 'POST' and form.validate():
        try:
            uuid = session['inputid']
        except KeyError:
            error = "You need to Login before ordering. "
            session['error'] = error
            return render_template('error.html')
        ppid = session['proid']
        truename = form.name.data
        howmany = form.quantity.data
        place = session['aaddress']
        mobilen = session['mmobile']
        now = datetime.datetime.now()
        time_needed = datetime.timedelta(days=5)
        arrdate = now + time_needed
        arrdate2 = arrdate.strftime("%y-%m-%d %H:%M:%S")
        special_opition = "none"

        curs = mysql.connection.cursor()
        curs.execute("INSERT INTO orders(uuid, ppid, truename, howmany, place, mobilen, buydate, arrdate, sopition) "
                     "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (uuid, ppid, truename, howmany, place, mobilen, now, arrdate2, special_opition))
        mysql.connection.commit()
        cur.close()

        session.pop('proid')
        success = "Purchase successful"
        session['success'] = success
        return render_template('success.html', oproduct=tshirt, form=form)

    if 'pid' in request.args:
        list = []
        list2 = []
        product_id = request.args['pid']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE pID=%s", (product_id,))
        productID = curso.fetchall()

        for e in productID :
            list.append(e['uploader'])
        uploaderid = list[0]
        curid = mysql.connection.cursor()
        curid.execute("SELECT username FROM users WHERE userID=%s", (uploaderid,))
        username = curid.fetchall()
        for e in username :
            list2.append(e['username'])
        name = list2[0]

        cur.execute("SELECT * FROM products WHERE category=%s AND pID !=%s ORDER BY RAND() LIMIT 2", (values,product_id,))
        similar = cur.fetchall()

        curcom = mysql.connection.cursor()
        curcom.execute("SELECT comments.cid, comments.proid ,comments.userID, comments.ctime,comments.comment,users.username, users.profilepicture FROM comments, users WHERE comments.userID = users.userID AND comments.proid=%s ORDER BY comments.cid DESC ", (product_id,))

        comment = curcom.fetchall()

        return render_template('viewproduct.html', productID=productID, name=name ,similar=similar ,comment=comment )

    elif 'orderpid' in request.args:

        product_id = request.args['orderpid']
        session['proid'] = product_id

        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE pID=%s", (product_id,))
        product = curso.fetchall()
        return render_template('orderproduct.html', oproduct=product, form=form)

    return render_template("mobile.html", mobile=mobile)

@app.route('/home' , methods=['GET', 'POST'])
def home():
    form = OrderForm(request.form)

    cur = mysql.connection.cursor()
    values = 'home'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY pID ASC", (values,))
    home = cur.fetchall()

    if request.method == 'POST' and form.validate():
        try:
            uuid = session['inputid']
        except KeyError:
            error = "You need to Login before ordering. "
            session['error'] = error
            return render_template('error.html')

        ppid = session['proid']
        truename = form.name.data
        howmany = form.quantity.data
        place = session['aaddress']
        mobilen = session['mmobile']
        now = datetime.datetime.now()
        time_needed = datetime.timedelta(days=5)
        arrdate = now + time_needed
        arrdate2 = arrdate.strftime("%y-%m-%d %H:%M:%S")
        special_opition = "none"

        curs = mysql.connection.cursor()
        curs.execute("INSERT INTO orders(uuid, ppid, truename, howmany, place, mobilen, buydate, arrdate, sopition) "
                     "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (uuid, ppid, truename, howmany, place, mobilen, now, arrdate2, special_opition))
        mysql.connection.commit()
        cur.close()

        session.pop('proid')
        success = "Purchase successful"
        session['success'] = success
        return render_template('success.html', oproduct=tshirt, form=form)

    if 'pid' in request.args:
        list = []
        list2 = []
        product_id = request.args['pid']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE pID=%s", (product_id,))
        productID = curso.fetchall()

        for e in productID :
            list.append(e['uploader'])
        uploaderid = list[0]
        curid = mysql.connection.cursor()
        curid.execute("SELECT username FROM users WHERE userID=%s", (uploaderid,))
        username = curid.fetchall()
        for e in username :
            list2.append(e['username'])
        name = list2[0]

        cur.execute("SELECT * FROM products WHERE category=%s AND pID !=%s ORDER BY RAND() LIMIT 2", (values,product_id,))
        similar = cur.fetchall()

        curcom = mysql.connection.cursor()
        curcom.execute("SELECT comments.cid, comments.proid ,comments.userID, comments.ctime,comments.comment,users.username, users.profilepicture FROM comments, users WHERE comments.userID = users.userID AND comments.proid=%s ORDER BY comments.cid DESC ", (product_id,))

        comment = curcom.fetchall()

        return render_template('viewproduct.html', productID=productID, name=name ,similar=similar ,comment=comment )

    elif 'orderpid' in request.args:

        product_id = request.args['orderpid']
        session['proid'] = product_id

        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE pID=%s", (product_id,))
        product = curso.fetchall()
        return render_template('orderproduct.html', oproduct=product, form=form)

    return render_template("home.html", home=home)

@app.route('/uploadproduct', methods=['POST', 'GET'])
def uploadproduct(): # upload product page , get userid to know who are going to upload products , login are needed
    try:
        userid = session['inputid']

        if request.method == 'POST': # input get in the form at html
            name = request.form.get('name')
            price = request.form['price']
            description = request.form['description']
            quantity = request.form['quantity']
            category = request.form['category']
            file = request.files['picture']

            now = datetime.datetime.now()
            now_time = now.strftime("%y-%m-%d %H:%M:%S")

            if name and price and description and quantity and category and file:
                pic = file.filename
                photo = pic.replace("'", "")
                picture = photo.replace(" ", "_")
                if picture.lower().endswith(('.png', '.jpg', '.jpeg')):
                    save_photo = photos.save(file, folder=category)
                    if save_photo:
                        curs = mysql.connection.cursor()
                        curs.execute("INSERT INTO products(pname,pprice,description,quantity,category,plink,date,uploader)"
                                     "VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",
                                     (name, price, description, quantity, category, picture, now_time, userid))
                        mysql.connection.commit()#after checking the detail then insert the new product detail to database

                        flash('Product added successful', 'success')
                        return redirect(url_for('uploadproduct'))
                    else:
                        flash('Picture not save', 'danger')
                        return redirect(url_for('uploadproduct'))
                else:
                    flash('File not supported', 'danger')
                    return redirect(url_for('uploadproduct'))
            else:
                flash('Missing Information', 'danger')
                return redirect(url_for('uploadproduct'))
        else:
            return render_template('uploadproduct.html')

    except KeyError:
        error = "Please Login"
        session['error'] = error
        return render_template("error.html")

@app.route('/uploaded', methods=['GET', 'POST'])
def uploaded(): #show all the uploaded product of the users
    try:
        userid = session['inputid']
        curso = mysql.connection.cursor()
        num_rows = curso.execute("SELECT * FROM products where uploader=%s", (userid,))
        result = curso.fetchall()

        #order_rows = curso.execute("SELECT * FROM orders")
    except KeyError:
        error = "Please Login"
        session['error'] = error
        return render_template("error.html")

    return render_template('uploaded.html', result=result, row=num_rows)

@app.route('/editproduct', methods=['POST', 'GET'])
def editproduct(): #edit all the uploaded product of the users
    if 'pid' in request.args:
        product_id = request.args['pid']
        cured = mysql.connection.cursor()
        cured.execute("SELECT * FROM products WHERE pID=%s", (product_id,))
        product = cured.fetchall()
        if request.method == 'POST':
            print('post')
            name = request.form.get('name')
            price = request.form['price']
            description = request.form['description']
            quantity = request.form['quantity']
            category = request.form['category']
            file = request.files['picture']
#edit with uploading new picture
            if name and price and description and quantity and category and file:
                pic = file.filename
                photo = pic.replace("'", "")
                picture = photo.replace(" ", "_")
                if picture.lower().endswith(('.png', '.jpg', '.jpeg')):
                    save_photo = photos.save(file, folder=category)
                    if save_photo:
                        cured.execute("UPDATE products SET pname=%s, pprice=%s, description=%s, quantity=%s, category=%s, plink=%s WHERE pID=%s ",
                            (name, price, description, quantity, category, pic, product_id,))
                        mysql.connection.commit()

                        flash('Data updated', 'success')
                        return redirect(url_for('uploaded'))

                    else:
                        flash('Pic not upload', 'danger')
                        return render_template('editproduct.html', product=product)
                else:
                    flash('File not support', 'danger')
                    return render_template('editproduct.html', product=product)
            else:
                if name and price and description and quantity and category :#edit without uploading new picture
                    cured.execute(
                        "UPDATE products SET pname=%s, pprice=%s, description=%s, quantity=%s, category=%s WHERE pID=%s ",
                        (name, price, description, quantity, category, product_id,))
                    mysql.connection.commit()

                    flash('Data updated', 'success')
                    return redirect(url_for('uploaded'))

                else:
                    flash('Fill all field2', 'danger')
                    return render_template('editproduct.html', product=product)

        else:
            print('get')
            return render_template('editproduct.html', product=product)
    else:
        return redirect(url_for('uploaded'))

@app.route('/delproduct', methods=['GET', 'POST'])
def delproduct(): #delete product uploaded by the login users
    if 'delpid' in request.args:
        product_id = request.args['delpid']
        curdel = mysql.connection.cursor()
        curdel.execute("SELECT * FROM products WHERE pID=%s", (product_id,))
        product = curdel.fetchall()
        if request.method == 'POST':
            delpw = request.form.get('delpw').encode('utf-8')
            userid = session['inputid']

            user = []
            curpw = mysql.connection.cursor()
            curpw.execute("SELECT userpw FROM users WHERE userID=%s", (userid,))
            user = curpw.fetchone()

            if bcrypt.hashpw(delpw, user['userpw'].encode('utf-8')) == user['userpw'].encode('utf-8'):
                curdel = mysql.connection.cursor()
                curdel.execute("DELETE FROM products where pID=%s", (product_id,))
                mysql.connection.commit()

                success = "Success deleted product"
                session['success'] = success
                return render_template('success.html')

            else:
                error = "Password  Incorrect "
                session['error'] = error
                return redirect(url_for('error'))

        return render_template('delproduct.html', product=product)

    else:
        error = "Product not exist "
        session['error'] = error
        return render_template('error.html')

@app.route("/cart")
def cart():# shopping cart , based on cookie , after log out will lost all data
    pid_in_cart = session.get('cart',[])
    print(pid_in_cart)
    productno = len(pid_in_cart)

    if productno == 0:
        return render_template("cart.html", productno=productno)
    elif productno == 1:
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products where pID=%s", (pid_in_cart[0],))
        result = curso.fetchall()

        return render_template("cart.html", productno=productno, result=result,)
    elif productno == 2:
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products where pID=%s", (pid_in_cart[0],))
        result = curso.fetchall()

        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products where pID=%s", (pid_in_cart[1],))
        result2 = curso.fetchall()

        return render_template("cart.html", productno=productno, result=result, result2=result2)
    elif productno == 3:
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products where pID=%s", (pid_in_cart[0],))
        result = curso.fetchall()

        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products where pID=%s", (pid_in_cart[1],))
        result2 = curso.fetchall()

        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products where pID=%s", (pid_in_cart[2],))
        result3 = curso.fetchall()

        return render_template("cart.html", productno=productno, result=result,
                               result2=result2, result3=result3)
    elif productno == 4:
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products where pID=%s", (pid_in_cart[0],))
        result = curso.fetchall()

        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products where pID=%s", (pid_in_cart[1],))
        result2 = curso.fetchall()

        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products where pID=%s", (pid_in_cart[2],))
        result3 = curso.fetchall()

        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products where pID=%s", (pid_in_cart[3],))
        result4 = curso.fetchall()

        return render_template("cart.html", productno=productno, result=result,
                               result2=result2, result3=result3, result4=result4)
    elif productno == 5:
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products where pID=%s", (pid_in_cart[0],))
        result = curso.fetchall()

        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products where pID=%s", (pid_in_cart[1],))
        result2 = curso.fetchall()

        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products where pID=%s", (pid_in_cart[2],))
        result3 = curso.fetchall()

        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products where pID=%s", (pid_in_cart[3],))
        result4 = curso.fetchall()

        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products where pID=%s", (pid_in_cart[4],))
        result5 = curso.fetchall()

        return render_template("cart.html", productno=productno, result=result,
                               result2=result2, result3=result3, result4=result4, result5=result5)
    elif productno > 5:
        error = "You can only install 5 products to shopping cart "
        session['error'] = error
        return redirect(url_for('error'))

    return render_template("cart.html", productno=productno)


@app.route("/add_to_cart/<int:id>")
def add_to_cart(id): #adding product to shopping cart
    if 'cart' not in session:
        session['cart'] = []

    session['cart'].append(id)
    print(session['cart'])

    flash("Successfully added to cart." , "success")
    return redirect("/cart")

@app.route("/vieworders")
def vieworders(): #user can check their orders
    try:
        userid = session['inputid']
        curso = mysql.connection.cursor()
        num_rows = curso.execute("SELECT * FROM orders where uuid=%s", (userid,))
        result = curso.fetchall()

        # order_rows = curso.execute("SELECT * FROM orders")
    except KeyError:
        error = "Please Login"
        session['error'] = error
        return render_template("error.html")

    return render_template('vieworders.html', result=result, row=num_rows)

@app.route("/admlogin" , methods=['GET', 'POST'])
def adminlogin(): # admin login page
    try :
        if session['adid']:
            return render_template("admmain.html")

    except KeyError :
        if request.method == 'POST':
            ademail = request.form['ademail']
            adpw = request.form['adpw']

            #username and password checking
            user = []
            curads = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            curads.execute("SELECT * FROM admin WHERE ademail=%s", (ademail,))
            user = curads.fetchone()

            userlogin = []
            curadl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            curadl.execute("SELECT * FROM admin WHERE ademail=%s", (ademail,))

            try:
                for q in curadl.fetchone():
                    userlogin.append(q)
            except TypeError :
                userlogin.append("1")
            curadl.close()

            if len(userlogin) > 1 :
                if user['adpw'] == adpw :
                    session['adid'] = user['adid']
                    session['adname'] = user['adname']
                    session['ademail'] = user['ademail']

                    flash('Log In success', 'success')
                    return render_template("admmain.html")
                else:
                    error = "Password  Incorrect "
                    session['error'] = error
                    return redirect(url_for('error'))
            else:
                error = "User not Found "
                session['error'] = error
                return redirect(url_for('error'))
        else:
            return render_template("admlogin.html")

@app.route("/admmain")
def adminmain(): #admin main page
    return render_template("admmain.html")

@app.route("/adalluser", methods=['GET', 'POST'])
def adalluser(): #admin can check all the detail of all the users . A list of all users' details will show up
    try:
        test = session['adid']
        print("Admin ID : ", test ," is checking ALL User.")
        curad = mysql.connection.cursor()
        num_rows = curad.execute("SELECT * FROM users")
        result = curad.fetchall()

    except KeyError:
        error = "Please Login"
        session['error'] = error
        return render_template("error.html")

    return render_template('adalluser.html', result=result, row=num_rows)

@app.route("/adallpro", methods=['GET', 'POST'])
def adallpro():#admin can check all the detail of all the products . A list of all product' details will show up
    try:
        test = session['adid']
        print("Admin ID : ", test ," is checking ALL Product.")
        curad = mysql.connection.cursor()
        num_rows = curad.execute("SELECT * FROM products")
        result = curad.fetchall()

    except KeyError:
        error = "Please Login"
        session['error'] = error
        return render_template("error.html")

    return render_template('adallpro.html', result=result, row=num_rows)

@app.route('/adeditproduct', methods=['POST', 'GET'])
def adeditproduct():#admin can check and update details of each product to avoid any violation products
    if 'adp' in request.args:
        product_id = request.args['adp']
        cured = mysql.connection.cursor()
        cured.execute("SELECT * FROM products WHERE pID=%s", (product_id,))
        product = cured.fetchall()
        if request.method == 'POST':
            print('post')
            name = request.form.get('name')
            price = request.form['price']
            description = request.form['description']
            quantity = request.form['quantity']
            category = request.form['category']

            try:
                file = request.files['picture']
                if name and price and description and quantity and category and file:
                    pic = file.filename
                    photo = pic.replace("'", "")
                    picture = photo.replace(" ", "_")
                    if picture.lower().endswith(('.png', '.jpg', '.jpeg')):
                        save_photo = photos.save(file, folder=category)
                        if save_photo:
                            cured.execute("UPDATE products SET pname=%s, pprice=%s, description=%s, quantity=%s, category=%s, plink=%s WHERE pID=%s ",
                                (name, price, description, quantity, category, pic, product_id,))
                            mysql.connection.commit()

                            flash('Data updated', 'success')
                            return redirect(url_for('adallpro'))

                        else:
                            flash('Pic not upload', 'danger')
                            return render_template('adeditproduct.html', product=product)
                    else:
                        flash('File not support', 'danger')
                        return render_template('adeditproduct.html', product=product)
                else:
                    flash('Fill all field', 'danger')
                    return render_template('adeditproduct.html', product=product)

            except KeyError:
                if name and price and description and quantity and category :
                    cured.execute(
                        "UPDATE products SET pname=%s, pprice=%s, description=%s, quantity=%s, category=%s WHERE pID=%s ",
                        (name, price, description, quantity, category, product_id,))
                    mysql.connection.commit()

                    flash('Data updated', 'success')
                    return redirect(url_for('adallpro'))

                else:
                    flash('Fill all field', 'danger')
                    return render_template('adeditproduct.html', product=product)

        else:
            print('get')
            return render_template('adeditproduct.html', product=product)
    else:
        return redirect(url_for('adallpro'))

@app.route('/addelpro', methods=['GET', 'POST'])
def addelpro():#admin can delete product to avoid any violation products
    if 'addelp' in request.args:
        product_id = request.args['addelp']
        curdel = mysql.connection.cursor()
        curdel.execute("SELECT * FROM products WHERE pID=%s", (product_id,))
        product = curdel.fetchall()
        if request.method == 'POST':
            ok1 = request.form.get('ok1')

            if ok1 == "ok" :
                curdel = mysql.connection.cursor()
                curdel.execute("DELETE FROM products where pID=%s", (product_id,))
                mysql.connection.commit()

                success = "Success deleted product"
                session['success'] = success
                return render_template('success.html')

            else:
                error = "Please re-type 'ok' "
                session['error'] = error
                return redirect(url_for('error'))

        return render_template('addelpro.html', product=product)

    else:
        error = "Error "
        session['error'] = error
        return render_template('error.html')

@app.route("/advieworders")
def advieworders():#admin can check and update details of each orders
    try:
        test = session['adid']
        print("Admin ID : ", test, " is checking ALL Orders.")
        curso = mysql.connection.cursor()
        num_rows = curso.execute("SELECT * FROM orders")
        result = curso.fetchall()

    except KeyError:
        error = "Please Login "
        session['error'] = error
        return render_template("error.html")

    return render_template('advieworders.html', result=result, row=num_rows)

@app.route('/addelo', methods=['GET', 'POST'])
def addelo():#admin can delete orders when misunderstanding or scam are caused
    if 'addelo' in request.args:
        orderID = request.args['addelo']
        curdelo = mysql.connection.cursor()
        curdelo.execute("DELETE FROM orders where orderID=%s", (orderID,))
        mysql.connection.commit()

        success = "Success deleted order"
        session['success'] = success
        return render_template('success.html')

    else:
        error = "Error "
        session['error'] = error
        return render_template('error.html')

@app.route('/search', methods=['POST', 'GET'])
def search(): #search function on the nav-bar , search by products name
    form = OrderForm(request.form)
    if 'search' in request.args:
        find = request.args['search']

        cur = mysql.connection.cursor()

        query_string = "SELECT * FROM products WHERE pname LIKE %s ORDER BY pid ASC"
        cur.execute(query_string, ('%' + find + '%',))
        products = cur.fetchall()

        cur.close()
        flash('Showing result for: ' + find, 'success')
        return render_template('search.html', products=products, form=form)
    else:
        flash('Search again', 'danger')
        return render_template('search.html')

@app.route('/addcomment', methods=['POST'])
def addcomment(): #add comment on each product , login are needed
    try:
        com_userid = session['inputid']
        com_username = ['inputname']
    except KeyError :
        error = "You need to Login before adding comment. "
        session['error'] = error
        return render_template('error.html')

    content = request.form.get('comment_content')
    com_productid = request.form.get('product_id_com')
    com_productcat = request.form.get('product_cat_com')

    if len(content) < 5 : #block any useless comment
        error = "Please enter useful comment "
        session['error'] = error
        return render_template('error.html')

    now = datetime.datetime.now()
    nowtime = now.strftime("%y-%m-%d %H:%M:%S")

    curaddcom = mysql.connection.cursor()
    curaddcom.execute("INSERT INTO comments(proid,userID,ctime,comment)"
                 "VALUES(%s, %s, %s, %s)",
                 (com_productid, com_userid, nowtime, content))
    mysql.connection.commit()

    list = []
    list2 = []
    curso = mysql.connection.cursor()
    curso.execute("SELECT * FROM products WHERE pID=%s", (com_productid,))
    productID = curso.fetchall()

    for e in productID:
        list.append(e['uploader'])
    uploaderid = list[0]
    curid = mysql.connection.cursor()
    curid.execute("SELECT username FROM users WHERE userID=%s", (uploaderid,))
    username = curid.fetchall()
    for e in username:
        list2.append(e['username'])
    name = list2[0]

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products WHERE category=%s AND pID !=%s ORDER BY RAND() LIMIT 2", (com_productcat, com_productid,))
    similar = cur.fetchall()

    curcom = mysql.connection.cursor()
    curcom.execute(
        "SELECT comments.cid, comments.proid ,comments.userID, comments.ctime,comments.comment,users.username, users.profilepicture FROM comments, users WHERE comments.userID = users.userID AND comments.proid=%s ORDER BY comments.cid DESC ",
        (com_productid,))

    comment = curcom.fetchall()

    return render_template('viewproduct.html', productID=productID, name=name, similar=similar, comment=comment)

@app.route('/forgotpw', methods=['POST', 'GET'])
def forgotpw(): # forgot password function , reply new password by email
    if 'email' in request.args:
        email = request.form.get('email')

        userlogin = [] #check that is the email is registed
        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curl.execute("SELECT * FROM users WHERE useremail=%s", (email,))
        try:
            for q in curl.fetchone():
                userlogin.append(q)
        except TypeError:
            userlogin.append("1")
        curl.close()

        if len(userlogin) > 1:
            usernamelist = []
            curnl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            curnl.execute("SELECT * FROM users WHERE useremail=%s", (email,))
            for g in curnl.fetchall():
                usernamelist.append(g['username'])
            username = usernamelist[0]
            
            #Generate a new password

            vercode = []
            letter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            gg = random.randint(1,9) , random.choice(letter)
            vercode.append(random.choice(gg))

            letter2 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            gg2 = random.randint(1,9) , random.choice(letter2)
            vercode.append(random.choice(gg2))

            letter3 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            gg3 = random.randint(1,9) , random.choice(letter3)
            vercode.append(random.choice(gg3))

            letter4 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            gg4 = random.randint(1,9) , random.choice(letter4)
            vercode.append(random.choice(gg4))

            fin = str("".join(str(x) for x in vercode))

            new_pass = fin
            inputpassword = new_pass.encode('utf-8')
            hash_password = bcrypt.hashpw(inputpassword, bcrypt.gensalt())

            now = datetime.datetime.now()
            now_time = now.strftime("%y-%m-%d %H:%M:%S")

            #readly to send Email

            msg = Message('Forgot Password', recipients=[email])

            #body of the email

            msg.body = ('Hello !\nDear user: '+username+',\n'
                'You or someone else has requested to generated a newpassword for your account because of forgot password.\n'
                'If you made this request, then please change the password now:\n'
                '\nNew Password : '+str(new_pass)+'\n'
                '\nFrom OceanShop Admin \n'
                'Time sent : ' +str(now_time)+'')
            try:
                mail.send(msg)
            except Exception:
                error = "Eail sent fail, email are incorrect style"
                session['error'] = error
                return redirect(url_for('error'))

            #update back the new password back to database

            curup = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            curup.execute(
                "UPDATE users SET userpw=%s WHERE useremail=%s ",(hash_password, email,))
            mysql.connection.commit()

            flash("Email Sent","info")
            return render_template('main.html')

        #smtplib.SMTPAuthenticationError will cause on Gmail
        #Google has change their policy , low safety app cannot login

        else:
            error = "User not Found "
            session['error'] = error
            return redirect(url_for('error'))
    else:
        return render_template('forgotpw.html')

@app.route('/changepw', methods=['POST', 'GET'])
def changepw(): # change password function, user can change password by enter a correct old password and a new password
    try:
        cpw_email = session['inputemail']

    except KeyError :
        error = "You need to Login before change password. "
        session['error'] = error
        return render_template('error.html')

    if 'npw' in request.args:
        oldpw = request.form.get('opw').encode('utf-8')
        newpw = request.form.get('npw')

        user = []
        curz = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curz.execute("SELECT * FROM users WHERE useremail=%s", (cpw_email,))
        user = curz.fetchone()

        userlogin = []
        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curl.execute("SELECT * FROM users WHERE useremail=%s", (cpw_email,))
        try:
            for q in curl.fetchone():
                userlogin.append(q)
        except TypeError:
            userlogin.append("1")
        curl.close()

        if len(userlogin) > 1: #check the old password and input old password aren't match
            if bcrypt.hashpw(oldpw, user["userpw"].encode('utf-8')) == user["userpw"].encode('utf-8'):
                new_pass = newpw
                inputpassword = new_pass.encode('utf-8')
                hash_password = bcrypt.hashpw(inputpassword, bcrypt.gensalt())

                curup = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                curup.execute(
                    "UPDATE users SET userpw=%s WHERE useremail=%s ",
                    (hash_password, cpw_email,))
                mysql.connection.commit()

                flash("Password updated","info")
                return redirect(url_for('logout'))

            else:
                error = "Old Password not correct "
                session['error'] = error
                return redirect(url_for('error'))
        else:
            error = "User not Found "
            session['error'] = error
            return redirect(url_for('error'))
    else:
        return render_template('changepw.html')

@app.route('/updatepersonal', methods=['POST', 'GET'])
def updatepersonal(): #user can change their personal info , like email , username, address, mobile number
    try:
        info_email = session['inputemail']

    except KeyError :
        error = "You need to Login before change personal information. "
        session['error'] = error
        return render_template('error.html')

    cured = mysql.connection.cursor()
    cured.execute("SELECT * FROM users WHERE useremail=%s", (info_email,))
    userinfo = cured.fetchall()
    if request.method == 'POST':
        name = request.form.get('username')
        email = request.form.get('useremail')
        mobile = request.form.get('mobile')
        address = request.form.get('address')

        if name and email and mobile and address :
            useremaillist = []
            curs = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            curs.execute("SELECT * FROM users WHERE useremail=%s", (email,))
            try:
                for e in curs.fetchone():
                    useremaillist.append(e)
            except TypeError:
                useremaillist.append("1")
            curs.close()

            usernamelist = []
            curn = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            curn.execute("SELECT * FROM users WHERE username=%s", (name,))
            try:
                for w in curn.fetchone():
                    usernamelist.append(w)
            except TypeError:
                usernamelist.append("2")
            curn.close()

            mobilecheck = []
            try:
                int(mobile)
            except ValueError:
                mobilecheck.append("3")

            if len(useremaillist) == 1:
                if len(usernamelist) == 1:
                    if len(mobilecheck) == 0:
                        cured.execute(
                            "UPDATE users SET username=%s, useremail=%s, usermobile=%s, useraddress=%s WHERE useremail=%s ",
                            (name, email, mobile, address, info_email,))
                        mysql.connection.commit()

                        flash('Sign up successful', 'success')
                        return redirect(url_for('logout'))

                    else:
                        error = "Mobile Number not correct "
                        session['error'] = error
                        return redirect(url_for('error'))
                else:
                    error = "Username has been used "
                    session['error'] = error
                    return redirect(url_for('error'))
            else:
                error = "Email has been used "
                session['error'] = error
                return redirect(url_for('error'))
        else:
            error = "Missing Information "
            session['error'] = error
            return redirect(url_for('error'))

    else:
        return render_template('updatepersonal.html' , userinfo=userinfo)

@app.route('/goal')
def goal(): #some info page
    return render_template('goal.html')

@app.route('/contactus')
def contactus():#some info page
    return render_template('contactus.html')

if __name__ == '__main__':
    app.secret_key = "^A%DJAJU^JJ123"
    app.run(debug=True)
