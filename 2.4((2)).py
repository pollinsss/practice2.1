import sqlite3
class DrinkDatabase:
    def __init__(self):
        self.connection = sqlite3.connect("drinks.db")
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS alcoholic_drinks (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                strength REAL NOT NULL,
                stock INTEGER NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cocktails (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                strength REAL NOT NULL,
                price REAL NOT NULL,
                composition TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def add_alcoholic_drink(self, name, strength, stock):
        self.cursor.execute('''
            INSERT INTO alcoholic_drinks (name, strength, stock) VALUES (?, ?, ?)
        ''', (name, strength, stock))
        self.connection.commit()

    def add_cocktail(self, name, ingredients):
        total_strength = sum(self.get_drink_strength(ing) for ing in ingredients) / len(ingredients)
        price = sum(self.get_drink_price(ing) for ing in ingredients)
        self.cursor.execute('''
            INSERT INTO cocktails (name, strength, price, composition) VALUES (?, ?, ?, ?)
        ''', (name, total_strength, price, ', '.join(ingredients)))
        self.connection.commit()

    def get_drink_strength(self, name):
        self.cursor.execute('''
            SELECT strength FROM alcoholic_drinks WHERE name = ?
        ''', (name,))
        return self.cursor.fetchone()[0]

    def get_drink_price(self, name):
        self.cursor.execute('''
            SELECT price FROM alcoholic_drinks WHERE name = ?
        ''', (name,))
        return self.cursor.fetchone()[0]

    def update_stock(self, name, amount):
        self.cursor.execute('''
            UPDATE alcoholic_drinks SET stock = stock + ? WHERE name = ?
        ''', (amount, name))
        self.connection.commit()

    def sell_drink(self, name, quantity):
        self.cursor.execute('''
            UPDATE alcoholic_drinks SET stock = stock - ? WHERE name = ?
        ''', (quantity, name))
        self.connection.commit()

    def view_drinks(self):
        self.cursor.execute('SELECT * FROM alcoholic_drinks')
        return self.cursor.fetchall()

    def view_cocktails(self):
        self.cursor.execute('SELECT * FROM cocktails')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()


# Пример использования
db = DrinkDatabase()

# Добавление алкогольных напитков
db.add_alcoholic_drink("Водка", 40, 100)
db.add_alcoholic_drink("Ром", 37.5, 50)

# Пополнение запасов
db.update_stock("Водка", 20)

# Продажа напитка
db.sell_drink("Водка", 5)

# Добавление коктейля
db.add_cocktail("Куба Либре", ["Ром", "Кока-кола", "Лайм"])

# Просмотр всех напитков и коктейлей
print("Напитки:")
for drink in db.view_drinks():
    print(drink)

print("\nКоктейли:")
for cocktail in db.view_cocktails():
    print(cocktail)

db.close()
