from second.items import SecondItem
from typing import ItemsView
# We need this so that Python knows about the item object

import scrapy

class dSpyder(scrapy.Spider):
    name = 'd'
    start_urls = {
        'https://www.99acres.com/residential-land-in-udaipur-ffid',
        'https://www.99acres.com/residential-land-in-udaipur-ffid-page-2',
        'https://www.99acres.com/residential-land-in-udaipur-ffid-page-3',
        'https://www.99acres.com/residential-land-in-udaipur-ffid-page-4' , 
        'https://www.99acres.com/residential-land-in-udaipur-ffid-page-5',
        'https://www.99acres.com/residential-land-in-udaipur-ffid-page-6',
        'https://www.99acres.com/residential-land-in-udaipur-ffid-page-7',
        'https://www.99acres.com/residential-land-in-udaipur-ffid-page-8',
        'https://www.99acres.com/residential-land-in-udaipur-ffid-page-12',
        'https://www.99acres.com/residential-land-in-udaipur-ffid-page-13'
        }
        


    def parse(self,response):
        items = SecondItem()

        url = response.xpath('//*[@id="srp_tuple_property_title"]/@href').extract()
        
        urls = []
        for  a  in url:
            
            p = 'https://www.99acres.com' + a 
            urls.append(p)

        for i in urls :
            
            yield scrapy.Request( i , callback = self.parseInnerpage)

    def parseInnerpage(self , response):
        items = SecondItem()
        price = response.xpath('//*[@id="pdPrice2"]/text()').extract()
        price_per = response.xpath('//*[@id="FactTableComponent"]/tr/td[2]/div[2]/text()').extract()
        plot_area = response.xpath('//*[@id="factArea"]/span[2]/text()').extract()
        address = response.xpath('//*[@id="FactTableComponent"]/tr[2]/td[1]/div[2]/text()').extract()
        allowed_floors = response.xpath('//*[@id="floorNumLabel"]/text()').extract()
        boundary_walls = response.xpath('//*[@id="Is_Boundary_Wall_Made_Label"]/text()').extract()
        width_facing_road = response.xpath('//*[@id="Width_Of_Facing_Road"]/text()').extract()
        tranjection_type = response.xpath('//*[@id="Transact_Type_Label"]/text()').extract()

        price_per = price_per[2].replace('@','')

        items['price'] = price
        items['price_per'] = price_per
        items['plot_area'] = plot_area
        items['address']  = address
        items['allowed_floors'] = allowed_floors
        items['boundary_walls'] = boundary_walls
        items['width_facing_road'] = width_facing_road
        print(tranjection_type)

        yield items