import pymysql

def insert():
    con=pymysql.connect(host='localhost',user='root',password='',database='Siera')
    
    mwanzo='Garissa'
    mwisho='Mandera'
    date='22/08/2022'
    time='4AM'
    amount=1000

    cursor=con.cursor()


    sql='insert into bookings(mwanzo,mwisho,date,time,amount)values(%s,%s,%s,%s,%s)'
    cursor.execute(sql,(mwanzo,mwisho,date,time,amount))
    con.commit()
    print('saved successfully')

insert()

def insert():
    con=pymysql.connect(host='localhost',user='root',password='',database='Siera')
    
    first_name='Bernedet'
    last_name='Mwihaki'
    speciality='Opthamologist'
    gender='male'
    phone_number=711456998

    cursor=con.cursor()


    sql='insert into doctors(first_name,last_name,speciality,gender,phone_number)values(%s,%s,%s,%s,%s)'
    cursor.execute(sql,(first_name,last_name,speciality,gender,phone_number))
    con.commit()
    print('saved')

insert()



















