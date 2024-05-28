import asyncio
import sqlite3


async def count_message(count):
    db = sqlite3.connect("id.base")
    cur = db.cursor()
    cur.execute(f"SELECT * FROM messages")
    messages_base = cur.fetchall()
    c = True
    for i in messages_base:
        count = count + 1

    if count == 0:
        c = False

    print(count)
    db.close()
    return count

async def count_message1(count):
    db = sqlite3.connect("id.base")
    cur = db.cursor()
    cur.execute(f"SELECT * FROM messages")
    messages_base = cur.fetchall()

    c = True

    for i in messages_base:
        count = count + 1

    if count == 0:
        c = False
    print(c)
    db.close()
    return c
async def main():
    await count_message(0)
    await count_message1(0)

asyncio.run(main())


