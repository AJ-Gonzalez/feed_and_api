#!/usr/bin/python
import psycopg2


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')

        conn = psycopg2.connect(
            host="72.14.189.61",
            database="movies",
            user="postgres",
            password="password")

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # cmd = """CREATE TABLE moviedata (
        #     movie_id SERIAL PRIMARY KEY,
        #     title VARCHAR(255) NOT NULL,
        #     description VARCHAR(255) NOT NULL,
        #     price VARCHAR(255) NOT NULL,
        #     release VARCHAR(255) NOT NULL);"""
        # cur.execute(cmd)
        # conn.commit()
        
        cur.execute("SELECT * FROM moviedata;")
    
        print(cur.fetchall())
        cur.execute("INSERT INTO moviedata VALUES (DEFAULT,'Example Movie 1','an example film','20','Jan 2007')")
        conn.commit()

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
