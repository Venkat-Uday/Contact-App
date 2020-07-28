import sqlite3
import side

conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()
cursor.execute('create table if not exists contacts(name text,number integer )')
cursor.close()

while True:
    print("Choose : \n1.Add contact\n2.Update Contact\n3.Delete Contact\n4.print\n5.serch\n6.exit\n")
    i=int(input("Enter Your Choice:"))
    if i==1:
        name=input("Enter Name:")
        num=int(input("Enter Number:"))
        side.insert(conn,name,num)
    elif i==2:
        name=input("Enter Name:")
        num=int(input("Enter Number:"))
        side.update(conn, name, num)
    elif i==3:
        name=input("Enter Name:")
        side.delete(conn, name)
    elif i==4:
        side.serch(conn)
    elif i==5:
        ip=input("Enter value:")
        side.userview(conn,ip)
    elif i==6:
        side.close(conn)
    else:
        print('input should be between 1 to 6 only')


