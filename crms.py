# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 12:54:27 2021

@author: shiva
"""
import datetime
import mysql.connector
#print('Successfully imported')
import pytz
import webbrowser

global mydb,cur
#Create connection
mydb= mysql.connector.connect(host='localhost',
                              database='crime',
                              user='root',
                              password='netZaq1@wsx')
#print("Connection created ")

#create cursor
cur = mydb.cursor()


#create login table

query='create table if not exists logindetails(id integer primary key,name varchar(50),pwd varchar(20))'
cur.execute(query)  #execute given query in MySQL
mydb.commit()   # save changes made to the database

#create crime record table

query='create table if not exists crimerecord(id integer primary key,name varchar(20),age integer,crimetype varchar(30),IpcSection varchar(30),city varchar(20),Date varchar(20),tenure integer,recordEntryTime varchar(30))'
cur.execute(query)
mydb.commit()



def login():
    while True:
        uid = input('Enter your id :')
        upass = input('Enter your Password :')
        cur.execute('select * from logindetails where id="{}" and pwd ="{}"'.format(uid,upass))
        mydb.commit
        cur.fetchall()
        mydb.commit()
        rows = cur.rowcount
        if rows!=1:
            print('Invalid Login details..... Try again')
        else:
            print('You are eligible for operating this system............')
            print('\n\n\n')
            print('Press any key to continue...............')
            break
        
def introduction():
     msg = '''
          C R I M E   R E C O R D    I N F O R M A T I O N    S Y S T E M 
          
          - An Introduction
          
          Crime record are the most important part of any modern society for better controlling crime. Crime database database help us to recognise the
          type of crime right now happending in the system and how to overcome that. 

          This project is also trying to solve this simple but very useful information of the crime. The whole 
          database is store in MySQL table alumni that stores their current position as well as some other useful
          information like age,crime type,crime place, Ipc section for arrest and many more
          The whole project is divided into four major parts ie addition of data, modification, searching and 
          reporting. all these part are further divided into menus for easy navigation
          '''
     print(msg)
         
def add_record():
    name=input('Enter name of criminal\n:')
    id=int(input("Enter criminal id:(Note:Criminal id is always unique)")) 
    age=int(input("Enter criminals age:\n"))
    crimetype=input("What did criminal do:") 
    IpcSection=input("Under what IPC charges is criminal arrested:")
    city=input("Which city did crime take place:")
    Date=input("Enter the arrest date:")
    tenure=int(input("Enter number of years of imprisonment:"))
    current_time=datetime.datetime.now(pytz.timezone('Asia/Calcutta'))
    query='insert into crimerecord values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    b=(id,name,age,crimetype,IpcSection,city,Date,tenure,current_time)
    cur.execute(query,b)
    mydb.commit()
    print('\n\nRecord added successfully')

def search_record():
    id=input('Enter criminal Id whom you want to search:')
    query='select * from crimerecord where id={}'.format(id)
    cur.execute(query)
    result=cur.fetchall()
    row=cur.rowcount
    if(row==1):
        print("\n\n{}\n\n".format(result))           
    else:
        print("Record does not exist:")
    
def delete_record():
    id=int(input("\nEnter criminal id whom you want to remove from database:\n"))
    query='delete from crimerecord where id=%d'%(id)
    cur.execute(query)
    mydb.commit()
    print("\n\n\nRecord deleted successfully\n\n")

def display_record():
    print('1.Display all records\n2.Display criminals based on specific crimetype\n3.Display criminals based on specific crime place\nEnter choice:')
    ch=int(input())
    
    if(ch==1):
        print("\n\nId \t Name \t Age \t Crime \t IPC \tPlace\t CrimeDate \t EntryRecordTime")
        s='select * from crimerecord'
        cur.execute(s)
        result=cur.fetchall()
        #print(cur.fetchall())
        for rec in result:
            
            print(rec)
        if(len(result)==0):
            print('\n\n\nSorry,No records found\n\n\n')
    elif(ch==2):
        
        crimetype=input('Enter what type of crime criminals do you want:')
        s='select * from crimerecord where crimetype="{}"'.format(crimetype)
        cur.execute(s)
        result=cur.fetchall()
        print("\n\nId     Name   Age  Crime    IPC    Place      CrimeDate")
        for rec in result:
            print(rec)
        if(len(result)==0):
            print('\n\n!!!!No Records Found!!!\n\n')
    elif(ch==3):
        crimeplace=input('At which place you are searching for crime?:')
        s='select * from crimerecord where city="{}"'.format(crimeplace)
        cur.execute(s)
        result=cur.fetchall()
        print("\n\nId     Name   Age  Crime    IPC    Place      CrimeDate")
        for rec in result:
            print(rec)
        if(len(result)==0):
            print('\n\n!!!!No Records Found!!!\n\n')
            
            
def modify_record():
    id=int(input("Enter criminal id whose information you want to update:")) 
    name=input('Enter name of criminal\n:')
    
    age=int(input("Enter criminals age:\n"))
    crimetype=input("What did criminal do:") 
    IpcSection=input("Under what IPC charges is criminal arrested:")
    city=input("Which city did crime take place:")
    Date=input("Enter the arrest date:")
    tenure=int(input("Enter number of years of imprisonment:"))
    current_time=datetime.datetime.now(pytz.timezone('Asia/Calcutta'))            
    query='update crimerecord set name=%s,crimetype=%s,age=%s,IpcSection=%s,city=%s,Date=%s,tenure=%s,recordEntryTime=%s where id=%s'
    b=(name,crimetype,age,IpcSection,city,Date,tenure,current_time,id)
    cur.execute(query,b)
    mydb.commit()
    print('\nRecord modified successfully\n')
            
def main():
    login()  
    introduction()
    print("\n\n\n")
    while(True):
        print('''
              1.Add records to the database
              2.Search record from database
              3.Delete Record
              4.Display criminal records
              5.Modify Records
              6.View police information of any state
              7.Exit
              Enter your choice:
              ''')
        ch=int(input())
        if(ch==1):
            add_record()
        elif(ch==2):
            search_record()
        elif(ch==3):
            delete_record()
        elif(ch==4):
            display_record()
        elif(ch==5):
            modify_record()
        elif(ch==6):
            var=input('Do you want to see information about any state police?(y/n)')
            if(var=='y'):
                webbrowser.open_new("https://ncrb.gov.in/en/police-links")
        elif(ch==7):
            break;
              
        
                   
            
#call main function
main()            
            
            