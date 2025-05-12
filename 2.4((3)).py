import sqlite3
import time
from datetime import datetime


class SystemMonitorDatabase:
    def __init__(self):
        self.connection = sqlite3.connect("system_monitor.db")
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS monitoring_data (
                id INTEGER PRIMARY KEY,
                timestamp DATETIME NOT NULL,
                cpu_usage REAL NOT NULL,
                memory_usage REAL NOT NULL,
                disk_usage REAL NOT NULL
            )
        ''')
        self.connection.commit()

    def insert_monitoring_data(self, cpu, memory, disk):
        timestamp = datetime.now()
        self.cursor.execute('''
            INSERT INTO monitoring_data (timestamp, cpu_usage, memory_usage, disk_usage) VALUES (?, ?, ?, ?)
        ''', (timestamp, cpu, memory, disk))
        self.connection.commit()

    def fetch_all_data(self):
        self.cursor.execute('SELECT * FROM monitoring_data')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()


class SystemMonitor:
    def __init__(self):
        self.db = SystemMonitorDatabase()

    def monitor_system(self, interval=10):
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_usage = psutil.virtual_memory().percent
            disk_usage = psutil.disk_usage('/').percent

            print(f'Time: {datetime.now()}, CPU: {cpu_usage}%, Memory: {memory_usage}%, Disk: {disk_usage}%')

            self.db.insert_monitoring_data(cpu_usage, memory_usage, disk_usage)
            time.sleep(interval)

    def view_data(self):
        data = self.db.fetch_all_data()
        for entry in data:
            print(f'Time: {entry[1]}, CPU: {entry[2]}%, Memory: {entry[3]}%, Disk: {entry[4]}%')

    def close(self):
        self.db.close()


if __name__ == "__main__":
    monitor = SystemMonitor()

    try:
        print("Starting system monitoring...")
        monitor.monitor_system(interval=10)  # Интервал между измерениями (в секундах)
    except KeyboardInterrupt:
        print("Stopping system monitoring...")
        monitor.view_data()  # Показываем сохраненные данные перед выходом
    finally:
        monitor.close()
