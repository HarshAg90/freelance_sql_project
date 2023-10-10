from flask import Flask, session, redirect, url_for, jsonify
from flask import render_template,request
import pymysql
from werkzeug.utils import secure_filename
import os
import pathlib
from datetime import datetime 
import json
from PIL import Image

app = Flask(__name__)

UPLOAD_FOLDER = 'static/posts/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = 'any random string'


'''
socailawareness
admin12345678
'''

import firebase_admin
from firebase_admin import credentials, storage

# Initialize Firebase with your credentials JSON file
cred = credentials.Certificate("storage.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'auth-testing-d2b78.appspot.com'
})

# Create a reference to the Firebase Storage bucket
bucket = storage.bucket()

def dbConnection():
    try:
        connection = pymysql.connect(host="socailawareness-sql.cxkbcysa8pim.eu-north-1.rds.amazonaws.com", user="adminn", password="admin12345678", database="socailawareness")
        return connection
    except:
        print("Something went wrong in database Connection")

def dbClose():
    try:
        dbConnection().close()
    except:
        print("Something went wrong in Close DB Connection")

con = dbConnection()
cursor = con.cursor()

@app.route('/')
def index():
    return render_template('sign-in.html')  

@app.route("/test")
def testing():
        return jsonify({"status":"working"}),200
@app.route('/home')
def home():    
    username = session.get("userusername")
    print(username)
    
    
    cursor.execute("SELECT profilepic FROM userdetails WHERE username=%s",(username))
    profilepiclist = cursor.fetchone()
    profilepic = profilepiclist[0]
    
    cursor.execute("SELECT notifyuser.uname,notifyuser.notify,userdetails.uname,userdetails.lname,userdetails.profilepic FROM notifyuser JOIN userdetails ON notifyuser.uname = userdetails.username WHERE notifyuser.uname=%s",(username))
    notificationlst = cursor.fetchall()
    
    cursor.execute("SELECT userdetails.uname,userdetails.lname,userdetails.profilepic,posts.postimage,posts.posttext,posts.id,posts.timestamp,posts.likecount FROM userdetails JOIN posts ON userdetails.username = posts.uploader WHERE posts.uploader = %s",(username))
    userpost = cursor.fetchall()
    userpost = list(userpost)
    
    cursor.execute("SELECT user2 FROM followunfollow WHERE user1=%s",(username))
    l = cursor.fetchall()
    row = [item for sublist in l for item in sublist]
    for i in row:
        cursor.execute("SELECT userdetails.uname,userdetails.lname,userdetails.profilepic,posts.postimage,posts.posttext,posts.id,posts.timestamp,posts.likecount FROM userdetails JOIN posts ON userdetails.username = posts.uploader WHERE posts.uploader = %s",(i))
        data = cursor.fetchall()
        print(data)
        for j in data:
            userpost.append(j)
    userpost11 = sorted(userpost, key=lambda x: x[-2], reverse=True)
    userpost = []
    for user in userpost11:
        print(user)
        cursor.execute("SELECT userdetails.profilepic,userdetails.uname,userdetails.lname,comments.comment,comments.time FROM comments JOIN userdetails ON comments.commenter = userdetails.username WHERE comments.uname = %s AND comments.lname = %s AND comments.idofpost = %s AND comments.timestamp = %s",(user[0],user[1],user[5],user[6]))
        count = cursor.rowcount        
        user = list(user)
        user.append(count)
        userpost.append(user)
    
    cursor.execute("SELECT username FROM userdetails WHERE username!=%s",(username))
    l = cursor.fetchall()
    row = [item for sublist in l for item in sublist]
    # print(row)
    folowing_frnd = []
    for i in row:    
        cursor.execute("SELECT user2 FROM followunfollow WHERE user1=%s AND user2=%s",(username,i))
        rows = cursor.fetchone()
        if rows == None:        
            cursor.execute("SELECT username,uname,lname,profilepic FROM userdetails WHERE username=%s",(i))
            data = cursor.fetchone()
            folowing_frnd.append(data)
            
    cursor.execute("SELECT user2 FROM followunfollow WHERE user1=%s",(username))
    l1 = cursor.fetchall()
    row11 = [item for sublist in l1 for item in sublist]
    # print(row11)
    
    cursor.execute("SELECT username,uname,lname,profilepic FROM userdetails WHERE username!=%s",(username))
    sdfdsf = cursor.fetchall()
    folowed_frnd = []
    for i in sdfdsf:
        if i[0] in row11 and len(row11) != 0:
            folowed_frnd.append(i)
    # print(folowed_frnd)
    
    return render_template('index.html',rows=userpost,folowing_frnd=folowing_frnd,currentuser=username,folowed_frnd=folowed_frnd,profilepic=profilepic,notificationlst=notificationlst) 

@app.route('/profile')
def profile():
    username = session.get("userusername")
    print(username)
    
    cursor.execute("SELECT profilepic,uname,lname FROM userdetails WHERE username=%s",(username))
    profilepiclist = cursor.fetchone()
    profilepic = profilepiclist[0]
    profilename = profilepiclist[1]+" "+profilepiclist[2]
    profileusername = username
    
    cursor.execute("SELECT notifyuser.uname,notifyuser.notify,userdetails.uname,userdetails.lname,userdetails.profilepic FROM notifyuser JOIN userdetails ON notifyuser.uname = userdetails.username WHERE notifyuser.uname=%s",(username))
    notificationlst = cursor.fetchall()
    
    cursor.execute("SELECT email,phone,dob FROM userdetails WHERE username=%s",(username))
    infolist = cursor.fetchone()
    cursor.execute("SELECT address,city,maritalstatus,Qualification,age FROM extrainfo WHERE username=%s",(username))
    row = cursor.fetchone()
    if row == None:
        infolist = list(infolist)+['-','-','-','-','-']
    else:
        infolist = list(infolist)+list(row)
        
    cursor.execute("SELECT user2 FROM followunfollow WHERE user1=%s",(username))
    l1 = cursor.fetchall()
    row11 = [item for sublist in l1 for item in sublist]
    # print(row11)
    
    cursor.execute("SELECT username,uname,lname,profilepic FROM userdetails WHERE username!=%s",(username))
    sdfdsf = cursor.fetchall()
    folowed_frnd = []
    for i in sdfdsf:
        if i[0] in row11 and len(row11) != 0:
            folowed_frnd.append(i)

    folowed_frnd1 = []
    for frnd in folowed_frnd:
        cursor.execute("SELECT COUNT(*) AS row_count FROM posts WHERE uploader = %s",(frnd[0]))
        d = cursor.fetchone()
        frnd = list(frnd)
        frnd.append(d[0])
        folowed_frnd1.append(frnd)
    
    return render_template('friends.html',profilepic=profilepic,notificationlst=notificationlst,profilename=profilename,profileusername=profileusername,infolist=infolist,folowed_frnd=folowed_frnd1)  

@app.route('/SignUp', methods=['GET', 'POST'])
def SignUp():
    if request.method == 'POST':
        details = request.form
        
        username = details['username']
        fname = details['fname']
        lname = details['lname']
        email = details['email']
        mobile = details['mobile']
        dob = details['dob'] 
        password = details['password']
        
        cursor.execute('SELECT * FROM userdetails WHERE username = %s', (username))
        count = cursor.rowcount
        if count > 0:
            return render_template('sign-up.html')  
        else:   
            sql1 = "INSERT INTO userdetails(username,uname,lname,email,password,phone,dob) VALUES (%s, %s, %s, %s, %s, %s, %s);"
            val1 = (username, fname, lname, email, password, mobile, dob)
            cursor.execute(sql1,val1)
            con.commit()        
            return render_template('sign-in.html')
    return render_template('sign-up.html')

@app.route('/SignIn', methods=['GET', 'POST'])
def SignIn():
    if request.method == "POST":
        details = request.form
        
        username = details['username']
        password = details['password']
        # try:
        cursor.execute('SELECT * FROM userdetails WHERE username = %s AND password = %s', (username, password))
        count = cursor.rowcount
        # except:
        # print("an error occured while executing sql code ================")
        # count = 0
        if count == 1:   
            session['userusername'] = username             
            return "success" 
        else:
            return "fail"   
    return render_template('sign-in.html')  

@app.route('/AdminSignIn', methods=['GET', 'POST'])
def AdminSignIn():
    if request.method == "POST":
        details = request.form
        
        username = details['username']
        password = details['password']
        
        if username == 'admin' and password == 'admin':   
            session['adminusername'] = username             
            return "success" 
        else:
            return "fail"   
    return render_template('Admin-sign-in.html')  

@app.route('/home1')
def home1():    
    
    cursor.execute("SELECT userdetails.uname,userdetails.lname,userdetails.profilepic,poststoadmin.postimage,poststoadmin.posttext,poststoadmin.id,poststoadmin.timestamp FROM userdetails JOIN poststoadmin ON userdetails.username = poststoadmin.uploader")
    userpost = cursor.fetchall()
    userpost = list(userpost)
    
    return render_template('index1.html',rows=userpost) 


@app.route('/addPost',methods=['POST','GET'])
def addPost():
    if request.method == "POST":
        
        user = session.get("userusername")
            
        try:
            # posttext = request.form['posttext']
            # f2= request.files['postimage']
            
            # filename_secure = secure_filename(f2.filename)
            
            # pathlib.Path(app.config['UPLOAD_FOLDER'], user).mkdir(exist_ok=True)
            # f2.save(os.path.join(app.config['UPLOAD_FOLDER'],user, filename_secure))
            
            # current_time = datetime.now()  
            # time_stamp = current_time.timestamp() 
            # date_time = datetime.fromtimestamp(time_stamp)s
            # str_date_time = date_time.strftime("%d-%m-%Y %H:%M")
            
            # sql1 = "INSERT INTO poststoadmin(uploader, postimage, posttext, timestamp) VALUES (%s, %s, %s, %s);"
            # val1 = (user, 'static/posts/'+user+'/'+filename_secure, posttext, str_date_time)
            # cursor.execute(sql1,val1)
            # con.commit()                 
            # return redirect(url_for('home'))
            posttext = request.form['posttext']
            f2 = request.files['postimage']
            
            # Generate a unique filename (e.g., using a timestamp)
            import time
            filename = f"{int(time.time())}_{secure_filename(f2.filename)}"
            
            # Create a blob (object) in Firebase Storage
            blob = bucket.blob(filename)

            # Upload the image file to Firebase Storage
            blob.upload_from_string(f2.read(), content_type=f2.content_type)

            blob.make_public()
            # Get the public URL of the uploaded image
            postimage_url = blob.public_url
            print(postimage_url)
            current_time = datetime.now()  
            time_stamp = current_time.timestamp() 
            date_time = datetime.fromtimestamp(time_stamp)
            str_date_time = date_time.strftime("%d-%m-%Y %H:%M")
            
            sql1 = "INSERT INTO poststoadmin(uploader, postimage, posttext, timestamp) VALUES (%s, %s, %s, %s);"
            val1 = (user, postimage_url, posttext, str_date_time)
            cursor.execute(sql1, val1)
            con.commit()
            return redirect(url_for('home'))
        except:            
            print('UPLOAD FAILEDDDDDDDDDDDDD')
            print('UPLOAD FAILEDDDDDDDDDDDDDd')
            posttext = request.form['posttext']
            
            current_time = datetime.now()  
            time_stamp = current_time.timestamp() 
            date_time = datetime.fromtimestamp(time_stamp)
            str_date_time = date_time.strftime("%d-%m-%Y %H:%M")
            
            sql1 = "INSERT INTO poststoadmin(uploader, postimage, posttext, timestamp) VALUES (%s, %s, %s, %s);"
            val1 = (user, "None", posttext, str_date_time)
            cursor.execute(sql1,val1)
            con.commit()                 
            return redirect(url_for('home'))

@app.route('/logout')
def logout():
    return render_template('sign-in.html') 

@app.route('/followuser')
def followuser():
    username = session.get('userusername')
    
    user1 = request.args.get('usrname1')
    user2 = request.args.get('usrname2')
    print(user1,user2)

    cursor.execute("SELECT follow from userdetails where username=%s",(user2))
    res = cursor.fetchone()
    res = list(res)
    fcount = res[0]

    followcount = int(fcount)+1
    sql1 = "UPDATE userdetails SET follow=%s WHERE username=%s"
    val1 = (str(followcount),str(user2))
    cursor.execute(sql1,val1)
    con.commit()

    followcount2 = str(username)+" Started following you!"
    print(followcount2)

    sql2 = "INSERT into notifyuser(uname,notify)VALUES(%s,%s);"
    val2 = (str(user2),str(followcount2))
    cursor.execute(sql2,val2)
    con.commit()

    followcount3 = "1"
    sql3 = "INSERT into followunfollow(user1,user2,follow)VALUES(%s,%s,%s);"
    val3 = (str(user1),str(user2),str(followcount3))
    cursor.execute(sql3,val3)
    con.commit()
    
    return redirect(url_for("home"))

@app.route('/unfollowuser')
def unfollowuser():
    username = session.get('userusername')
    # username = "aniket"
    
    user1 = request.args.get('usrname1')
    user2 = request.args.get('usrname2')
    
    cursor.execute("SELECT follow from userdetails where username=%s",(user2))
    res = cursor.fetchone()
    res = list(res)
    fcount = res[0]

    followcount = int(fcount)-1
    sql1 = "UPDATE userdetails SET follow=%s WHERE username=%s"
    val1 = (str(followcount),str(user2))
    cursor.execute(sql1,val1)
    con.commit()

    unnfollowcount = int(fcount)+1
    sql2 = "UPDATE userdetails SET unfollow=%s WHERE username=%s"
    val2 = (str(unnfollowcount),str(user2))
    cursor.execute(sql2,val2)
    con.commit()

    followcount3 = str(username)+" Started Unfollow you!"
    sql3 = "INSERT into notifyuser(uname,notify)VALUES(%s,%s);"
    val3 = (str(user2),str(followcount3))
    cursor.execute(sql3,val3)
    con.commit()

    sql4 = "DELETE from followunfollow where user1=%s and user2=%s"
    val4 = (str(user1),str(user2))
    cursor.execute(sql4,val4)
    con.commit()
    
    return redirect(url_for("home"))

@app.route('/commentPost', methods=['GET', 'POST'])
def commentPost():
    if request.method == "POST":
        details = request.form
        
        username = session.get('userusername')        
        comment = details['comment']
        uname = details['uname']
        lname = details['lname']
        idofpost = details['idofpost']
        timestamp = details['timestamp']
        
        current_time = datetime.now()  
        time_stamp = current_time.timestamp() 
        date_time = datetime.fromtimestamp(time_stamp)
        str_date_time = date_time.strftime("%d-%m-%Y %H:%M")
        
        sql3 = "INSERT into comments(uname,lname,idofpost,timestamp,comment,commenter,time)VALUES(%s,%s,%s,%s,%s,%s,%s);"
        val3 = (uname,lname,idofpost,timestamp,comment,username,str_date_time)
        cursor.execute(sql3,val3)
        con.commit()
        
        cursor.execute("SELECT username from userdetails where uname=%s AND lname=%s",(uname,lname))
        listofusername = cursor.fetchone()
        user2 = listofusername[0]
        
        followcount3 = str(username)+" commented on your post."
        sql3 = "INSERT into notifyuser(uname,notify)VALUES(%s,%s);"
        val3 = (str(user2),str(followcount3))
        cursor.execute(sql3,val3)
        con.commit()
    
        return redirect(url_for("home"))
    
@app.route('/likepost', methods=['GET', 'POST'])
def likepost():
    if request.method == "POST":
        details = request.form
        
        username = session.get('userusername') 
        idofpost = details['idofpost']
        timestamp = details['timestamp']  
        
        cursor.execute("SELECT likecount FROM posts WHERE id = %s AND timestamp = %s",(idofpost,timestamp))
        rowcount1 = cursor.rowcount
        
        if rowcount1 > 0:
            
            rowdata = cursor.fetchone()             
            likecount = rowdata[0]+1
            
            sql2 = "UPDATE posts SET likecount=%s WHERE id = %s AND timestamp = %s"
            val2 = (likecount,idofpost,timestamp)
            cursor.execute(sql2,val2)
            con.commit()
            
            cursor.execute("SELECT uploader from posts where id=%s",(idofpost))
            listofusername = cursor.fetchone()
            user2 = listofusername[0]
            
            followcount3 = str(username)+" liked on your post."
            sql3 = "INSERT into notifyuser(uname,notify)VALUES(%s,%s);"
            val3 = (str(user2),str(followcount3))
            cursor.execute(sql3,val3)
            con.commit()
        
            return redirect(url_for("home"))
        else:
            return redirect(url_for("home"))
            
    
@app.route('/fetchComments', methods=['GET', 'POST'])
def fetchComments():
    if request.method == "POST":
        details = request.form
        
        uname = details['uname']
        lname = details['lname']  
        idofpost = details['idofpost']
        timestamp = details['timestamp'] 
        
        cursor.execute("SELECT userdetails.profilepic,userdetails.uname,userdetails.lname,comments.comment,comments.time FROM comments JOIN userdetails ON comments.commenter = userdetails.username WHERE comments.uname = %s AND comments.lname = %s AND comments.idofpost = %s AND comments.timestamp = %s",(uname,lname,idofpost,timestamp))
        res = cursor.fetchall()
        
        jsonObj = json.dumps(res) 
        return jsonObj
    
    return redirect(url_for("home")) 

@app.route('/deletePost/<idofpost>')
def deletePost(idofpost):

    sql4 = "DELETE from posts where id=%s"
    val4 = (int(idofpost))
    cursor.execute(sql4,val4)
    con.commit()
    
    return redirect(url_for("home"))

@app.route('/updateProfile', methods=['GET', 'POST'])
def updateProfile():
    if request.method == 'POST':
        details = request.form
        
        username = session.get('userusername') 
        
        f2= request.files['profilepic']
        address = details['address']
        city = details['city']
        maritalstatus = details['maritalstatus']
        qualification = details['qualification']
        age = details['age']         
            
        # filename_secure = secure_filename(f2.filename)
        
        # pathlib.Path(app.config['UPLOAD_FOLDER'], username).mkdir(exist_ok=True)
        # f2.save(os.path.join(app.config['UPLOAD_FOLDER'],username,filename_secure))

        # image = Image.open('static/posts/'+username+'/'+filename_secure)
        
        # sunset_resized = image.resize((853, 853))
        # sunset_resized.save('static/posts/'+username+'/'+filename_secure)
        
        # sql2 = "UPDATE userdetails SET profilepic=%s WHERE username = %s"
        # val2 = ('static/posts/'+username+'/'+filename_secure,username)
        # Generate a unique filename (e.g., using a timestamp)
        import time
        filename = f"{int(time.time())}_{secure_filename(f2.filename)}"

        # Create a blob (object) in Firebase Storage
        blob = bucket.blob(filename)

        # Upload the image file to Firebase Storage
        blob.upload_from_string(f2.read(), content_type=f2.content_type)

        blob.make_public()
        # Get the public URL of the uploaded image
        image_url = blob.public_url
        print(image_url)
        sql2 = "UPDATE userdetails SET profilepic=%s WHERE username = %s"
        val2 = (image_url, username)
        cursor.execute(sql2,val2)
        con.commit()
        
        cursor.execute('SELECT * FROM extrainfo WHERE username = %s', (username))
        count = cursor.rowcount
        if count > 0:
            sql2 = "UPDATE extrainfo SET address=%s,city=%s,maritalstatus=%s,Qualification=%s,age=%s WHERE username = %s"
            val2 = (address, city, maritalstatus, qualification, age, username)
            cursor.execute(sql2,val2)
            con.commit()
            return redirect(url_for("profile"))
        else:   
            sql1 = "INSERT INTO extrainfo(username,address,city,maritalstatus,Qualification,age) VALUES (%s, %s, %s, %s, %s, %s);"
            val1 = (username, address, city, maritalstatus, qualification, age)
            cursor.execute(sql1,val1)
            con.commit()        
            return redirect(url_for("profile"))
    return render_template('sign-up.html')

@app.route('/approvedisapprove', methods=['GET', 'POST'])
def approvedisapprove():
    if request.method == "POST":
        details = request.form
        
        idof = details['id']
        status = details['status']
        
        if status == 'Approve':
            
            cursor.execute('SELECT * FROM poststoadmin WHERE id = %s',(int(idof)))
            data = cursor.fetchone() 
            
            sql1 = "INSERT INTO posts(uploader, postimage, posttext, timestamp) VALUES (%s, %s, %s, %s);"
            val1 = (data[1], data[2], data[3], data[4])
            cursor.execute(sql1,val1)
            con.commit()        
            
            sql4 = "DELETE from poststoadmin where id=%s"
            val4 = (int(idof))
            cursor.execute(sql4,val4)
            con.commit()
            return 'success'
            
        else:
            
            sql4 = "DELETE from poststoadmin where id=%s"
            val4 = (int(idof))
            cursor.execute(sql4,val4)
            con.commit()
            return 'success'
            
    return render_template('Admin-sign-in.html')  
    
def main():
    app.run('0.0.0.0', port=8000)


if __name__ == '__main__':
    # app.run(debug=True)
    # app.run(debug=True, host='0.0.0.0', port=8000)
    main()