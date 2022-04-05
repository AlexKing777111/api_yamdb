import sqlite3
import csv
import os
from django.core.management.base import BaseCommand

from api_yamdb.settings import BASE_DIR

PATH_DIR = os.path.join(BASE_DIR, r"static\data")
PATH_TO_BD = "../api_yamdb/db.sqlite3"

CONFORMITY = [
    {"users.csv": "users_user"},
    {"category.csv": "reviews_category"},
    {"genre.csv": "reviews_genre"},
    {"titles.csv": "reviews_title"},
    {"genre_title.csv": "reviews_title_genre"},
    {"review.csv": "reviews_review"},
    {"comments.csv": "reviews_comment"},
]


class Command(BaseCommand):
    help = "Data import..........."

    def handle(self, *args, **options):
        con = sqlite3.connect(PATH_TO_BD)
        cur = con.cursor()

        for i in CONFORMITY:
            for j in i.keys():
                PATH_TO_FILE = os.path.join(PATH_DIR, j)
                table_name = i[j]

                with open(PATH_TO_FILE, "r", encoding="utf-8") as f_open_csv:
                    rows = csv.DictReader(f_open_csv)
                    for row in rows:
                        columns = ", ".join(row.keys())
                        placeholders = ", ".join("?" * len(row))
                        sql = "INSERT INTO {} ({}) VALUES ({})".format(
                            table_name, columns, placeholders
                        )
                        values = [
                            int(x) if x.isnumeric() else x
                            for x in row.values()
                        ]
                        cur.execute(sql, values)
                print(f"  Importing data from file {j}... OK")

        con.commit()
        con.close()

        print()
        print("======================================")
        print("The all data from .csv-files are imported.")
        print()
