import pymysql

conn = pymysql.connect(
    host='database-1.cyyijqhtrsrx.us-east-1.rds.amazonaws.com',
    port=int(3306),
    user="admin",
    passwd="dhruvabhi",
    db="studentinfo")

print("connected");


#cursor=conn.cursor()
#create_table="""
#create table Details (name varchar(200),email varchar(200))
#"""
#cursor.execute(create_table)


def insert_details(name,email,contact_number,address):
    cur=conn.cursor()
    cur.execute("INSERT INTO Details (name,email,contact_number,address) VALUES (%s,%s,%s,%s)", (name,email,contact_number,address))
    conn.commit()

def get_details():
    cur=conn.cursor()
    cur.execute("SELECT *  FROM Details")
    details = cur.fetchall()
    return details

