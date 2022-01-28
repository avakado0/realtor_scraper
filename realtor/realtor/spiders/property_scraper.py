import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class FirstSpider(scrapy.Spider):
    name = 'property_scraper'
    allowed_domains = ['realtor.com']
    start_urls = ['http://realtor.com/realestateandhomes-search/Florida/']
    header = {
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language' :	'en-US,en;q=0.5',
        'Connection' : 	'keep-alive',
        'Host' : 'www.realtor.com',
        #'Cookie': 'split=n; split_tcv=195; __vst=94f2c248-6517-4606-b849-57cf91ebb41a; __ssn=f3c440a0-0388-4f6b-af89-b6a3cf289937; __ssnstarttime=1642982534; permutive-id=76414d15-def7-4a17-8f22-b019a4ff7a8e; criteria=pg%3D3%26sprefix%3D%252Frealestateandhomes-search%26area_type%3Dstate%26search_type%3Dstate%26state%3DFlorida%26state_code%3DFL%26state_id%3DFL%26lat%3D28.4770636835453%26long%3D-82.4664217915869%26loc%3DFlorida%26locSlug%3DFlorida; user_activity=return; last_ran=-1; last_ran_threshold=1642990010334; _ncg_sp_id.cc72=bf055c38-baa5-4651-80d9-4de65c53bd37.1642982539.3.1642989972.1642985409.cd82cfd0-2f96-4592-8ee9-43780c74ab97; _ncg_id_=bf055c38-baa5-4651-80d9-4de65c53bd37; ab.storage.userId.7cc9d032-9d6d-44cf-a8f5-d276489af322=%7B%22g%22%3A%22visitor_94f2c248-6517-4606-b849-57cf91ebb41a%22%2C%22c%22%3A1642982540550%2C%22l%22%3A1642982540550%7D; ab.storage.sessionId.7cc9d032-9d6d-44cf-a8f5-d276489af322=%7B%22g%22%3A%224d66f6d1-caac-e4ea-f567-3b5d9547ec50%22%2C%22e%22%3A1642991811242%2C%22c%22%3A1642987494821%2C%22l%22%3A1642990011242%7D; ab.storage.deviceId.7cc9d032-9d6d-44cf-a8f5-d276489af322=%7B%22g%22%3A%2240beb7c0-db54-a471-fbfa-be5ce906b40a%22%2C%22c%22%3A1642982540553%2C%22l%22%3A1642982540553%7D; G_ENABLED_IDPS=google; __split=68; __gads=ID=6353e9a2e192dfaf-2212ec2229cd00f6:T=1642982546:S=ALNI_MZ49kA2QRzGk-VhjxgHFthkh5VBkw; __qca=P0-529999605-1642982546786; pxcts=ecd72b44-7ca8-11ec-b689-4b754a584b79; _pxvid=ecd72284-7ca8-11ec-b689-4b754a584b79; AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=-1124106680%7CMCIDTS%7C19017%7CMCMID%7C73160622265833697612445793733711854529%7CMCAAMLH-1643594616%7C6%7CMCAAMB-1643594616%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1642997016s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19024%7CvVersion%7C5.2.0; _gcl_au=1.1.1974984548.1642982553; _tac=false~self|not-available; _ta=us~1~89df68bc35032d48c293adce8574aa42; QSI_HistorySession=https%3A%2F%2Fwww.realtor.com%2Frealestateandhomes-search%2FFlorida~1642982553260%7Chttps%3A%2F%2Fwww.realtor.com%2Frealestateandhomes-search%2FFlorida%2Fpg-2~1642987514540%7Chttps%3A%2F%2Fwww.realtor.com%2Frealestateandhomes-search%2FFlorida%2Fpg-2%3FabButtonId%3D0~1642988172697%7Chttps%3A%2F%2Fwww.realtor.com%2Frealestateandhomes-search%2FFlorida~1642989819297; _px3=ca1a4e8068bcbf615de13c1fbe751980610ab826b520fc71bd352aaebd7e880f:SAzR7XY3fXA4t1vn/Mg2mTgUimdAgTB/sAAtbsRszjnjchIQropFFHI5GV9xgPDcGm9Y5wXxwBSfL05TVPDkyw==:1000:z6nAfMu0TzN6R2Yxob4H6y4K2DtHelnBgFBIRdhAEPIlNdx7OsgZIGXw2xbjUuBE1VMu/3rLG419Echzbhu2TOEFhB8gGdgmS2oGYxJQ9BV/b21r4FsPMZP/FzA7e7BLvhiN3Y94NGFDGp/dorrnXu1ZtZfJj5iC7fdJVRfTVTy0YKugylusoc+z/nhtS+Nr1gZ4+5mYbtgvUuuJ2WUOYA==; AMCV_AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=-1124106680%7CMCIDTS%7C19017%7CMCMID%7C04907200327180252485109892508390083644%7CMCOPTOUT-1642994715s%7CNONE%7CvVersion%7C5.2.0; AMCVS_8853394255142B6A0A4C98A4%40AdobeOrg=1; _fbp=fb.1.1642982554932.493741030; _ga=GA1.2.152867385.1642982547; _gid=GA1.2.1378567015.1642982555; ajs_anonymous_id=%22ad9809e9-b85d-40bc-96f6-3cac89973e77%22; s_ecid=MCMID%7C73160622265833697612445793733711854529; AMCVS_AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=1; adcloud={%22_les_v%22:%22y%2Crealtor.com%2C1642991777%22}; _lr_geo_location=TR; cto_bundle=li5T6l8zRmhSRVRqVDdNYk43bUlFVEdDRDBVWGVkemJmRiUyQlZMcUYlMkZHUk94bzRCYUJKVnVIWVdoWGllbTBBcXdsOVZaNWYlMkJGcFpmY096YUJLdjEyVENjM29JbnpJOHkzcGxSWkFObEFPeFAzUkhoQUtvMGt1TnNNT1lKZGlaWlNYRTVtb3N0dXpYanVlWEpQcHZwTFJlbnRyZUElM0QlM0Q; g_state={"i_p":1642989895214,"i_l":1}; _ncg_sp_ses.cc72=*; srchID=9426b5058473402fae881645f77d810f; _tas=b7zkzhch1w7; _gat=1; _uetsid=ef2846b07ca811ec87ed0574d5baa474; _uetvid=ef2852d07ca811ec8a34c167bbc22db5; _pxff_bdd=2000; _pxff_cde=5,10',
        'If-None-Match': "dea13-cMxOHgWfbT7yRh61e76KizB2j48",
        'Referer': 'https://www.realtor.com/realestateandhomes-search/Florida/pg-3',
        
    }
    def parse(self, response):
        data = response.xpath('//li[@data-testid="result-card"]')
        
        next_page_part = response.xpath('//a[@aria-label="Go to next page"]/@href').get()
                    
        for property in data:
            price = property.xpath('.//span[@data-label="pc-price"]/text()').get()
            addr1= property.xpath('.//div[@data-label="pc-address"]/text()').get()
            addr2= property.xpath('.//div[@data-label="pc-address-second"]/text()').get()

            yield {
                'price':price,
                'address1' :addr1,
                'address2' :addr2
                }
        if next_page_part:
            print("....sonraki sayfa açılıyor...")
            next_page = response.urljoin(next_page_part)
            yield scrapy.Request(next_page,callback=self.parse,headers=self.header,dont_filter=True)

            
        
        
        
        
