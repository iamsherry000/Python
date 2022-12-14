

import sqlite3
conn = sqlite3.connect('test.sqlite')
cursor = conn.cursor()
print("Opened database successfully")


#create table
inset_stmt = 'CREATE TABLE SCHOOL("ID" INT PRIMARY KEY NOT NULL,\
                "NAME" TEXT NOT NULL,"AGE" INT NOT NULL,"ADDRESS" CHAR(50),\
                "MARKS" INT)'
cursor.execute(inset_stmt)


# insert data
cursor.execute("INSERT OR IGNORE INTO SCHOOL VALUES(1,'Rohan',14,'Delhi',200)")
cursor.execute("INSERT OR IGNORE INTO SCHOOL VALUES(2,'Allen',14,'Bangalore',150)")
cursor.execute("INSERT OR IGNORE INTO SCHOOL VALUES(3,'Martha',15,'Hyderabad',200)")
cursor.execute("INSERT OR IGNORE INTO SCHOOL VALUES(4,'Palak',15,'Kolkata',650)")

rows = cursor.execute("SELECT * form SCHOOL").fetchall()
print("inset data:",rows)
conn.commit()

for row in rows:
    print("ID = ",row[0])
    print("NAME = ",row[1])
    print("MARKS = ",row[4],"\n")



