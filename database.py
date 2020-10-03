import mysql.connector

def createDatabase():
    mydb = mysql.connector.connect(
        host="localhost",
        port="3302",
        user="root",
        password="password"
    )
    print(mydb)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase;")

    mydb = mysql.connector.connect(
        host="localhost",
        port="3302",
        user="root",
        password="password",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE IF NOT EXISTS SearchResults (title VARCHAR(255), authors VARCHAR(255), journal VARCHAR(255), datePublished VARCHAR(255), urlList VARCHAR(255), description VARCHAR(255));")
    mycursor.execute("CREATE TABLE IF NOT EXISTS AuthorTable (Citation VARCHAR(255),AuthorKeys VARCHAR(255), firstName VARCHAR(255), lastName VARCHAR(255), institution VARCHAR(255), designation VARCHAR(255));")
    mycursor.execute("CREATE TABLE IF NOT EXISTS UserKeyWordsTable (keywordKey VARCHAR(255),keyword VARCHAR(255), date VARCHAR(255));")
    mycursor.execute("CREATE TABLE IF NOT EXISTS OurKeyWordsTable (keywordKey VARCHAR(255),keyword VARCHAR(255));")
    return mydb