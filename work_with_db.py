from os import curdir
import sqlite3

class UrlDataBase:

    def __init__(self):
        self.conn = sqlite3.connect("urls.db", check_same_thread=False)
        self.cursor = self.conn.cursor()

    def generate_short_url(self, long_url):
        return "qwert"

    def add_new_url(self, long_url):
        short_url = self.generate_short_url(long_url)
        execute_str = f"INSERT INTO urls VALUES ('{long_url}', '{short_url}');"
        self.cursor.execute(execute_str)
        self.conn.commit()
        return short_url

    def get_short_url_from_db(self, long_url):
        execute_str = f"SELECT short_url FROM urls WHERE long_url=='{long_url}'"
        self.cursor.execute(execute_str)
        short_url = self.cursor.fetchall()
        return short_url

    def get_short_url(self, long_url):
        short_url = self.get_short_url_from_db(long_url)
        if len(short_url) != 0:
            return short_url[0][0]
        else:
            return self.add_new_url(long_url)
