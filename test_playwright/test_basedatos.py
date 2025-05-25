import os
import sqlite3

def test_prueba_general_bd():
    db_path = "db.sqlite3"
    assert os.path.exists(db_path), f" No se encontró la base de datos en {db_path}"

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
    tablas = cursor.fetchall()
    assert tablas, " No se encontraron tablas en la base de datos"

    print(f" Tablas encontradas: {[t[0] for t in tablas]}")

    for tabla in tablas:
        nombre_tabla = tabla[0]
        print(f"\n Analizando tabla: {nombre_tabla}")

        cursor.execute(f"SELECT COUNT(*) FROM {nombre_tabla}")
        total = cursor.fetchone()[0]
        print(f"  → Registros: {total}")

        if total > 0:

            cursor.execute(f"PRAGMA table_info({nombre_tabla})")
            columnas = [col[1] for col in cursor.fetchall()]
            print(f"  → Columnas: {columnas}")


            cursor.execute(f"SELECT * FROM {nombre_tabla} LIMIT 3")
            registros = cursor.fetchall()
            for i, fila in enumerate(registros, start=1):
                print(f"    Registro {i}: {dict(zip(columnas, fila))}")
        else:
            print("   La tabla no tiene registros.")

    conn.close()