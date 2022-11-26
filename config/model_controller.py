import sqlite3

def create_db():
    db_proyect= sqlite3.connect("db_pdf.db")
    try:
    
        cursor_db_proyect = db_proyect.cursor()
        query = """ CREATE TABLE files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name  VARCHAR (250) NOT NULL,
                path VARCHAR(250) NOT NULL,
                size VARCHAR(10) NOT NULL,
                creation VARCHAR(15) NOT NULL
        )
        """
        cursor_db_proyect.execute(query)
        db_proyect.close()
    except:
        print("La tabla ya existe")

def insert_file(name, path, size, creation):
    db_proyect= sqlite3.connect("db_pdf.db")
    cursor_db_proyect = db_proyect.cursor()
    data = (name, path, size, creation)
    query = "INSERT INTO files (name, path, size, creation) VALUES(?, ?, ?, ?)"
    cursor_db_proyect.execute(query, data)
    db_proyect.commit()
    db_proyect.close()

def get_all_files():
    db_proyect= sqlite3.connect("db_pdf.db")
    cursor_db_proyect = db_proyect.cursor()
    query = "SELECT  * FROM files"
    cursor_db_proyect.execute(query)
    return cursor_db_proyect.fetchall()

def get_by_title(title, creation):
    db_proyect = sqlite3.connect("db_pdf.db")
    cursor_db_proyect = db_proyect.cursor()
    query = f"SELECT * FROM files WHERE name LIKE '%{title}%' AND creation LIKE '%{creation}%';"
    cursor_db_proyect.execute(query)
    return cursor_db_proyect.fetchall()

def get_file_by_id(id):
    db_proyect = sqlite3.connect("db_pdf.db")
    cursor_db_proyect = db_proyect.cursor()
    data = (id,)
    query = f"SELECT * FROM files WHERE id = ?;"
    cursor_db_proyect.execute(query, data)
    return cursor_db_proyect.fetchall()


def delete_by_id(id):
    db_proyect  = sqlite3.connect("db_pdf.db")
    cursor_db_proyect = db_proyect.cursor()
    query = f"DELETE FROM files WHERE id = {id}"
    cursor_db_proyect.execute(query)
    db_proyect.commit()
    db_proyect.close()

def edit_file(id,new_title, new_path, new_creation):
    db_proyect = sqlite3.connect("db_pdf.db")
    cursor_db_proyect = db_proyect.cursor()
    data =(new_title, new_path, new_creation, id)
    query = f"UPDATE files SET name = ?, path = ? , creation = ? WHERE id = ?;" 
    cursor_db_proyect.execute(query, data)
    db_proyect.commit()
    db_proyect.close()