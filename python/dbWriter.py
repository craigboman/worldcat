import sqlite3, time, datetime
import sys
sys.path.insert(0, '..') # allows scripts to be import from parent directory

def batchStatus(results):
    from random import uniform
    import sqlite3, time, datetime
    from stati.holdingStatus import status
    batch,fail = [],[]
    def status(results):
        for i in results:
            try:
                test = status(i)
                if test:
                    print('status checked', test)
                    batch.append([i, test])
                    print(len(batch))
                else:
                    print('status read failed')
                    fail.append(i)
            except:
                ('nothing worked, throwing in the towel')
            wait = uniform(0,.5)
            time.sleep(wait)
    status(results)
    return batch,fail
        # mul.append([i,test])
        # print(len(mul))

def dbWriter(batch):
    import sqlite3, time, datetime
    c,conn = connect_db()
    create_db(c)
    # should not need to create table but it doesn't work without it
    for i in batch:
        try:
            c.execute("INSERT INTO test VALUES({},{})".format(*i))
            conn.commit()
            print('db write successful')
        except:
            print('db write failed')
    db_close(c, conn)

def dbWriter2(batch):
    import sqlite3, time, datetime
    c,conn = connect_db()
    create_db(c)
    # should not need to create table but it doesn't work without it
    for i in batch:
        try:
            c.execute("INSERT INTO swdep VALUES({},{})".format(*i))
            conn.commit()
            print('db write successful')
        except:
            print('db write failed')
    db_close(c, conn)


# https://python-forum.io/Thread-insert-list-into-sqlite3

def create_db(c):
    c.execute('CREATE TABLE IF NOT EXISTS swdep(oclc,status)')

def connect_db():
    conn = sqlite3.connect('../Oxford.db')
    c = conn.cursor()
    return c,conn

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%m-%d'))
    value = random.randrange(0,len(words))
    c.execute("INSERT INTO foobar (unix,datestamp,value) VALUES(?,?,?)",
    (unix, date, value))
    conn.commit()

def db_close(c, conn):
    c.close()
    conn.close()

# really bad loop; don't use without a bunch of work
def failLoop(batch,fail):
    batch, fail = batchStatus(slice)
    if fail:
        fail.append()

if __name__ == "__main__":
    one = ['27429232', '32778355', '968141', '39381268', '7119961', '575236', '16715413', '558486', '774160330', '7430088']
    two = ['17257924', '13845695', '21972508', '48070545', '34281492', '52511400', '51182403', '43396865', '48195094', '32075467']
    dbWriter(one)
    # batchStatus(slice)

    # use multiPool to pool processes
    # multiPool(one,two)

# deprecated; multiple sql writes don't work
# def multi(one,two):
#     import multiprocessing
#     # creating processes
#     p1 = multiprocessing.Process(target=dbWriter, args=(one[:3], ))
#     p2 = multiprocessing.Process(target=dbWriter, args=(two[:3], ))
#     # starting process 1
#     p1.start()
#     # starting process 2
#     p2.start()
#     # wait until process 1 is finished
#     p1.join()
#     # wait until process 2 is finished
#     p2.join()
#     # both processes finished
#     print("Done!")
