
import sqlite3

async def select_from_base():
    db = sqlite3.connect("id.base")
    cur = db.cursor()

    cur.execute(f"SELECT * FROM corses ORDER BY id DESC LIMIT 1")
    db.commit()
    a = cur.fetchone()
    db.close()
    return a


# db = sqlite3.connect("id.base")
# cur = db.cursor()
# cur.execute(f"SELECT * FROM corses ORDER BY id DESC LIMIT 1")
# db.commit()
# a = cur.fetchone()
# db.close()



