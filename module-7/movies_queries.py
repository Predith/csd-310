#Kristoher Kuenning
#4/27/2025
#CSD-310
#Module 7.2

""" import statements """
import mysql.connector # to connect
from mysql.connector import errorcode, cursor

import dotenv # to use .env file
from dotenv import dotenv_values

#using our .env file
secrets = dotenv_values(".env")

""" database config object """
config = {
    "user": 'root',
    "password": 'KRis2791!?$$$$',
    "host": 'localhost',
    "database": 'movies',
    "raise_on_warnings": True #not in .env file
}

try:
    """ try/catch block for handling potential MySQL database errors """

    db = mysql.connector.connect(**config)  # connect to the movies database

    # output the connection status
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    cursor = db.cursor()

#first query: select all from studio
    print("Displaying studio records")
    cursor.execute("SELECT studio_id, studio_name FROM studio")
    studios = cursor.fetchall()
    for studio in studios:
        print(f"Studio ID: {studio[0]}"
              f"Studio Name: {studio[1]}\n")

#second query: select all from genre
    print("Displaying Genre records")
    cursor.execute("SELECT genre_id, genre_name FROM genre")
    genres = cursor.fetchall()
    for genre in genres:
        print(f"Genre ID: {genre[0]}"
              f"Genre Name: {genre[1]}\n")

#Third query: select all from film
    print ("Displaying film records")
    cursor.execute("SELECT film_name, film_runtime FROM film where film_runtime < 120")
    films = cursor.fetchall()
    for film in films:
        print(f"Film Name: {films[0]}"
              f"Film Runtime: {films[1]}\n")

#Forth query: select all from directors
    print ("Displaying director records")
    cursor.execute("SELECT film_name, film_director FROM film")
    film_director = cursor.fetchall()
    for film in film_director:
        print(f"Film Name: {film_director[0]}"
              f"Film Director: {film_director[1]}\n")

    cursor.close()


    input("\n\n  Press any key to continue...")

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

