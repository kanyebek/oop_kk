import sqlite3

# A4
connect = sqlite3.connect('Usery.db')

# Ruka c ruchkoi
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usery(
        name VARCHAR(25) NOT NULL,
        age INT NOT NULL,
        hobby  TEXT
    )                  
               '''
               )

connect.commit()

def add_user(name, age, hobby):

    cursor.execute(
        'INSERT INTO usery(name, age, hobby) VALUES(?,?,?)',
        (name, age, hobby)

    )

    connect.commit()
    print("Пользователь {name} добавлен")


def get_all_users():

    cursor.execute('SELECT * FROM usery')
    users = cursor.fetchall()
    print(users)
    print('Список всех пользователей')

    for i in users:
        print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")

def get_user_by_name(imya):

    cursor.execute(
        'SELECT * FROM usery WHERE name = ?',
        (imya,)
    )
    usery = cursor.fetchall()
    for i in usery:
        print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")

# add_user('Max', 19, 'basketball')
# add_user('Beks', 25, 'basketball')
# get_all_users()
get_user_by_name('Beks')
