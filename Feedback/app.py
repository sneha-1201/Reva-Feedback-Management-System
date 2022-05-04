from flask import Flask, render_template, request, flash, redirect,url_for, jsonify, session 
from flask import Response,send_file

app = Flask(__name__)

import rds_db as db

@app.route('/',methods = ['GET','POST'])
def index():

    return render_template("index.html")

@app.route('/campus',methods = ['GET','POST'])
def campus():
    
    if request.method == 'POST':
        name = request.form['name']
        comment = request.form['comment']
        classrate = request.form['class']
        placement = request.form['prate']
        washroom = request.form['wrate']
        cleanliness = request.form['clrate']
        arch = request.form['arate']
        libr = request.form['lrate']
        sports = request.form['srate']
        foodcourt = request.form['fcrate']
        healthcenter = request.form['hrate']
        campusenv = request.form['erate']
        db.insert_cdetails(name,classrate,placement,washroom,cleanliness,arch,libr,sports,foodcourt,healthcenter,campusenv,comment)
        cdetails = db.get_details()
        print(cdetails)
        for detail in cdetails:
            var = detail
    return render_template("campus.html")

@app.route('/hostel',methods = ['GET','POST'])
def hostel():
    
    if request.method == 'POST':
        blockname = request.form['bname']
        hostelcomment = request.form['hcomment']
        room = request.form['room']
        food = request.form['food']
        staff = request.form['staff']
        laundary = request.form['ld']
        wifi = request.form['wifi']
        housekeeping = request.form['hk']
        warden = request.form['warden']
        problem= request.form['prob']
        db.insert_hdetails(blockname,room,food,staff,laundary,wifi,housekeeping,warden,problem,hostelcomment)
        hdetails = db.get_hdetails()
        print(hdetails)
        for detail in hdetails:
            var = detail
    return render_template("hostel.html")


@app.route('/faculty',methods = ['GET','POST'])
def faculty():
    
    if request.method == 'POST':
        facultyname = request.form['facultyname']
        teaching = request.form['teaching']
        communication = request.form['communication']
        involvement = request.form['involvement']
        assignments = request.form['assignments']
        mentoring = request.form['mentoring']
        guidance = request.form['guidance']
        friendly = request.form['friendly']
        facultycomment = request.form['facultycomment']
        db.insert_fdetails(facultyname,teaching,communication,involvement,assignments,mentoring,guidance,friendly,facultycomment)
        fdetails = db.get_fdetails()
        print(fdetails)
        for detail in fdetails:
            var = detail
    return render_template("faculty.html")


@app.route('/transportation',methods = ['GET','POST'])
def transportation():
    
    if request.method == 'POST':
        routenumber=request.form['routenumber']
        buscondition = request.form['buscondition']
        punctuality = request.form['punctuality']
        driving = request.form['driving']
        safety = request.form['safety']
        behaviour = request.form['behaviour']
        comfort = request.form['comfort']
        transportcomment = request.form['transportcomment']
        db.insert_tdetails(routenumber,buscondition,punctuality,driving,safety,behaviour,comfort,transportcomment)
        tdetails = db.get_tdetails()
        print(tdetails)
        for detail in tdetails:
            var = detail
    return render_template("transportation.html")



if __name__ == "__main__":
    
    app.run(debug=True)