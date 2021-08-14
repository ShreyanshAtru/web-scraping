# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SecondItem(scrapy.Item):
    # define the fields for your item here like:
    price = scrapy.Field()
    price_per = scrapy.Field()
    plot_area = scrapy.Field()
    address = scrapy.Field()
    allowed_floors = scrapy.Field()
    boundary_walls = scrapy.Field()
    tranjection_type = scrapy.Field()
    width_facing_road = scrapy.Field()
    about_property = scrapy.Field()

    
