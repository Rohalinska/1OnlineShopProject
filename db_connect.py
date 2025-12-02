import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="твій_пароль",
    database="shop_db"
)

cursor = conn.cursor()
print("Підключення до бази даних успішне!")

# Закриваємо з'єднання
cursor.close()
conn.close()
