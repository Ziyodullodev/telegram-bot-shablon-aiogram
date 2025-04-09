import sqlite3
import os

class SQLiteDatabase:
    def __init__(self, db_path='local_database.db'):
        """SQLite bilan bog‘lanish"""
        try:
            self.conn = sqlite3.connect(db_path)
            self.conn.row_factory = sqlite3.Row  # Natijalarni dict sifatida olish uchun
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"❌ SQLite bog‘lanish xatosi: {e}")
            exit(1)

    def insert(self, table, data):
        """Jadvalga yangi yozuv qo‘shish"""
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        values = tuple(data.values())

        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(query, values)
        self.conn.commit()
        return self.cursor.lastrowid

    def update(self, table, data, conditions):
        """Jadvaldagi ma’lumotni yangilash"""
        set_clause = ', '.join([f"{k} = ?" for k in data.keys()])
        where_clause = ' AND '.join([f"{k} = ?" for k in conditions.keys()])
        values = tuple(data.values()) + tuple(conditions.values())

        query = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
        self.cursor.execute(query, values)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def delete(self, table, conditions):
        """Jadvaldan yozuv o‘chirish"""
        where_clause = ' AND '.join([f"{k} = ?" for k in conditions.keys()])
        values = tuple(conditions.values())

        query = f"DELETE FROM {table} WHERE {where_clause}"
        self.cursor.execute(query, values)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def get(self, table, conditions=None, where=None):
        """Bitta yozuvni olish"""
        query = f"SELECT * FROM {table}"
        values = []

        if conditions:
            cond_str = ' AND '.join([f"{k} = ?" for k in conditions.keys()])
            values.extend(conditions.values())
            query += f" WHERE {cond_str}"
        if where:
            query += f" {'AND' if conditions else 'WHERE'} {where}"

        query += " LIMIT 1"
        self.cursor.execute(query, tuple(values))
        row = self.cursor.fetchone()
        return dict(row) if row else None

    def get_all(self, table, conditions=None, where=None):
        """Barcha mos yozuvlarni olish"""
        query = f"SELECT * FROM {table}"
        values = []

        if conditions:
            cond_str = ' AND '.join([f"{k} = ?" for k in conditions.keys()])
            values.extend(conditions.values())
            query += f" WHERE {cond_str}"
        if where:
            query += f" {'AND' if conditions else 'WHERE'} {where}"

        self.cursor.execute(query, tuple(values))
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows] if rows else []

    def execute(self, query, values=None):
        """SQL so‘rovni bajarish"""
        self.cursor.execute(query, values or [])
        return self.cursor.fetchall()

    def close(self):
        """Bog‘lanishni yopish"""
        self.cursor.close()
        self.conn.close()
