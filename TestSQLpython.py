import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS saves(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     class TEXT,
     lvl INTERGER,
     xp INTERGER,
     hp INTERGER,
     atk INTERGER
)
""")
conn.commit()
"""
conn.execute("INSERT INTO saves (id,class,lvl,xp,hp,atk) \
      VALUES (781, 'Archer', 32, 2, 5,6)");

conn.commit()
print ("Records created successfully")

text="UPDATE saves SET atk=98 WHERE id=41"
text2="UPDATE saves SET hp=98 WHERE id=41"
conn.execute(text)
conn.execute(text2)

for name in ("1"):
    cursor.execute("SELECT rowid FROM saves WHERE id = ?", (name,))
    data=cursor.fetchall()
    if len(data)==0:
        print('There is no component named %s'%name)
    else:
        print('Component %s found with rowids %s'%(name,','.join(map(str, next(zip(*data))))))
"""

def chargersauvegarde():
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM saves WHERE id = ?", (1, ))
        user1 = cursor.fetchone()

        conn.commit()
        return(user1,"Voici les infos de la sauvegarde")

print(chargersauvegarde())
conn.commit()
conn.close()
