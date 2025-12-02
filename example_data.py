import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="твій_пароль",
    database="shop_db"
)

cursor = conn.cursor()

# Додати приклад користувача
cursor.execute("""
INSERT INTO users (name, email, password, role) 
VALUES (%s, %s, %s, %s)
""", ("Олександра", "alex@gmail.com", "hashed_password", "customer"))

# Додати приклад продукту
cursor.execute("""
INSERT INTO products (name, category, price, description)
VALUES (%s, %s, %s, %s)
""", ("Ноутбук", "Електроніка", 25000.00, "Ігровий ноутбук"))

conn.commit()
cursor.close()
conn.close()
print("Дані додані успішно!")
