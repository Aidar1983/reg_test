import sqlite3

async def clean_massage_base():
    db = sqlite3.connect("id.base")
    cur = db.cursor()
    cur.execute(f"DELETE FROM messages ")
    # cur.execute("DROP TABLE messages")
    # cur.execute("SELECT * FROM messages")
    # a = cur.fetchall()
    # print(a)
    # # cur.execute("DROP TABLE IF EXISTS messages")
    # try:
    #     cur.execute("PRAGMA table_info(messages)")
    #     print("Таблица существует")
    # except sqlite3.OperationalError:
    #     print("Таблица не существует")

    db.commit()
    db.close()


