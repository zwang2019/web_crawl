# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3
from my_credentials import DB_PATH

class MyscrapyPipeline:

    def __init__(self):
        self.crawler = None
        self.spider = None

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        pipeline.crawler = crawler
        return pipeline

    def open_spider(self):
        """
        Execute before spider start. Connect to database and create table if not exist
        :param spider:
        :return:
        """
        self.spider = self.crawler.spider
        if self.spider.name == 'douban':

            self.conn = sqlite3.connect(DB_PATH)
            self.cursor = self.conn.cursor()

            sql_create_table = """
            CREATE TABLE IF NOT EXISTS douban_top_250 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title_cn TEXT NOT NULL,
            title_foreign TEXT,
            title_other TEXT,
            director TEXT,
            cast TEXT,
            year INTEGER,
            country TEXT,
            genre TEXT,
            rating REAL,
            reviews INTEGER,
            quotation TEXT,
            link_url TEXT NOT NULL UNIQUE,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);
            """
            try:
                self.cursor.execute(sql_create_table)
                self.conn.commit()
                print("douban_top_250 table created successfully.")
            except Exception as e:
                self.conn.rollback()
                print(f"Error creating table: {e}")


    def process_item(self, item):

        insert_sql = """
            INSERT INTO douban_top_250 (title_cn, title_foreign, title_other, director, cast, year, country, genre, rating, reviews, quotation, link_url)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(link_url)
            DO UPDATE SET 
                title_cn      = excluded.title_cn,
                title_foreign = excluded.title_foreign,
                title_other   = excluded.title_other,
                director      = excluded.director,
                cast          = excluded.cast,
                year          = excluded.year,
                country       = excluded.country,
                genre         = excluded.genre,
                rating        = excluded.rating,
                reviews       = excluded.reviews,
                quotation     = excluded.quotation,
                updated_at    = CURRENT_TIMESTAMP;
            """

        return item


    def close_spider(self):
        """
        Execute after spider close
        :param spider:
        :return:
        """


        pass