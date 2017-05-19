# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UsptoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    us_patent_id = scrapy.Field()
    galle_et_al = scrapy.Field()
    abstract = scrapy.Field()
    inventors = scrapy.Field()
    applicant = scrapy.Field()
    name = scrapy.Field()
    city = scrapy.Field()
    state_country_type = scrapy.Field()
    assignee = scrapy.Field()
    family_id = scrapy.Field()
    appl_no = scrapy.Field()
    filed = scrapy.Field()
    document_identifier = scrapy.Field()
    publication_date = scrapy.Field()
    current_us_class = scrapy.Field()
    current_cpc_class = scrapy.Field()
    current_international_class = scrapy.Field()
    field_of_search = scrapy.Field()
    other_references = scrapy.Field()
    claims = scrapy.Field()
    description = scrapy.Field()

    pass
