# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import datetime

from itemadapter import ItemAdapter

import os
import configparser
from week02.proxy_crawler.proxy_crawler.utils.DB import SQLManager

cp = configparser.ConfigParser()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_file = os.path.join(BASE_DIR, 'DB_config', 'setting.cfg')
if os.path.exists(config_file):
    cp.read(config_file)
    config = cp.items('mysql')
else:
    raise FileNotFoundError('未发现配置文件！~ {}'.format(config_file))

class ProxyCrawlerPipeline:
    def process_item(self, item, spider):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql = "INSERT INTO `moives` ( `name`,`type`,`release_time`, `created_time`, `updated_time`) VALUES (%s, %s, %s , %s, %s)"
        values = (item['name'], item['type'], item['time'], now, now)

        db = SQLManager(dict(config))
        try:
            db.moddify(sql, values)
        except Exception as e:
            print(e)
        return item
