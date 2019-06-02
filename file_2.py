import tkinter as tk
import sqlite3

connection=sqlite3.connect("management.db")

TABLE_NAME="management_table"
STUDENT_ID="student_id"
STUDENT_NAME="student_name"
STUDENT_COLLEGE="student_college"
STUDENT_ADDRESS="student_address"
STUDENT_PHONE="student_phone"

def create_table():
    connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME
                   + " ( " + STUDENT_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE +
                   " TEXT, " +
                   STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE +
                  " INTEGER);")

def insert_table(name,college,address,phone):
    # name = input("enter your name")
    # college = input("enter your college name")
    # address = input("enter your address")
    # phone = input("enter the phone number")

    connection.execute("INSERT INTO " + TABLE_NAME + " ( " +
                       STUDENT_NAME + ", " +
                       STUDENT_COLLEGE + ", " + STUDENT_ADDRESS +
                       ", " + STUDENT_PHONE +
                       " )VALUES('"+name+"',' "+college+"','"+address+"',"+str(phone)+" );")
    print("DATA INSERTED")
    connection.commit()


def retrieve_data():
    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    for row in cursor:
        print("student id is : ",row[0])
        print("student name is : ", row[1])
        print("student college is : ",row[2])
        print("student address is : ",row[3])
        print("student phone is : ", row[4])
        connection.commit()

def delete_data(id):
    cursor=connection.execute(" DELETE FROM " + TABLE_NAME + " WHERE " " ( " + STUDENT_ID + " )=( "+id+");")
    connection.commit()
