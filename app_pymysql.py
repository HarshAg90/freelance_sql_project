#################################################################################################################
#                                       Importing required libraries
#################################################################################################################
from flask import Flask, render_template, request, session, url_for, redirect, jsonify,send_from_directory,flash
import pymysql
import numpy as np
import pandas as pd
import os
from flask import Flask, flash, request, redirect, url_for
from requests import delete
from werkzeug.utils import secure_filename
from flask import Flask, render_template, Response
from datetime import date


#import imutils
UPLOAD_FOLDER = 'static/post_images/'
UPLOAD_FOLDER1 = 'static/spectograms/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'random string'


global postid
postid = []
#################################################################################################################
#                                       DB connection
#################################################################################################################
def dbConnection():
    try:
        connection = pymysql.connect(host="localhost", user="root", password="root", database="socailawareness")
        return connection
    except:
        print("Something went wrong in database Connection")


def dbClose():
    try:
        dbConnection().close()
    except:
        print("Something went wrong in Close DB Connection")

# initialize the video stream and allow the camera sensor to
# warmup
#vs = VideoStream(usePiCamera=1).start()

con=dbConnection()
cursor=con.cursor()
#################################################################################################################
#                                       Index Page
#################################################################################################################
def recommend(id):
    import pandas as pd
    import numpy as np
    conn = dbConnection()
    cur = conn.cursor()
    sql="SELECT uid,pid,likes from recomnd"
    cur.execute(sql)
    table_rows = cur.fetchall()
    df = pd.DataFrame(table_rows,columns=['uid','pid','ratings'])
    print(df)
    print()
    #df.to_csv("Reco.csv")
    print()
    print("printign np.unique(df['pid']")
    print(np.unique(df['pid']))
    a=len(np.unique(df['pid']))

    print()
    print("printing a")
    print(a)
    print()
    df = df.astype({"uid": int,"pid": int,"ratings": int })
    ratings_utility_matrix=df.pivot_table(values='ratings', index='uid', columns='pid', fill_value=0)
    X = ratings_utility_matrix.T

    from sklearn.decomposition import TruncatedSVD
    SVD = TruncatedSVD(n_components=int(2))
    decomposed_matrix = SVD.fit_transform(X)
    correlation_matrix = np.corrcoef(decomposed_matrix)
    i = id
    product_names = list(X.index)
    product_ID = product_names.index(i)
    correlation_product_ID = correlation_matrix[product_ID]
    Recommend = list(X.index[correlation_product_ID > 0.50])
    print("Recommended list")
    print(Recommend)
    Recommend.remove(i) 
    return Recommend[0:5]
#################################################################################################################
#                                       Recommend Page
#################################################################################################################
@app.route('/recomend')
def recomend():
    if 'user' in session:
        usrname = session.get('user')

        conn = dbConnection()
        curs = conn.cursor()

        curs.execute("SELECT postid from recomended_posts where uname=%s;",(usrname))
        res = curs.fetchall()
        psres = list(res)
        print("prinitng res from recomended_posts")
        print(psres)
        curs.execute("DELETE from recomended_posts")

        cap = []
        postimg = []
        post_tag = []
        post_dt = []
        uname = []
        pid = []
        likes = []
        dislike = []
        comentername = []
        usercomnt = []
        comentdate = []

        for i in psres:
            curs.execute("SELECT caption, post_img, tag, post_dt, uname, pid, likes, dislike from userpost where pid=%s",(i[0]))
            res = curs.fetchall()
            result = list(res)

            for i in result:
                a = i[0]
                cap.append(a)

                b = i[1]
                postimg.append(b)
                
                c = i[2]
                post_tag.append(c)

                d = i[3]
                post_dt.append(d)

                e = i[4]
                uname.append(e)

                f = i[5]
                pid.append(f)

                g = i[6]
                likes.append(g)

                h = i[7]
                dislike.append(h)

                curs.execute("SELECT uname, cmnt, pstime from post_comment where pid=%s and posttag=%s",(f,c))
                ress1 = curs.fetchall()
                resultt1 = list(ress1)

                # print()
                # print("prinitng comment fetch data")
                # print(resultt1)
                # print()
                for j in resultt1:
                    k = j[0]
                    comentername.append(k)

                    l = j[1]
                    usercomnt.append(l)
                    
                    m = j[2]
                    comentdate.append(m)
                
        print("printing len of cap")
        print(len(cap))
        pst_lst = zip(cap,postimg,post_tag,post_dt,uname,pid,likes,dislike,comentername,usercomnt,comentdate)
        
        # curs.execute("select uname from userdetails where email != %s",(sesionmail))
        curs.execute("SELECT uname FROM userdetails a WHERE  NOT EXISTS(SELECT uname FROM followunfollow b WHERE  b.user2 = a.uname)and uname!=%s;",(usrname))
        res3 = curs.fetchall()
        result3 = list(res3)
        
        folowing_frnd = []
        for i in result3:
            a = i[0]
            folowing_frnd.append(a)

        curs.execute("SELECT user2 FROM followunfollow a WHERE  user1=%s;",(usrname))
        res4 = curs.fetchall()
        result4 = list(res4)
        
        frndlst = []
        for i in result4:
            a = i[0]
            frndlst.append(a)

        sql6 = "SELECT uname, notify from notifyuser where uname=%s;"
        val6 = (usrname)
        curs.execute(sql6,val6)
        res6 = curs.fetchall()
        reslt6 = list(res6)

        notifylst = []
        uname = []

        for i in reslt6:
            a = i[0]
            uname.append(a)

            b = i[1]
            notifylst.append(b)

        ncount = len(notifylst)

        notiflst = zip(uname,notifylst)

        print()
        print("prinitng pid")
        print(cap,postimg,post_tag,post_dt,uname,pid,likes,dislike,comentername,usercomnt,comentdate)
        print()

        return render_template('recomend.html',pid=pid,ncount=ncount,pst_lst=pst_lst,folowing_frnd=folowing_frnd,frndlst=frndlst,username=usrname,notiflst=notiflst)
    # return render_template('index-2.html')
    return redirect(url_for("login"))

#################################################################################################################
#                                               Index Page
#################################################################################################################
@app.route('/index')
def index():
    if 'user' in session:
        usrname = session.get('user')
        # username = "aniket"
        conn = dbConnection()
        curs = conn.cursor()
        
        curs.execute("SELECT caption, post_img, tag, post_dt, uname, pid, likes, dislike from userpost")
        res = curs.fetchall()
        result = list(res)
        cap = []
        postimg = []
        post_tag = []
        post_dt = []
        uname = []
        pid = []
        likes = []
        dislike = []
        comentername = []
        usercomnt = []
        comentdate = []

        for i in result:
            a = i[0]
            cap.append(a)

            b = i[1]
            postimg.append(b)
            
            c = i[2]
            post_tag.append(c)

            d = i[3]
            post_dt.append(d)

            e = i[4]
            uname.append(e)

            f = i[5]
            pid.append(f)

            g = i[6]
            likes.append(g)

            h = i[7]
            dislike.append(h)

            curs.execute("SELECT uname, cmnt, pstime from post_comment where pid=%s and posttag=%s",(f,c))
            ress1 = curs.fetchall()
            resultt1 = list(ress1)

            if len(resultt1)==0:
                k = "No comment yet!"
                comentername.append(k)

                l = "No comment yet!"
                usercomnt.append(l)
                
                m = "No comment yet!"
                comentdate.append(m)
            else:
                for j in resultt1:
                    k = j[0]
                    comentername.append(k)

                    l = j[1]
                    usercomnt.append(l)
                    
                    m = j[2]
                    comentdate.append(m)
        
        ls1 = zip(pid, uname, post_tag) 
        
        cmnt = []
        for i,j,k in ls1:
            curs.execute("SELECT cmnt from post_comment where pid=%s and uname=%s and posttag=%s",(i,j,k))
            res2 = curs.fetchall()
            result2 = list(res2)    
            for l in result2:
                a = l[0]
                cmnt.append(a)
        pst_lst = zip(cap,postimg,post_tag,post_dt,uname,pid,likes,dislike,comentername,usercomnt,comentdate)
        
        # curs.execute("select uname from userdetails where email != %s",(sesionmail))
        curs.execute("SELECT uname FROM userdetails a WHERE  NOT EXISTS(SELECT uname FROM followunfollow b WHERE  b.user2 = a.uname)and uname!=%s;",(usrname))
        res3 = curs.fetchall()
        result3 = list(res3)
        
        folowing_frnd = []
        for i in result3:
            a = i[0]
            folowing_frnd.append(a)

        curs.execute("SELECT user2 FROM followunfollow a WHERE  user1=%s;",(usrname))
        res4 = curs.fetchall()
        result4 = list(res4)
        
        frndlst = []
        for i in result4:
            a = i[0]
            frndlst.append(a)

        sql6 = "SELECT uname, notify from notifyuser where uname=%s;"
        val6 = (usrname)
        curs.execute(sql6,val6)
        res6 = curs.fetchall()
        reslt6 = list(res6)

        notifylst = []
        uname = []

        for i in reslt6:
            a = i[0]
            uname.append(a)

            b = i[1]
            notifylst.append(b)

        ncount = len(notifylst)

        notiflst = zip(uname,notifylst)

        print()
        print("prinitng pid")
        print(cap,postimg,post_tag,post_dt,uname,pid,likes,dislike,comentername,usercomnt,comentdate,cmnt)
        print()
        return render_template('index-2.html',pid=pid,ncount=ncount,pst_lst=pst_lst,folowing_frnd=folowing_frnd,frndlst=frndlst,username=usrname,notiflst=notiflst)
    # return render_template('index-2.html')
    return redirect(url_for("login"))
#################################################################################################################
#                                       Store Posted Image and Text
#################################################################################################################
@app.route('/posting', methods=["GET","POST"])
def posting():
    if 'user' in session:
        if request.method=="POST":
            userpost = request.form.get('userpost')
            img = request.files['file1']
            pst_tag = request.form.get('pst_tag')
            # uname = session.get('user')
            # uname = "aniket"
            uname = session.get('user')
            tod_dt = date.today()

            print(userpost,img)

            if len(userpost)==0:
                userpost = "Na"
                filename_secure = secure_filename(img.filename)
                img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename_secure))
                print("print saved")
                filename1 = filename_secure
                print("printig filename1")
                print(filename1)

                conn = dbConnection()
                curs = conn.cursor()
                sql = "INSERT into userpost (uname, caption, post_img, tag, post_dt) values(%s,%s,%s,%s,%s)"
                val = (uname, userpost, filename_secure, pst_tag, str(tod_dt))
                curs.execute(sql,val)
                conn.commit()
            elif not img:
                img = "Na"
                conn = dbConnection()
                curs = conn.cursor()
                sql = "INSERT into userpost (uname, caption, post_img, tag, post_dt) values(%s,%s,%s,%s,%s)"
                val = (uname, userpost, img, pst_tag, str(tod_dt))
                curs.execute(sql,val)
                conn.commit()
            else:
                filename_secure = secure_filename(img.filename)
                img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename_secure))
                print("print saved")
                filename1 = filename_secure
                print("printig filename1")
                print(filename1)

                conn = dbConnection()
                curs = conn.cursor()
                sql = "INSERT into userpost (uname, caption, post_img, tag, post_dt) values(%s,%s,%s,%s,%s)"
                val = (uname, userpost, filename_secure, pst_tag, str(tod_dt))
                curs.execute(sql,val)
                conn.commit()

        return redirect(url_for("index"))
    return redirect(url_for("login"))
#################################################################################################################
#                                       About Page
#################################################################################################################
@app.route('/about')
def aboutme():
    if 'user' in session:
        usrname = session.get('user')
        usrmail = session.get('umail')

        conn = dbConnection()
        curs = conn.cursor()

        curs.execute("SELECT uname FROM userdetails a WHERE  NOT EXISTS(SELECT uname FROM followunfollow b WHERE  b.user2 = a.uname)and uname!=%s;",(usrname))
        res3 = curs.fetchall()
        result3 = list(res3)
        
        folowing_frnd = []
        for i in result3:
            a = i[0]
            folowing_frnd.append(a)

        curs.execute("SELECT user2 FROM followunfollow a WHERE  user1=%s;",(usrname))
        res4 = curs.fetchall()
        result4 = list(res4)
        
        frndlst = []
        for i in result4:
            a = i[0]
            frndlst.append(a)

        curs.execute("SELECT * from basicinfo1 where uname=%s and email=%s ;",(usrname,usrmail))
        result = curs.fetchall()
        fresult = list(result)
        
        uname = []
        lname = []
        email = []
        phone = []
        dob = []
        gender = []
        city = []
        state = []
        aboutme = []
        studyat = []
        studyfrom = []
        studyto = []

        for i in fresult:
            a=i[1]
            uname.append(a)

            b=i[2]
            lname.append(b)

            c=i[3]
            email.append(c)

            d=i[4]
            phone.append(d)

            e=i[5]
            dob.append(e)

            f=i[6]
            gender.append(f)

            g=i[7]
            city.append(g)

            h=i[8]
            state.append(h)

            j=i[9]
            aboutme.append(j)

            k=i[10]
            studyat.append(k)

            l=i[11]
            studyfrom.append(l)

            m=i[12]
            studyto.append(m)

        curs.execute("SELECT field_interest from userdetails where uname=%s and email=%s ;",(usrname,usrmail))
        result2 = curs.fetchall()
        fresult2 = list(result2)

        fofinterest = []

        for i in fresult2:
            a = i[0]
            fofinterest.append(a)

        flst = zip(uname,lname,email,phone,dob,gender,city,state,aboutme,studyat,studyfrom,studyto,fofinterest)

        curs.execute("SELECT verifytag from basicinfo1 where uname=%s",(uname))
        result = curs.fetchall()


        return render_template('aboutme.html',result=result,folowing_frnd=folowing_frnd,frndlst=frndlst,flst=flst)
    return redirect(url_for("login"))
    
#################################################################################################################
#                                       Contact Page
#################################################################################################################
@app.route('/contact')
def contact():
    if 'user' in session:
        return render_template('contact.html')
    return redirect(url_for("login"))

@app.route('/SignUp')
def SignUp():
    return render_template('sign-up.html')
#################################################################################################################
#                                       Timeline Page
#################################################################################################################
@app.route('/timeline')
def timeline():
    if 'user' in session:
        username = session.get('user')
        # username = "aniket"
        conn = dbConnection()
        curs = conn.cursor()
        curs.execute("SELECT caption, post_img, tag, post_dt, uname, pid, likes, dislike from userpost where uname=%s",(username))
        res = curs.fetchall()
        result = list(res)
        cap = []
        postimg = []
        post_tag = []
        post_dt = []
        uname = []
        pid = []
        likes = []
        dislike = []

        for i in result:
            a = i[0]
            cap.append(a)

            b = i[1]
            postimg.append(b)
            
            c = i[2]
            post_tag.append(c)

            d = i[3]
            post_dt.append(d)

            e = i[4]
            uname.append(e)

            f = i[5]
            pid.append(f)

            g = i[6]
            likes.append(g)

            h = i[7]
            dislike.append(h)
        
        ls1 = zip(pid, uname, post_tag)
        cmnt = []
        for i,j,k in ls1:
            curs.execute("SELECT cmnt from post_comment where pid=%s and uname=%s and posttag=%s",(i,j,k))
            res2 = curs.fetchall()
            result2 = list(res2)    
            for l in result2:
                a = l[0]
                cmnt.append(a)
            

        pst_lst = zip(cap,postimg,post_tag,post_dt,uname,pid,likes,dislike)

        curs.execute("SELECT user2 from followunfollow where user2=%s",(username))
        res3 = curs.fetchall()
        ress3 = list(res3)

        folowusers = []
        for i in ress3:
            a = i[0]
            folowusers.append(a)

        followcount = len(folowusers)

        sql6 = "SELECT uname, notify from notifyuser where uname=%s;"
        val6 = (username)
        curs.execute(sql6,val6)
        res6 = curs.fetchall()
        reslt6 = list(res6)

        notifylst = []
        uname = []

        for i in reslt6:
            a = i[0]
            uname.append(a)

            b = i[1]
            notifylst.append(b)

        ncount = len(notifylst)

        notiflst = zip(uname,notifylst)

        curs.execute("SELECT uname FROM userdetails a WHERE  NOT EXISTS(SELECT uname FROM followunfollow b WHERE  b.user2 = a.uname)and uname!=%s;",(username))
        res3 = curs.fetchall()
        result3 = list(res3)
        
        folowing_frnd = []
        for i in result3:
            a = i[0]
            folowing_frnd.append(a)

        curs.execute("SELECT user2 FROM followunfollow a WHERE  user1=%s;",(username))
        res4 = curs.fetchall()
        result4 = list(res4)
        
        frndlst = []
        for i in result4:
            a = i[0]
            frndlst.append(a)

        curs.execute("SELECT verifytag from basicinfo1 where uname=%s",(username))
        result = curs.fetchall()


        return render_template('time-line.html',ncount=ncount,notiflst=notiflst,pst_lst=pst_lst,username=username,
        followcount=followcount,folowing_frnd=folowing_frnd,frndlst=frndlst,result=result)
    return redirect(url_for("login"))

@app.route('/timelinefr')
def timelinefr():
    if 'user' in session:
        username = session.get('user')

        conn = dbConnection()
        curs = conn.cursor()

        curs.execute("SELECT user2 from followunfollow where user1=%s",(username))
        res3 = curs.fetchall()
        ress3 = list(res3)

        folowusers = []
        for i in ress3:
            a = i[0]
            folowusers.append(a)

        followcount = len(folowusers)

        sql6 = "SELECT uname, notify from notifyuser where uname=%s;"
        val6 = (username)
        curs.execute(sql6,val6)
        res6 = curs.fetchall()
        reslt6 = list(res6)

        notifylst = []
        uname = []

        for i in reslt6:
            a = i[0]
            uname.append(a)

            b = i[1]
            notifylst.append(b)

        ncount = len(notifylst)

        notiflst = zip(uname,notifylst)

        curs.execute("SELECT uname FROM userdetails a WHERE  NOT EXISTS(SELECT uname FROM followunfollow b WHERE  b.user2 = a.uname)and uname!=%s;",(username))
        res3 = curs.fetchall()
        result3 = list(res3)
        
        folowing_frnd = []
        for i in result3:
            a = i[0]
            folowing_frnd.append(a)

        curs.execute("SELECT user2 FROM followunfollow a WHERE  user1=%s;",(username))
        res4 = curs.fetchall()
        result4 = list(res4)
        
        frndlst = []
        for i in result4:
            a = i[0]
            frndlst.append(a)

        curs.execute("SELECT verifytag from basicinfo1 where uname=%s",(username))
        result = curs.fetchall()


        return render_template('timeline-friends.html',ncount=ncount,notiflst=notiflst,folowusers=folowusers
        ,username=username,followcount=followcount,folowing_frnd=folowing_frnd,frndlst=frndlst,result=result)
    return redirect(url_for("login"))    
    
@app.route('/timelinepic', methods=["GET","POST"])
def timelinepic():
    if 'user' in session:
        username = session.get('user')
        conn = dbConnection()
        curs = conn.cursor()

        curs.execute("SELECT certifyImg from certificate where uname=%s",(username))
        res = curs.fetchall()
        conn.commit()

        result = list(res)
        certifyimgs = []
        for i in result:
            a = i[0]
            certifyimgs.append(a)
        print("prinitng certifyimgs")
        print(certifyimgs)

        sql6 = "SELECT uname, notify from notifyuser where uname=%s;"
        val6 = (username)
        curs.execute(sql6,val6)
        res6 = curs.fetchall()
        reslt6 = list(res6)

        notifylst = []
        uname = []

        for i in reslt6:
            a = i[0]
            uname.append(a)

            b = i[1]
            notifylst.append(b)

        ncount = len(notifylst)

        notiflst = zip(uname,notifylst)

        curs.execute("SELECT uname FROM userdetails a WHERE  NOT EXISTS(SELECT uname FROM followunfollow b WHERE  b.user2 = a.uname)and uname!=%s;",(username))
        res3 = curs.fetchall()
        result3 = list(res3)
        
        folowing_frnd = []
        for i in result3:
            a = i[0]
            folowing_frnd.append(a)

        curs.execute("SELECT user2 FROM followunfollow a WHERE  user1=%s;",(username))
        res4 = curs.fetchall()
        result4 = list(res4)
        
        frndlst = []
        for i in result4:
            a = i[0]
            frndlst.append(a)   

        curs.execute("SELECT verifytag from basicinfo1 where uname=%s",(username))
        result = curs.fetchall()    
        

        if request.method=="POST":
            certificate = request.files['certify']

            filename_secure = secure_filename(certificate.filename)
            certificate.save(os.path.join(app.config['UPLOAD_FOLDER'], filename_secure))
            print("print saved")
            filename1 = filename_secure
            print("printig filename1")
            print(filename1)

            
            sql = "INSERT into certificate(uname,certifyImg) VALUES (%s,%s)"
            val = (username,filename1)
            curs.execute(sql,val)
            conn.commit()

            return render_template('timeline-photos.html',ncount=ncount,notiflst=notiflst,username=username
            ,folowing_frnd=folowing_frnd,frndlst=frndlst,certifyimgs=certifyimgs,result=result)
        return render_template('timeline-photos.html',ncount=ncount,notiflst=notiflst,username=username,
        folowing_frnd=folowing_frnd,frndlst=frndlst,certifyimgs=certifyimgs,result=result)
    return redirect(url_for("login"))
#################################################################################################################
#                                       Check profile
#################################################################################################################
@app.route('/checkprofile')
def checkprofile():
    if 'user' in session:
        username = session.get('user')
        # username = "aniket"
        usrnm = request.args.get('usrnm')
        conn = dbConnection()
        curs = conn.cursor()
        curs.execute("SELECT caption, post_img, tag, post_dt, uname, pid, likes, dislike from userpost where uname=%s",(usrnm))
        res = curs.fetchall()
        result = list(res)
        cap = []
        postimg = []
        post_tag = []
        post_dt = []
        uname = []
        pid = []
        likes = []
        dislike = []

        for i in result:
            a = i[0]
            cap.append(a)

            b = i[1]
            postimg.append(b)
            
            c = i[2]
            post_tag.append(c)

            d = i[3]
            post_dt.append(d)

            e = i[4]
            uname.append(e)

            f = i[5]
            pid.append(f)

            g = i[6]
            likes.append(g)

            h = i[7]
            dislike.append(h)
        
        ls1 = zip(pid, uname, post_tag)
        cmnt = []
        for i,j,k in ls1:
            curs.execute("SELECT cmnt from post_comment where pid=%s and uname=%s and posttag=%s",(i,j,k))
            res2 = curs.fetchall()
            result2 = list(res2)    
            for l in result2:
                a = l[0]
                cmnt.append(a)

        sql6 = "SELECT uname, notify from notifyuser where uname=%s;"
        val6 = (username)
        curs.execute(sql6,val6)
        res6 = curs.fetchall()
        reslt6 = list(res6)

        notifylst = []
        uname = []

        for i in reslt6:
            a = i[0]
            uname.append(a)

            b = i[1]
            notifylst.append(b)

        ncount = len(notifylst)

        notiflst = zip(uname,notifylst)
            

        pst_lst = zip(cap,postimg,post_tag,post_dt,uname,pid,likes,dislike)

        curs.execute("SELECT uname FROM userdetails a WHERE  NOT EXISTS(SELECT uname FROM followunfollow b WHERE  b.user2 = a.uname)and uname!=%s;",(username))
        res3 = curs.fetchall()
        result3 = list(res3)
        
        folowing_frnd = []
        for i in result3:
            a = i[0]
            folowing_frnd.append(a)

        curs.execute("SELECT user2 FROM followunfollow a WHERE  user1=%s;",(username))
        res4 = curs.fetchall()
        result4 = list(res4)
        
        frndlst = []
        for i in result4:
            a = i[0]
            frndlst.append(a)
        
        curs.execute("SELECT verifytag from basicinfo1 where uname=%s",(usrnm))
        result = curs.fetchall()


        return render_template('time-line.html',ncount=ncount,notiflst=notiflst,pst_lst=pst_lst,
        folowing_frnd=folowing_frnd,frndlst=frndlst,username=usrnm,result=result)
    return redirect(url_for("login"))
#################################################################################################################
#                                       Check profile
#################################################################################################################
@app.route('/searchprofile')
def searchprofile():
    if 'user' in session:

        username = session.get('user')
        # username = "aniket"
        usrnm = request.form.get('usrnm')
        conn = dbConnection()
        curs = conn.cursor()
        curs.execute("SELECT caption, post_img, tag, post_dt, uname, pid, likes, dislike from userpost where uname=%s",(username))
        res = curs.fetchall()
        result = list(res)
        cap = []
        postimg = []
        post_tag = []
        post_dt = []
        uname = []
        pid = []
        likes = []
        dislike = []

        for i in result:
            a = i[0]
            cap.append(a)

            b = i[1]
            postimg.append(b)
            
            c = i[2]
            post_tag.append(c)

            d = i[3]
            post_dt.append(d)

            e = i[4]
            uname.append(e)

            f = i[5]
            pid.append(f)

            g = i[6]
            likes.append(g)

            h = i[7]
            dislike.append(h)
        
        ls1 = zip(pid, uname, post_tag)
        cmnt = []
        for i,j,k in ls1:
            curs.execute("SELECT cmnt from post_comment where pid=%s and uname=%s and posttag=%s",(i,j,k))
            res2 = curs.fetchall()
            result2 = list(res2)    
            for l in result2:
                a = l[0]
                cmnt.append(a)

        sql6 = "SELECT uname, notify from notifyuser where uname=%s;"
        val6 = (username)
        curs.execute(sql6,val6)
        res6 = curs.fetchall()
        reslt6 = list(res6)

        notifylst = []
        uname = []

        for i in reslt6:
            a = i[0]
            uname.append(a)

            b = i[1]
            notifylst.append(b)

        ncount = len(notifylst)

        notiflst = zip(uname,notifylst)
            

        pst_lst = zip(cap,postimg,post_tag,post_dt,uname,pid,likes,dislike)

        return render_template('time-line.html',ncount=ncount,notiflst=notiflst,pst_lst=pst_lst,username=usrnm)
    return redirect(url_for("login"))
#################################################################################################################
#                                       Follow user
#                                 user1 following user2
#################################################################################################################
@app.route('/followuser')
def followuser():
    if 'user' in session:
        username = session.get('user')
        # username = "aniket"
        
        user1 = request.args.get('usrname1')
        user2 = request.args.get('usrname2')
        print(user1,user2)
        print()

        conn = dbConnection()
        curs = conn.cursor()
        curs.execute("SELECT follow from userdetails where uname=%s",(user2))
        res = curs.fetchone()
        res = list(res)
        fcount = res[0]
        # print()
        # print("res")
        # print(fcount)
        print("Query 1 submitted")

        followcount = int(fcount)+1
        sql1 = "UPDATE userdetails SET follow=%s WHERE uname=%s"
        val1 = (str(followcount),str(user2))
        curs.execute(sql1,val1)
        print("query 2 submited")

        followcount2 = str(username)+" Started following you!"
        print(followcount2)

        sql2 = "INSERT into notifyuser(uname,notify)VALUES(%s,%s);"
        val2 = (str(user2),str(followcount2))
        curs.execute(sql2,val2)

        followcount3 = "1"
        sql3 = "INSERT into followunfollow(user1,user2,follow)VALUES(%s,%s,%s);"
        val3 = (str(user1),str(user2),str(followcount3))
        curs.execute(sql3,val3)
        print("Query 3 submited")

        conn.commit()
        print("Data commited")
        return redirect(url_for("index"))
    return redirect(url_for("login"))

#################################################################################################################
#                                       Follow user
#                                 user1 unfollowing user2
#################################################################################################################
@app.route('/unfollowuser')
def unfollowuser():
    if 'user' in session:
        username = session.get('user')
        # username = "aniket"
        
        user1 = request.args.get('usrname1')
        user2 = request.args.get('usrname2')
        print(user1,user2)
        print()

        conn = dbConnection()
        curs = conn.cursor()
        curs.execute("SELECT follow from userdetails where uname=%s",(user2))
        res = curs.fetchone()
        res = list(res)
        fcount = res[0]
        # print()
        # print("res")
        # print(fcount)
        print("Query 1 submitted")

        followcount = int(fcount)-1
        sql1 = "UPDATE userdetails SET follow=%s WHERE uname=%s"
        val1 = (str(followcount),str(user2))
        curs.execute(sql1,val1)
        print("query 2 submited")

        unnfollowcount = int(fcount)+1
        sql2 = "UPDATE userdetails SET unfollow=%s WHERE uname=%s"
        val2 = (str(unnfollowcount),str(user2))
        curs.execute(sql2,val2)
        print("query 2 submited")

        followcount3 = str(username)+" Started Unfollow you!"
        print(followcount3)
        sql3 = "INSERT into notifyuser(uname,notify)VALUES(%s,%s);"
        val3 = (str(user2),str(followcount3))
        curs.execute(sql3,val3)

        sql4 = "DELETE from followunfollow where user1=%s and user2=%s"
        val4 = (str(user1),str(user2))
        curs.execute(sql4,val4)
        print("Query 3 submited")

        conn.commit()
        print("Data commited")
        return redirect(url_for("index"))
    return redirect(url_for("login"))

#################################################################################################################
#                                       Comment on Post
#################################################################################################################
@app.route('/coment', methods=["GET","POST"])
def coment():
    if 'user' in session:
        cmnt = request.form.get('cmnt')
        psid = request.form.get('pid')
        usrname = request.form.get('uname')
        pstags = request.form.get('posttag')
        tod_dt = date.today()

        print(psid, usrname, pstags, cmnt)

        conn = dbConnection()
        curs = conn.cursor()
        sql = "INSERT into post_comment(pid, uname, posttag, cmnt, pstime) VALUES(%s,%s,%s,%s,%s);"
        val = (psid, usrname, pstags, cmnt, tod_dt)
        curs.execute(sql,val)
        conn.commit()
        
        return redirect(url_for('index'))  
    return redirect(url_for("login"))
#################################################################################################################
#                                       Notification function
#################################################################################################################
@app.route('/notify', methods=["GET","POST"])
def notify():
    if 'user' in session:
        uname = session.get('user')

        conn = dbConnection()
        curs = conn.cursor()
        sql = "SELECT notify form notifyuser where uname=%s"
        val = (uname)
        curs.execute(sql,val)
        res = curs.fetchall()
        reslt = list(res)

        notifylst = []
        for i in reslt:
            a = i[0]
            notifylst.append(a)
        
        return redirect(url_for('index'))  
    return redirect(url_for("login"))
#################################################################################################################
#                                      about info
#################################################################################################################
@app.route('/editprof', methods=["GET","POST"])
def editprof():
    if 'user' in session:
        uname = session.get('user')
        umail = session.get('umail')

        conn = dbConnection()
        curs = conn.cursor()
        sql = "SELECT * from basicinfo1 where uname=%s and email=%s;"
        val = (uname,umail)
        countres = curs.execute(sql,val)
        res = curs.fetchall()
        res = list(res)

        unam = []
        lname = []
        email = []
        phone = []
        dob = []
        city = []
        state = []

        for i in res:
            a = i[1]
            unam.append(a)

            b = i[2]
            lname.append(b)

            c = i[3]
            email.append(c)

            d = i[4]
            phone.append(d)

            e = i[5]
            dob.append(e)

            g = i[7]
            city.append(g)

            h = i[8]
            state.append(h)

        flst = zip(unam,lname,email,phone,dob,city,state)

        sql6 = "SELECT uname, notify from notifyuser where uname=%s;"
        val6 = (uname)
        curs.execute(sql6,val6)
        res6 = curs.fetchall()
        reslt6 = list(res6)

        notifylst = []
        uname = []

        for i in reslt6:
            a = i[0]
            uname.append(a)

            b = i[1]
            notifylst.append(b)

        ncount = len(notifylst)

        notiflst = zip(uname,notifylst)

        uname = session.get('user')
        curs.execute("SELECT uname FROM userdetails a WHERE  NOT EXISTS(SELECT uname FROM followunfollow b WHERE  b.user2 = a.uname)and uname!=%s;",(uname))
        res3 = curs.fetchall()
        result3 = list(res3)
        
        folowing_frnd = []
        for i in result3:
            a = i[0]
            folowing_frnd.append(a)

        curs.execute("SELECT user2 FROM followunfollow a WHERE  user1=%s;",(uname))
        res4 = curs.fetchall()
        result4 = list(res4)
        
        frndlst = []
        for i in result4:
            a = i[0]
            frndlst.append(a)
        
        folocount = len(frndlst)
        uname = session.get('user')
        curs.execute("SELECT verifytag from basicinfo1 where uname=%s",(uname))
        result = curs.fetchall()    

        if request.method=="POST":
            username = request.form.get('usrname')
            userlname = request.form.get('usrlname')
            useremail = request.form.get('email')
            userphone = request.form.get('phone')
            userdob = request.form.get('dob')
            usergender = request.form.get('gender')
            usercity = request.form.get('city')
            userstate = request.form.get('state')
            useraboutme = request.form.get('aboutme')
            userstudyat = request.form.get('studyat')
            userfrom = request.form.get('from')
            userto = request.form.get('to')
            uname = session.get('user')


            if countres>0:
                curs.execute("update basicinfo1 set uname=%s,lname=%s,email=%s,phone=%s,dob=%s,gender=%s,city=%s,state=%s,aboutme=%s,studyat=%s,studyfrom=%s,studyto=%s where uname=%s and email=%s;",
                username,userlname,useremail,userphone,userdob,usergender,usercity,userstate,useraboutme,userstudyat,userfrom,userto,uname,umail)
            else:
                sql2 = "INSERT into basicinfo1(uname,lname,email,phone,dob,gender,city,state,aboutme,studyat,studyfrom,studyto) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                val2 = (username,userlname,useremail,userphone,userdob,usergender,usercity,userstate,useraboutme,userstudyat,userfrom,userto)
                curs.execute(sql2,val2)
                conn.commit()

            return render_template("edit-profile-basic.html",result=result,folocount=folocount,folowing_frnd=folowing_frnd,frndlst=frndlst,ncount=ncount,notiflst=notiflst,uname=uname)
        return render_template("edit-profile-basic.html",result=result,folocount=folocount,folowing_frnd=folowing_frnd,frndlst=frndlst,ncount=ncount,notiflst=notiflst,uname=uname)
    return redirect(url_for("login"))

@app.route('/editint', methods=["GET","POST"])
def editint():
    if 'user' in session:
        uname = session.get('user')
        usermail = session.get('umail')

        conn = dbConnection()
        curs = conn.cursor()
        curs.execute("SELECT aboutme from basicinfo1 where email=%s and uname=%s",(uname,usermail))
        res = curs.fetchall()
        res = list(res)

        abtme = []
        for i in res:
            a = i[0]
            abtme.append(a)


        sql6 = "SELECT uname, notify from notifyuser where uname=%s;"
        val6 = (uname)
        curs.execute(sql6,val6)
        res6 = curs.fetchall()
        reslt6 = list(res6)

        notifylst = []
        uname = []

        for i in reslt6:
            a = i[0]
            uname.append(a)

            b = i[1]
            notifylst.append(b)

        ncount = len(notifylst)

        notiflst = zip(uname,notifylst)

        uname = session.get('user')
        curs.execute("SELECT uname FROM userdetails a WHERE  NOT EXISTS(SELECT uname FROM followunfollow b WHERE  b.user2 = a.uname)and uname!=%s;",(uname))
        res3 = curs.fetchall()
        result3 = list(res3)
        
        folowing_frnd = []
        for i in result3:
            a = i[0]
            folowing_frnd.append(a)

        curs.execute("SELECT user2 FROM followunfollow a WHERE  user1=%s;",(uname))
        res4 = curs.fetchall()
        result4 = list(res4)
        
        frndlst = []
        for i in result4:
            a = i[0]
            frndlst.append(a)
        
        folocount = len(frndlst)

        curs.execute("SELECT verifytag from basicinfo1 where uname=%s",(uname))
        result = curs.fetchall()  

        if request.method=="POST":
            foint = request.form.getlist('foint')
            
            curs.execute("update userdetails set field_interest=%s where uname=%s and email=%s",(foint,uname,usermail))

            return render_template("edit-interest.html",result=result,folocount=folocount,frndlst=frndlst,folowing_frnd=folowing_frnd,ncount=ncount,notiflst=notiflst,uname=uname,abtme=abtme)
        return render_template("edit-interest.html",result=result,folocount=folocount,frndlst=frndlst,folowing_frnd=folowing_frnd,ncount=ncount,notiflst=notiflst,uname=uname,abtme=abtme)
    return redirect(url_for("login"))
#################################################################################################################
#                                       Giving Likes to post
#################################################################################################################
import json
@app.route('/likes', methods=["GET","POST"])
def likes():
    if 'user' in session:
        print("Session")
        if request.method=="POST":
            global postid
            print("POST")
            conn = dbConnection()
            curs = conn.cursor()
            # heartinp = request.form['javascript_data']
            name = request.form.get('name').split("|")

            lik = name[0]
            psid = name[1]
            usrname = name[2]
            pstags = name[3]

            usession_name = session.get('user')
            rec_lst = recommend(int(psid))
            for i in rec_lst:
                sql = "INSERT into recomended_posts (uname,postid) VALUES(%s,%s);"
                val = (usession_name,i)
                curs.execute(sql,val)
                conn.commit()

            
            # print("printing likes data")
            # print(name)
            # print()
            # print(lik,psid,usrname,pstags)


            sql = "SELECT likes from userpost where pid=%s and uname=%s and tag=%s;"
            val = (psid, usrname, pstags)
            curs.execute(sql,val)
            res = curs.fetchone()
            result = list(res)
            # print(result)
            # print()
            # print("length of result is: ",len(result))

            like_count = []
            for i in result:
                if i == None:
                    # print("yes none is in i")
                    a = 0
                    like_count.append(a)         
                else:
                    # print(" none not present in i")
                    a = int(i[0])
                    like_count.append(a)
            
            final_count = int(lik)+like_count[0]   
            print()
            print("prinitng final count: ",final_count)
            curs.execute("UPDATE userpost SET likes=%s WHERE pid=%s and uname=%s and tag=%s;",(final_count, psid, usrname, pstags))
            conn.commit()

            uid = session.get('userid')
            sql2 = "INSERT into recomnd(uid,pid,likes) VALUES(%s,%s,%s);"
            val2 = (uid,psid,final_count)
            curs.execute(sql2,val2)

            uname = session.get('user')
            notif = str(uname)+" Give like to your "+pstags+" post"
            sql4 = "INSERT into notifyuser(uname,notify) VALUES(%s,%s);"
            val4 = (uname,notif)
            curs.execute(sql4,val4)
            conn.commit()

            # return "success"

            return redirect(url_for('index'))  
        return redirect(url_for('index'))  
    return redirect(url_for("login"))
#################################################################################################################
#                                       Giving Dislikes to post
#################################################################################################################
@app.route('/dislikes', methods=["GET","POST"])
def dislikes():
    if 'user' in session:
        lik = request.args.get('pslike')
        psid = request.args.get('psid')
        usrname = request.args.get('usrname')
        pstags = request.args.get('pstags')

        # print(psid, usrname, pstags, lik)

        conn = dbConnection()
        curs = conn.cursor()
        sql = "SELECT dislike from userpost where pid=%s and uname=%s and tag=%s;"
        val = (psid, usrname, pstags)
        curs.execute(sql,val)
        res = curs.fetchone()
        result = list(res)
        # print(result)
        # print()
        # print("length of result is: ",len(result))

        like_count = []
        for i in result:
            if i == None:
                # print("yes none is in i")
                a = 0
                like_count.append(a)         
            else:
                # print(" none not present in i")
                a = int(i[0])
                like_count.append(a)
        
        final_count = int(lik)+like_count[0]   
        print()
        print("prinitng final count: ",final_count)
        curs.execute("UPDATE userpost SET dislike=%s WHERE pid=%s and uname=%s and tag=%s;",(final_count, psid, usrname, pstags))
        conn.commit()
        return redirect(url_for('index'))  
    return redirect(url_for("login"))
#################################################################################################################
#                                       Logout
#################################################################################################################
@app.route('/logout')
def logout():
    session.pop('user')
    session.pop('userid')
    return redirect(url_for('index'))

#################################################################################################################
#                                       Logout
#################################################################################################################
from flask_mail import Mail
from flask_mail import Message
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'pranalibscproject@gmail.com'
app.config['MAIL_PASSWORD'] = 'pranalibscproject@123'
app.config['MAIL_DEFAULT_SENDER'] = 'email@email.com'

mail = Mail(app)

# def send_mail(email,otp):
#     try:
#         msg = Message(
#             'Hello user your password is: '+otp,
#             recipients=[email]
#         )
#         msg.body = 'message attachment test'
#     except Exception as e:
#         print(e)


def sendemailtouser(usermail,cmpimg,ogpass):   
    fromaddr = "pranalibscproject@gmail.com"
    toaddr = usermail
   
    #instance of MIMEMultipart 
    msg = MIMEMultipart() 
  
    # storing the senders email address   
    msg['From'] = fromaddr 
  
    # storing the receivers email address  
    msg['To'] = toaddr 
  
    # storing the subject  
    msg['Subject'] = "Reset password"
  
    # string to store the body of the mail 
    body = "Your password for login is: "+ogpass
  
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
  
    # open the file to be sent  
    filename = cmpimg
    attachment = open(cmpimg, "rb") 
  
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
  
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
  
    # encode into base64 
    encoders.encode_base64(p) 
   
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
  
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
  
    # start TLS for security 
    s.starttls() 
  
    # Authentication 
    s.login(fromaddr, "pranalibscproject@123") 
  
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
  
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
  
    # terminating the session 
    s.quit()   


@app.route('/verifydetails',methods=["GET","POST"])
def verifydetails():
    if request.method=="POST":
        username = request.form.get('username')
        usermail = request.form.get('usermail')
        userlname = request.form.get('userlname')
        print(username,usermail,userlname)

        conn = dbConnection()
        curs = conn.cursor()
        fetch_count = curs.execute("SELECT * from userdetails where uname=%s and lname=%s and email=%s;",(username, userlname, usermail))
        # print("fetch_count")
        # print(fetch_count)
        res = curs.fetchone()
        
        if fetch_count==1:
            a = list(res)
            ogpass = a[4]
            cmpimg = "static/images/logo2.png"
            sendemailtouser(usermail,cmpimg,ogpass)
            msg = "Please check your mail we sent to you"
            return render_template("login.html",msg=msg)
        else:
            msg = "Your name/email is wrong"
            return render_template("verifydet.html",msg=msg)
    return render_template("verifydet.html")
#################################################################################################################
#                                       Login
#################################################################################################################
@app.route('/', methods=["GET","POST"])
def login():
    msg = ''
    if request.method == "POST":
        try:
            session.pop('user',None)
            username = request.form.get("email")
            password = request.form.get("pass")
            userrole = request.form.get("rol")
            print(username, password, userrole)


            con = dbConnection()
            cursor = con.cursor()
            cursor.execute('SELECT * FROM userdetails WHERE email = %s AND password = %s AND role=%s', (username, password, userrole))
            result = cursor.fetchone()
            if result:
                session['user'] = result[1]
                session['userid'] = result[0]
                session['umail'] = result[3]
                return redirect(url_for('index'))
            else:
                return render_template("login.html")
        except:
            print("Exception occured at login")
            return render_template("login.html")     
        finally:
            dbClose()
    #return redirect(url_for('index'))
    return render_template("sign-in.html")     
#################################################################################################################
#                                       Register
#################################################################################################################
@app.route('/register', methods=["GET","POST"])
def register():
    if request.method == "POST":
        try:
            fname = request.form.get('fname')
            uname = request.form.get("lname")
            email = request.form.get("email")
            password = request.form.get("pass")
            phonenum = request.form.get("phone")
            finterest = request.form.getlist("foint")
            role = request.form.get("rol")
            follow = "0"
            unfolow = "0"
            verifytag = "../static/images/unverify.png"
            print(fname, uname, email, password, phonenum, finterest, role)
            
            con = dbConnection()
            cursor = con.cursor()
            sql = "INSERT INTO userdetails (uname, lname, email, password, phone, field_interest, role, follow, unfollow, verifytag) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            val = (fname, uname, email, password, phonenum, str(finterest), role, follow, unfolow,str(verifytag))
            cursor.execute(sql, val)
            print("first query submitted")
            print(fname, uname, email, phonenum, verifytag)

            sql2 = "INSERT INTO basicinfo1 (uname, lname, email, phone, verifytag) VALUES (%s, %s, %s, %s, %s);"
            val2 = (fname, uname, email, phonenum, str(verifytag))
            cursor.execute(sql2, val2)
            print("second query submitted")
            con.commit()
            return redirect(url_for('login'))
        except:
            print("Exception occured at register")
            return redirect(url_for('login'))
        finally:
            dbClose()
    return redirect(url_for('login'))
#################################################################################################################
#                                       Admin Login
#################################################################################################################
@app.route('/adlogin', methods=["GET","POST"])
def adlogin():
    msg = ''
    if request.method == "POST":
        try:
            session.pop('user',None)
            username = request.form.get("email")
            password = request.form.get("pass")
            print(username, password)


            con = dbConnection()
            cursor = con.cursor()
            cursor.execute('SELECT * FROM admindetails WHERE email = %s AND password = %s', (username, password))
            result = cursor.fetchone()
            if result:
                session['user'] = result[1]
                session['userid'] = result[0]
                session['umail'] = result[3]
                return redirect(url_for('adindex'))
            else:
                return render_template("admin_login.html")
        except:
            print("Exception occured at login")
            return render_template("admin_login.html")     
        finally:
            dbClose()
    #return redirect(url_for('index'))
    return render_template("admin_login.html")     
#################################################################################################################
#                                      Admin Register
#################################################################################################################
@app.route('/adregister', methods=["GET","POST"])
def adregister():
    if request.method == "POST":
        try:
            fname = request.form.get('fname')
            uname = request.form.get("lname")
            email = request.form.get("email")
            password = request.form.get("pass")
            phonenum = request.form.get("phone")
            
            print(fname, uname, email, password, phonenum)
            
            con = dbConnection()
            cursor = con.cursor()
            sql = "INSERT INTO admindetails (uname, lname, email, password, phone) VALUES (%s, %s, %s, %s, %s)"
            val = (fname, uname, email, password, phonenum)
            cursor.execute(sql, val)
            con.commit()
            return redirect(url_for('adlogin'))
        except:
            print("Exception occured at register")
            return redirect(url_for('adlogin'))
        finally:
            dbClose()
    return redirect(url_for('adlogin'))
#################################################################################################################
#                                       Admin home page
#################################################################################################################
@app.route('/adindex', methods=["GET","POST"])
def adindex():
    if 'user' in session:
        conn = dbConnection()
        curs = conn.cursor()
        curs.execute("SELECT * from basicinfo1")
        res = curs.fetchall()
        if request.method=="POST":
            usrid = request.form.get('uid')
            usname = request.form.get('uname')
            usemail = request.form.get('uemail')

            print(usrid,usname,usemail)

            conn = dbConnection()
            curs = conn.cursor()
            tagimg = "../static/images/verify.png"
            try:
                sql = "UPDATE basicinfo1 SET verifytag=%s where Basicid=%s and uname=%s and email=%s"
                val = (str(tagimg),str(usrid),str(usname),str(usemail))
                print(sql,val)
                curs.execute(sql,val)
                conn.commit()

                curs.execute("SELECT * from basicinfo1")
                res = curs.fetchall()
                
                return render_template("adindex.html",res=res)  
            except Exception as e:
                print(e)
        return render_template("adindex.html",res=res)  
    return redirect(url_for("adlogin")) 


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=8000)
    # app.run('0.0.0.0')