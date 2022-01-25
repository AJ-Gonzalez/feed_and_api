import psycopg2


def fetchMovies():
    val = []
    conn = None
    try:
        conn = psycopg2.connect(
            host="72.14.189.61",
            database="movies",
            user="postgres",
            password="password")

        # create a cursor
        cur = conn.cursor()

        cur.execute("SELECT * FROM moviedata;")

        val = cur.fetchall()

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
        return val


def insertMovie(title, desc, price, release):
    conn = None
    try:

        conn = psycopg2.connect(
            host="72.14.189.61",
            database="movies",
            user="postgres",
            password="password")

        # create a cursor
        cur = conn.cursor()

        cmd = "INSERT INTO moviedata VALUES (DEFAULT,'{title}','{desc}','{price}','{release}')".format(
            title=title, desc=desc, price=price, release=release)
        cur.execute(cmd)
        conn.commit()

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# insertMovie("example 2", "not another example movie", "3", "feb 2012")
#print(fetchMovies())
