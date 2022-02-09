import sqlite3 as sl

import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
db2 = os.path.join(THIS_FOLDER, 'fmbl.db')

db = "TikToks.db"
# api = TikTokApi.get_instance()
#
#
#
# #
# def parseTikTok():
#     count = 100
#     soundId = '6826096341966456833'
#     tiktoks = api.bySound(soundId, count=count)
#     list_of_tiktoks = []
#     for tiktok in tiktoks:
#         tiktok_user = tiktok["author"]["uniqueId"]
#         tiktok_id = tiktok["id"]
#         url = url_builder(tiktok_id, tiktok_user)
#         pair = (tiktok_user, url)
#         list_of_tiktoks.append(pair)
#     return list_of_tiktoks
conn1 = sl.connect(db2)
curs1 = conn1.cursor()


def update_fumble(username, reason):
    # conn = sl.connect(db2)
    stmt = '''INSERT into reasons(User, Reason) Values(?,?)'''
    ver = (str(username), str(reason))
    # curs = conn.cursor()
    curs1.execute(stmt, ver)
    conn1.commit()


def get_reasons():
    #conn = sl.connect(db2)
    stmt = '''select * from reasons'''
    #curs = conn.cursor()
    reasons = curs1.execute(stmt)
    return reasons


def url_builder(tiktok_id, tiktok_user):
    url = 'https://www.tiktok.com/'
    url += '@'
    url += tiktok_user
    url += '/video/' + tiktok_id
    return url


def add_fmbl():
    print(db2)
   # conn = sl.connect(db2)
    stmt = '''UPDATE choices SET Fumbles = Fumbles + 1'''
    #curs = conn.cursor()
    curs1.execute(stmt)

    get_fumbles = '''select * from choices'''
    conn1.commit()
    return curs1.execute(get_fumbles)

def remove_fumble(author, ID):
    stmt = '''''' + 'DELETE from reasons where uniqueid=' + str(ID) + " and User='" +str(author) + "'" + ''''''
    print(stmt)
    curs1.execute(stmt)
    conn1.commit()

    if curs1.rowcount == 0:
        return "You either have to be the author to delete that message or the unique id doesn't exist"
    else:
        return "Deleted the reason!"

def sub_fmbl():
    #conn = sl.connect(db2)
    stmt = '''UPDATE choices SET Fumbles = Fumbles - 1'''
    #curs = conn.cursor()
    curs1.execute(stmt)

    get_fumbles = '''select * from choices'''
    fumbles = curs1.execute(get_fumbles)
    conn1.commit()
    return fumbles


def write_to_db(tiktoks):
    conn = sl.connect(db)
    for x in tiktoks:
        ver = (x[0], x[1])
        curs = conn.cursor()
        stmt = '''INSERT INTO buss(Username, Link) VALUES(?,?)'''
        curs.execute(stmt, ver)
    conn.commit()
    conn.close()


def pick_random_link():
    conn = sl.connect(db)
    stmt = '''SELECT * FROM buss ORDER BY RANDOM() LIMIT 1'''
    curs = conn.cursor()
    return curs.execute(stmt)

#
# if __name__ == "__main__":
#     tiks = parseTikTok()
#     write_to_db(tiks)
#     link = pick_random_link()
#     for x in link:
#         print(x)
