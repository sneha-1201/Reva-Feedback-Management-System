
import pymysql
#import aws_credentials as rds
conn = pymysql.connect(
        host= 'feedback.c4whtecwxnws.us-east-1.rds.amazonaws.com', #endpoint link
        port = 3306, # 3306
        user = 'admin', # admin
        password = 'admin123', #adminadmin
        db = 'feedback', #test
        )

#Table Creation
#cursor=conn.cursor()
#create_table="""
#create table Details (name varchar(200),email varchar(200),comment varchar(200),gender varchar(20) )
#"""
#cursor.execute(create_table)


def insert_cdetails(name,classrate,placement,washroom,cleanliness,arch,libr,sports,foodcourt,healthcenter,campusenv,comment):
    cur=conn.cursor()
    cur.execute("INSERT INTO CAMPUS (name,classrate,placement,washroom,cleanliness,arch,libr,sports,foodcourt,healthcenter,campusenv,comment) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (name,classrate,placement,washroom,cleanliness,arch,libr,sports,foodcourt,healthcenter,campusenv,comment))
    conn.commit()

def get_details():
    cur=conn.cursor()
    cur.execute("SELECT *  FROM CAMPUS")
    cdetails = cur.fetchall()
    return cdetails

def insert_hdetails(blockname,room,food,staff,laundary,wifi,housekeeping,warden,problem,hostelcomment):
    cur=conn.cursor()
    cur.execute("INSERT INTO HOSTEL (blockname,room,food,staff,laundary,wifi,housekeeping,warden,problem,hostelcomment) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (blockname,room,food,staff,laundary,wifi,housekeeping,warden,problem,hostelcomment))
    conn.commit()

def get_hdetails():
    cur=conn.cursor()
    cur.execute("SELECT *  FROM HOSTEL")
    hdetails = cur.fetchall()
    return hdetails

def insert_fdetails(facultyname,teaching,communication,involvement,assignments,mentoring,guidance,friendly,facultycomment):
    cur=conn.cursor()
    cur.execute("INSERT INTO FACULTY (facultyname,teaching,communication,involvement,assignments,mentoring,guidance,friendly,facultycomment) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (facultyname,teaching,communication,involvement,assignments,mentoring,guidance,friendly,facultycomment))
    conn.commit()

def get_fdetails():
    cur=conn.cursor()
    cur.execute("SELECT *  FROM FACULTY")
    fdetails = cur.fetchall()
    return fdetails

def insert_tdetails(routenumber,buscondition,punctuality,driving,safety,behaviour,comfort,transportcomment):
    cur=conn.cursor()
    cur.execute("INSERT INTO TRANSPORT (routenumber,buscondition,punctuality,driving,safety,behaviour,comfort,transportcomment) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (routenumber,buscondition,punctuality,driving,safety,behaviour,comfort,transportcomment))
    conn.commit()

def get_tdetails():
    cur=conn.cursor()
    cur.execute("SELECT *  FROM TRANSPORT")
    tdetails = cur.fetchall()
    return tdetails
