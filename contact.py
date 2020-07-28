import sqlite3


def insert(conn,name,num):
    cur=conn.cursor()
    cur.execute('select * from contacts where Name=? or Number=?',(name,num))
    c = cur.fetchall()
    if not c:
        cur.execute('insert into contacts values(?,?)', (name,num))
        print('Contact Inserted.')
    else:
        print('Contact Already Exists.')
    conn.commit()

def update(conn,name,num):
    cur=conn.cursor()
    cur.execute('select * from contacts where Name=?',(name,))
    c=cur.fetchone()
    if c is None:
        print('No Contact with that name present')
    else:
        cur.execute('update contacts set Number=? where Name=?',(num,name))
        print("Updated the required contact")
    conn.commit()

def serch(conn):
    cur=conn.cursor()
    cur.execute('select * from contacts')
    c=cur.fetchall()
    if not c:
        print("No Contacts present.")
    else:
        print("Displaying Contacts:")
        for row in c:
            print(row)

def userview(conn,name):
    cur=conn.cursor()
    cur.execute('select * from contacts where Name like"%{}%"'.format(name))
    c=cur.fetchall()
    if not c:
        print("No contacts present")
    else:
        for row in c:
            print(row)

def delete(conn,name):
    cur=conn.cursor()
    cur.execute('select * from contacts where Name=?',(name,))
    c=cur.fetchone()
    if not c:
            print(" not found")
    else:
        cur.execute('delete from contacts where Name=?',(name,))
        print("contact  deleted")
    conn.commit()

def close(conn):
    conn.close()



