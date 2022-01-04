import psycopg2
import random
import nanika
import asyncio
import logging
import threading

#async def func(cursor, lst):
def func1(lst):
    #for name in lst:
    #    cursor.execute(f'update users set age={random.randint(minAge, maxAge)} where nickname=\'{name}\';') 
    conn = psycopg2.connect(dbname='zakhar', user='zakhar', host='127.0.0.1', port='5432', password='123')
    cursor = conn.cursor()
    print(cursor)
    for name in lst:
        cursor.execute(f'insert into users (first_name) values (\'{name}\');') 
    #print('Operation is complete')
    logging.info('func is complete ')
    #await asyncio.sleep(3)
    print('func is complete ')
    conn.commit()
    #cursor.close()
    conn.close()

def func2():
    conn = psycopg2.connect(dbname='zakhar', user='zakhar', host='127.0.0.1', port='5432', password='123')
    cursor = conn.cursor()
    cursor.execute(f'update users set last_name=\'rrr\';')
    conn.commit()
    conn.close()


#async def main():
def main():
    # Connect to your postgres DB
    names = nanika.name().getNames()
    #conn = psycopg2.connect(dbname='smile', user='smile', host='192.168.50.78', port='5432', password='123')
    #conn = psycopg2.connect(dbname='zakhar', user='zakhar', host='127.0.0.1', port='5432', password='123')
    # Open a cursor to perform database operations
    #cursor = conn.cursor()
    #def show_sql_req(cursor):
    #    return [ item[0] for item in cursor ]
    #cursor.execute("SELECT * FROM users;")
    #show_sql_req(cursor)
    #aaaa = nanika.name().getNames()
    #cursor.execute(f'select nickname from users')
    #lst = show_sql_req(cursor)
    #task = asyncio.create_task(func(cursor, names))
    x = threading.Thread(target=func1, args=(names,))
    x.start()


    #await task
    logging.info('main is complete ')
    print('main is complete ')
    #print('hello world')
    #conn.close()
    #conn.commit()
    #cursor.close()
    #conn.close()
    #cursor.execute("SELECT * FROM users;")
    #show_sql_req(cursor)
    # Retrieve query results
    #records = cursor.fetchall()
if __name__ == '__main__':
    #asyncio.run(main())
    main()







