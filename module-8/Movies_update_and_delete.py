#Kristopher Kuenning
#4/27/25
#CSD-310
#Module 8

import mysql.connector
from mysql.connector import errorcode


def show_films(cursor, title):
    #method to execute an inner join on all tables,
    #   iterate over the dataset and output the results to the terminal window.

    # inner join query
    cursor.execute("select film_name as Name, film_director as Director, genre_name as Genre, studio_name as "
                   "'Studio Name' from film INNER JOIN genre ON film.genre_id = genre.genre_id "
                   "INNER JOIN studio ON film.studio_id = studio.studio_id")

    # get the results from the cursor object
    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    #iterate over the film data set and display the results
    for film in films:
            print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

try:

        db = mysql.connector.connect(user = 'root',
                                     password = 'KRis2791!?$$$$',
                                     database = 'movies',
                                     raise_on_warnings = True)

        cursor = db.cursor()
        #display initial films
        show_films(cursor, "DiSPLAYING FILMS")

        #insert new film
        cursor.execute("INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)"
                       "VALUES ('SPEED', 1994, 156, 'Jan de Bont', 1, 1)")
        db.commit()
        show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

        #update Alien to Horror
        cursor.execute("UPDATE film SET genre_id = 1"
                       "WHERE film_name = 'Alien'")
        db.commit()
        show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - CHANGED ALIEN to Horror")

        #delete Gladiator
        cursor.execute("""DELETE FROM film WHERE film_name = 'Gladiator'""")
        db.commit()
        show_films(cursor, "DISPLAYING FILMS AFTER DELETE")
        cursor.close()

except mysql.connector.Error as err:
        """ on error code """

        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("  The supplied username or password are invalid")

        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("  The specified database does not exist")

        else:
            print(err)

finally:
        """ close the connection to MySQL """

        db.close()