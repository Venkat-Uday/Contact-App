import sqlite3
import contact

conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()
cursor.execute('create table if not exists contacts(name text,number integer )')
cursor.close()

i=-1
while i!=6:
    print("Choose : \n1.Add contact\n2.Update Contact\n3.Delete Contact\n4.print\n5.serch\n6.exit\n")
    i=int(input("Enter Your Choice:"))
    if i==1:
        name=input("Enter Name:")
        num=int(input("Enter Number:"))
        contact.insert(conn,name,num)
    elif i==2:
        name=input("Enter Name:")
        num=int(input("Enter Number:"))
        contact.update(conn, name, num)
    elif i==3:
        name=input("Enter Name:")
        contact.delete(conn, name)
    elif i==4:
        contact.serch(conn)
    elif i==5:
        ip=input("Enter value:")
        contact.userview(conn,ip)
    elif i==6:
        contact.close(conn)
    else:
        print('input should be between 1 to 6 only')


