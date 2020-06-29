# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class MaoyancrawlerPipeline:
    def __init__(self):
        self.file = open('./spider_movie.csv', 'w', newline='')
        self.csv_writer = csv.writer(self.file)
        self.csv_writer.writerow(['影片名称', '电影类型', '上映时间'])

    def process_item(self, item, spider):
        self.csv_writer.writerow([item["name"], item["type"], item["time"]])
        return item

    def close_spider(self, spider):
        self.file.close()
