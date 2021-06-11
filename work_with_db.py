from os import curdir
import sqlite3
import random


class UrlDataBase:
    def __init__(self):
        self.conn = sqlite3.connect("urls.db", check_same_thread=False)
        self.cursor = self.conn.cursor()

    def get_char_from_number(self, number):
        if number < 26:
            return str(chr(number + 65))
        elif number < 52:
            return str(chr(number - 26 + 97))    
        else:
            return str(number - 52)

    def is_short_url_have(self, short_url):
        execute_str = f"SELECT short_url FROM urls WHERE short_url=='{short_url}'"
        self.cursor.execute(execute_str)
        short_url = self.cursor.fetchall()
        return len(short_url) != 0

    def generate_short_url(self, long_url):
        size_random = 3844
        random_number = random.randrange(start=0,stop=size_random)
        first_number = random_number // 62
        second_number = random_number % 62
        first_char = self.get_char_from_number(first_number)
        second_char = self.get_char_from_number(second_number)
        random_url = f"{first_char}{second_char}"
        print(random_number)
        print(first_number)
        print(second_number)
        while (self.is_short_url_have(random_url)):
            random_number = random.randrange(start=0,stop=size_random)
            first_number = random_number // size_random
            second_number = random_number % size_random
            random_url = f"{first_number}{second_number}"
        return random_url        

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