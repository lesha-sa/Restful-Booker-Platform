import pytest


def test_simple_db_query(db_connection):
    cursor = db_connection.cursor()

    # Пример: получить список таблиц в текущей базе (PostgreSQL)
    cursor.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
    """)
    tables = cursor.fetchall()

    cursor.close()

    # Проверяем, что вернулся непустой список таблиц
    assert len(tables) > 0, "No tables found in the database"
