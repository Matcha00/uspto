# -*- coding: utf-8 -*-




#import scrapy
#from scrapy.linkextractors import LinkExtractor
#from scrapy.spiders import CrawlSpider,Rule

#from uspto.items import UsptoItem

#class Uspto(CrawlSpider):
    #name = 'uspto'
    #allowed_domains = ['www.uspto.gov']
    #start_url = ["http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1&u=%2Fnetahtml%2FPTO%2Fsearch-bool.html&r=0&f=S&l=50&TERM1=led&FIELD1=&co1=AND&TERM2=&FIELD2=&d=PTXT",]
    #rules = (Rule(LinkExtractor(allow='http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=d{1,6}&f=G&l=50&d=PTXT&p=1&S1=led&OS=led&RS=led',),callback= 'parse_item',follow= True))
    #rules = (Rule(LinkExtractor(allow='',allow_domains='http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=1&f=G&l=50&d=PTXT&p=1&S1=led&OS=led&RS=led'),callback= 'parse_item',follow=True))

    #start_url = ['http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=1&f=G&l=50&d=PTXT&p=1&S1=led&OS=led&RS=led']
    #def parse_item(self,response):
        #print(response.url)
    # allowed_domains = ['mzitu.com']
    # start_urls = ['http://www.mzitu.com/']
    # img_urls = []
    # rules = (
    #     Rule(LinkExtractor(allow=('http://www.mzitu.com/\d{1,6}',), deny=('http://www.mzitu.com/\d{1,6}/\d{1,6}')),
    #          callback='parse_item', follow=True),
    # )

    #def parse_item(self, response):
       # print(response.url)

import scrapy
from pip.utils import logging
from scrapy.http import Request

from uspto.items import UsptoItem

keyword = ''

'''To obtain keyword'''

'''Incoming url start the scrapy crawle'''
class Uspto(scrapy.Spider):
    name = 'uspto'
    #allowed_domains = ['http://patft.uspto.gov/']
    #start_url = 'http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1&u=%2Fnetahtml%2FPTO%2Fsearch-bool.html&r=0&f=S&l=50&TERM1=water&FIELD1=&co1=AND&TERM2=&FIELD2=&d=PTXT'

    allowed_domains = ["http://patft.uspto.gov"]
    keyword = input("ssss:")
    search_url = 'http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1&u=%2Fnetahtml%2FPTO%2Fsearch-' \
                  'bool.html&r=0&f=S&l=50&TERM1=' + keyword + '&FIELD1=&co1=AND&TERM2=&FIELD2=&d=PTXT'

    start_urls = [
        #"http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1&u=%2Fnetahtml%2FPTO%2Fsearch-bool.html&r=0&f=S&l=50&TERM1=python&FIELD1=&co1=AND&TERM2=&FIELD2=&d=PTXT",
        search_url,
        #'http: // patft.uspto.gov / netacgi / nph - Parser?Sect1 = PTO2 & Sect2 = HITOFF & p = 1 & u = % 2Fnetahtml % 2FPTO % 2Fsearch - bool.html & r = 0 & f = S & l = 50 & TERM1 = Vertical + lift + UAV & FIELD1 = & co1 = AND & TERM2 = & FIELD2 = & d = PTXT'
        #'http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1&u=%2Fnetahtml%2FPTO%2Fsearch-bool.html&r=0&f=S&l=50&TERM1=Vertical+lift+UAV&FIELD1=&co1=AND&TERM2=&FIELD2=&d=PTXT',


    ]


    # def search_word(self):
    #     keywords = list()
    #     while True:
    #         print('what do you want to do?(a: add a key word for searching, q:quit adding words and start)')
    #         command = input('command:')
    #         if command == 'a':
    #             word = input('keyword: ')
    #             if word not in keywords:
    #                 keywords.append(word)
    #         elif command == 'q':
    #             break
    #         else:
    #             print('please input a valid command')
    #     if len(keywords) == 0:
    #         return
    #     search_string = ''
    #     for keyword in keywords:
    #         search_string += keyword
    #         search_string += '+'
    #     search_string = search_string[:-1]
    #     return search_string

    #def start_requests(self):
        # keywords = list()
        # while True:
        #     print('what do you want to do?(a: add a key word for searching, q:quit adding words and start)')
        #     command = input('command:')
        #     if command == 'a':
        #         word = input('keyword: ')
        #         if word not in keywords:
        #             keywords.append(word)
        #     elif command == 'q':
        #         break
        #     else:
        #         print('please input a valid command')
        # if len(keywords) == 0:
        #     return
        # search_string = ''
        # for keyword in keywords:
        #     search_string += keyword
        #     search_string += '+'
        # search_string = search_string[:-1]
        #
        #base_url = 'http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1&u=%2Fnetahtml%2FPTO%2Fsearch-bool.html&r=0&f=S&l=50&TERM1='
        #last_url = '&FIELD1=&co1=AND&TERM2=&FIELD2=&d=PTXT'
        #keywrd = self.test()

        #scrapy.Request(keywrd,callback=self.parse)




    def parse(self, response):
        #print(response.text)

        # test = response.xpath('/html/body/table//tr/td[last()]/a/@href')
        # print(test)

        for href in response.xpath('/html/body/table//tr/td[last()]/a/@href'):

            url_href = href.extract()

            print("xpath", url_href)

            url = 'http://patft.uspto.gov' + url_href
            #logging.info("hh",url)
            #print("chenhuan",url)

            yield scrapy.Request(url,callback=self.parse_show,dont_filter=True)

            next_page = response.xpath('/html/body/form[1]/@action').extract()
            sect1_name = response.xpath('/html/body/form[1]/input[1]/@value').extract()
            sect2_name = response.xpath('/html/body/form[1]/input[2]/@value').extract()
            u_name = response.xpath('/html/body/form[1]/input[3]/@value').extract()
            r_name = response.xpath('/html/body/form[1]/input[4]/@value').extract()
            f_name = response.xpath('/html/body/form[1]/input[5]/@value').extract()
            l_name = response.xpath('/html/body/form[1]/input[6]/@value').extract()
            d_name = response.xpath('/html/body/form[1]/input[7]/@value').extract()
            os_name = response.xpath('/html/body/form[1]/input[8]/@value').extract()
            rs_name = response.xpath('/html/body/form[1]/input[9]/@value').extract()
            query_name = response.xpath('/html/body/form[1]/input[10]/@value').extract()
            td_name = response.xpath('/html/body/form[1]/input[10]/@value').extract()
            srch1_name = response.xpath('/html/body/form[1]/input[10]/@value').extract()
            list_name = response.xpath('/html/body/form[1]/input[11]/@name').extract()
            next_name = response.xpath('/html/body/form[1]/input[last()]/@value').extract()
            next_list = response.xpath('/html/body/form[1]/input[last()]/@name').extract()

            #print(next_page[0])

            #print(next_name,sect1_name,sect2_name,u_name,r_name,f_name,l_name,d_name,os_name,rs_name,query_name,td_name,srch1_name)

            if next_page[0]:
                url_next = 'http://patft.uspto.gov' + next_page[0] + '?Sect1=' + sect1_name[0] + '&Sect2=' + sect2_name[0] + '&u=' + u_name[0] + '&r=' + r_name[0] + '&f=' + f_name[0] + '&l=' + l_name[0] + '&d=' + d_name[0] + '&OS=' + os_name[0] + '&RS=' + rs_name[0] + '&Query=' + query_name[0] + '&TD=' + td_name[0] + '&Srch1=' + srch1_name[0] + '&' + next_list[0] + '=' + next_name[0]
                print(url_next)
                yield scrapy.Request(url_next,callback=self.parse,dont_filter=True)

            else:
                print('There is no page')

    def parse_show(self,response):
        # us_patent_id = scrapy.Field()
        #  = scrapy.Field()
        #  = scrapy.Field()
        #  = scrapy.Field()
        #  = scrapy.Field()
        #  = scrapy.Field()
        #  = scrapy.Field()
        #  = scrapy.Field()
        #  = scrapy.Field()
        #  = scrapy.Field()
        #  = scrapy.Field()
        #  = scrapy.Field()
        #  = scrapy.Field()
        #  = scrapy.Field()
        #  = scrapy.Field()
        #  = scrapy.Field()
        #  = scrapy.Field()
        #  = scrapy.Field()
        #  = scrapy.Field()
        # claims = scrapy.Field()
        # description = scrapy.Field()

        item = UsptoItem()

        item['us_patent_id'] = response.xpath('/html/body/table[2]/tr[1]/td[2]/b/text()').extract()
        item['galle_et_al'] = response.xpath('/html/body/table[2]/tr[2]/td[2]/b/text()').extract()
        ad = response.xpath('/html/body/p[1]/text()').extract()
        while "\n" in ad:
            ad.remove("\n")
        item['abstract'] = ad
        #item['inventors'] =  response.xpath('/html/body/table[3]/tr[1]/td[1]/text()|/html/body/table[3]/tr[1]/td[1]/b/text()').extract()
        data = response.xpath('/html/body/table[3]/tr[1]/td[1]|/html/body/table[3]/tr[1]/td[1]/b')
        info = data.xpath('string(.)').extract()[0]
        item['inventors'] = info

        #item['applicant'] = response.xpath('/html/body/table[3]/tr[2]/td/table/tr[2]/td[1]/b/text()').extract()
        #item['name'] = response.xpath().extract('/html/body/table[3]/tr[2]/td/table/tr[2]/td[2]/b/text()')
        # item['city'] = response.xpath('/html/body/table[3]/tr[2]/td/table/tr[2]/td[3]/text()').extract()
        # item['state_country_type'] = response.xpath('/html/body/table[3]/tr[2]/td/table/tr[2]/td[4]/text()').extract()
        # item['assignee'] = response.xpath('/html/body/table[3]/tr[3]/td/b/text()').extract()
        item['family_id'] = response.xpath('/html/body/table[3]/tr[last()-2]/td/b/text()').extract()
        item['appl_no'] = response.xpath('/html/body/table[3]/tr[last()-1]/td/b/text()').extract()
        item['filed'] = response.xpath('/html/body/table[3]/tr[last()]/td/b/text()').extract()
        # item['document_identifier'] = response.xpath('/html/body/table[4]/tr[3]/td[2]/text()').extract()
        # item['publication_date'] = response.xpath('/html/body/table[4]/tr[3]/td[3]/text()').extract()
        # # item['current_us_class']
        # # item['current_cpc_class']
        # # item['current_international_class']
        # # item['field_of_search']
        # # item['other_references']

        #print(item)

        yield  item


# def get_kw_url(kw):
#     """concatenate the url for searching"""
#
#     base_url = 'http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1&u=%2Fnetahtml%2FPTO%2Fsearch-bool.html&r=0&f=S&l=50&TERM1='
#     last_url = '&FIELD1=&co1=AND&TERM2=&FIELD2=&d=PTXT'
#     return base_url + kw + last_url



    # str = search_url


def test():
    keywords = list()
    while True:
        print('what do you want to do?(a: add a key word for searching, q:quit adding words and start)')
        command = input('command:')
        if command == 'a':
            word = input('keyword: ')
            if word not in keywords:
                keywords.append(word)
        elif command == 'q':
            break
        else:
            print('please input a valid command')
    if len(keywords) == 0:
        return
    search_string = ''
    for keyword in keywords:
        search_string += keyword
        search_string += '+'
    search_string = search_string[:-1]
    print(search_string)

    search_url = 'http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1&u=%2Fnetahtml%2FPTO%2Fsearch-' \
                 'bool.html&r=0&f=S&l=50&TERM1=' + search_string + '&FIELD1=&co1=AND&TERM2=&FIELD2=&d=PTXT'

    return search_url
    print(search_url)



