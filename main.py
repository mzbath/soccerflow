import sqlite3

# connects to a .db file or it creates a new one if not found
conn = sqlite3.connect('store.db')

# remove the table if already present
conn.execute('''DROP TABLE IF EXISTS pet''')

# executes the query to create the table with columns
conn.execute('''CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), 
             sex CHAR(1), checkups SMALLINT UNSIGNED, birth DATE, death DATE) '''
             )
print("Table created successfully !")

# insert data into the table
conn.execute('''INSERT INTO pet (name, owner, species, sex, checkups, birth, death)
            VALUES ('Fluffy', 'Harold', 'cat', 'f', 5, '2001-02-04','')'''
            )
conn.execute('''INSERT INTO pet (name, owner, species, sex, checkups, birth, death) 
            VALUES ('Claws', 'Gwen', 'cat', 'm', 2, '2000-03-17', '')'''
            )
# commit the changes
conn.commit()

print("Records created successfully !")
print("Total number of rows created : ", conn.total_changes)

# Print all the info in the table
cursor = conn.execute('''SELECT * FROM pet''')
for row in cursor:
    print("name = ", row[0])
    print("owner = ", row[1])
    print("species = ", row[2])
    print("sex = ", row[3])
    print("checkups = ", row[4])
    print("birth = ", row[5])
    print("death = ", row[6], "\n")

# Update records in the table
conn.execute(
'''UPDATE pet
   SET checkups = 4
 WHERE name='Claws';'''
)
conn.commit()


cursor = conn.execute('''SELECT * FROM pet''')
for row in cursor:
    print("name = ", row[0])
    print("owner = ", row[1])
    print("species = ", row[2])
    print("sex = ", row[3])
    print("checkups = ", row[4])
    print("birth = ", row[5])
    print("death = ", row[6], "\n")