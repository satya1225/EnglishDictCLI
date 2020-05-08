import mysql.connector as db
from difflib import get_close_matches as gcm

con = db.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()
word = input("Enter a word: ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)

results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    query = cursor.execute("SELECT * FROM Dictionary")
    results = cursor.fetchall()
    match = gcm(word, [word[0] for word in results])
    if match:
        yn = input("Did you mean %s? Type Y for yes N for no: " % match[0])
        if yn.lower() == 'y':
            query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % match[0])
            results = cursor.fetchall()
            for result in results:
                print(result[1])
        else:
            print("Word doesn't exist. Please double check it.")
    else:
       print("Word doesn't exist. Please double check it.") 
