import psycopg2
import os
from dotenv import load_dotenv

# .env faylini yuklash
load_dotenv()
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_port = os.getenv("DB_PORT")

class Database:
    def __init__(self, db_host=None, db_name=None, db_user=None, db_password=None, db_port=None):
        """PostgreSQL bilan bog‘lanish"""
        try:
            # PostgreSQL bilan bog‘lanish
            self.conn = psycopg2.connect(
                host=db_host,
                database=db_name,
                user=db_user,
                password=db_password,
                port=db_port,
                # connect_timeout=3
            )
            self.cursor = self.conn.cursor()

        except psycopg2.OperationalError as e:
            print(f"❌ PostgreSQL bog‘lanish xatosi: {e}")
            exit(1)  # Dastur to‘xtaydi

        except Exception as e:
            print(f"❌ Noma’lum xatolik: {e}")
            exit(1)  # Dastur to‘xtaydi
    
    def insert(self, table, data):
        """Jadvalga yangi yozuv qo‘shish"""
        columns = ', '.join(data.keys())  
        values_placeholders = ', '.join(['%s'] * len(data))  
        values = tuple(data.values())  
        
        query = f"INSERT INTO {table} ({columns}) VALUES ({values_placeholders}) RETURNING id;"
        print(query)
        self.cursor.execute(query, values)
        inserted_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return inserted_id

    def update(self, table, data, conditions):
        """Jadvaldagi ma’lumotni yangilash"""
        updates = ', '.join([f"{key} = %s" for key in data.keys()])
        conditions_str = ' AND '.join([f"{key} = %s" for key in conditions.keys()])
        values = tuple(data.values()) + tuple(conditions.values())

        query = f"UPDATE {table} SET {updates} WHERE {conditions_str};"
        self.cursor.execute(query, values)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def delete(self, table, conditions):
        """Jadvaldan yozuv o‘chirish"""
        conditions_str = ' AND '.join([f"{key} = %s" for key in conditions.keys()])
        values = tuple(conditions.values())

        query = f"DELETE FROM {table} WHERE {conditions_str};"
        self.cursor.execute(query, values)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def get(self, table, conditions=None, where=None):
        """
        Bitta yozuvni olish (shartlar yoki `where` bilan).
        :param table: Jadval nomi
        :param conditions: (dict) Shartlar (masalan: {"id": 5})
        :param where: (str) Qo‘shimcha SQL sharti (masalan: "year > 2000")
        """
        query = f"SELECT * FROM {table}"
        values = []

        if conditions:
            conditions_str = ' AND '.join([f"{key} = %s" for key in conditions.keys()])
            values.extend(conditions.values())
            query += f" WHERE {conditions_str}"
        if where:
            query += f" {'AND' if conditions else 'WHERE'} {where}"

        query += " LIMIT 1;"
        self.cursor.execute(query, tuple(values))
        return self.cursor.fetchone()

    def get_all(self, table, conditions=None, where=None):
        """
        Barcha mos yozuvlarni olish (`where` bilan ishlaydi).
        :param table: Jadval nomi
        :param conditions: (dict, optional) Shartlar (masalan: {"author": "Oda"})
        :param where: (str, optional) Qo‘shimcha SQL sharti (masalan: "year > 2000")
        """
        query = f"SELECT * FROM {table}"
        values = []

        if conditions:
            conditions_str = ' AND '.join([f"{key} = %s" for key in conditions.keys()])
            values.extend(conditions.values())
            query += f" WHERE {conditions_str}"

        if where:
            query += f" {'AND' if conditions else 'WHERE'} {where}"

        self.cursor.execute(query, tuple(values))
        return self.cursor.fetchall()

    def execute(self, query, values=None):
        """SQL so‘rovni bajarish"""
        self.cursor.execute(query, values)
        return self.cursor.fetchall()
     
    def close(self):
        """Bog‘lanishni yopish"""
        self.cursor.close()
        self.conn.close()


# db = Database(db_host, db_name, db_user, db_password, db_port)
# print("🔗 PostgreSQL bilan bog‘landik!")

# user = db.get("users_user", {"telegram_id": "123"})

# print(user)