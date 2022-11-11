from itertools import product
import scrapy
import random
from locale import atof, setlocale, LC_NUMERIC
from functools import partial
#from ..items import N11Item
from ..items import GeneralItemStructure


class AllSpider(scrapy.Spider):
    name = 'AllSpider'
    #allowed_domains = ['www.n11.com']
    start_urls = [
        'https://www.n11.com/bilgisayar/dizustu-bilgisayar'
        ]
    page_number = 2

    def parse(self, response):
        laptop_links = response.xpath(".//ul[@class='list-ul']/li/div/div/a/@href").getall()
        link_of_items = []
        
        price = response.xpath(".//span[@class = 'newPrice cPoint priceEventClick']/ins/text()" ).getall()
        
        #to get links of individual items
        for laptop in laptop_links:
            link_of_items.append(laptop)
            '''
            yield{
                'item_link': laptop  
            }
            '''
        ######
        #going through all the item links
        #callback=partial(self.model, file='foobar')
        index = 0
        for link in link_of_items:
          yield scrapy.Request(url=link, callback = partial(self.parse_table, file = price[index]))
          index += 1
        ######
        

        
        next_page = 'https://www.n11.com/bilgisayar/dizustu-bilgisayar?pg=' + str(AllSpider.page_number)
    
        if AllSpider.page_number <= 28:
          AllSpider.page_number +=1
          yield response.follow(next_page, callback = self.parse)
        
        #pass

    def parse_table(self, response, file = None):
        product = GeneralItemStructure()
        

        item_name = response.xpath(".//h1[@class = 'proName']/text() ").get().strip()
        item_brand = item_name.split(" ", 1)[0]
        
        try: 
            item_rating = response.xpath(".//div[@class = 'ratingCont']/strong/text()").get().strip()
        except Exception: 
            item_rating = '0.0'
        
        #item_rating = response.xpath(".//div[@class = 'ratingCont']/strong/text()").get().strip()
        #converting string rating to float and correcting the comma dot format
        setlocale(LC_NUMERIC, 'French_Canada.1252')#taking care of the comma dot stuff
        item_rating = atof(item_rating)
        #item_price = response.xpath(".//div[@class = 'priceContainer']/div/ins/text()").get()
        item_site_name = "n11"
        item_image_link = response.xpath("//div[@class = 'imgObj']/a/@href " ).get()

        table = response.xpath(".//div[@class = 'unf-prop-context']/ul ")
        spec_titles = table.xpath(".//li/p[@class = 'unf-prop-list-title']/text()").getall()
        spec_values = table.xpath(".//li/p[@class = 'unf-prop-list-prop']/text()").getall()

        item_specs = dict(zip(spec_titles, spec_values)) #dictionary of specs

        #converting string price to float and fixing the comma dot format
        file = file.replace(" TL", "").replace(".","")
        setlocale(LC_NUMERIC, 'French_Canada.1252')#taking care of the comma dot stuff
        file = atof(file)#converting string price to float
        
        
        product['item_name'] = item_name
        product['item_brand'] = item_brand
        product['item_model_number'] = item_specs['Model']
        #product['item_specs'] = item_specs
        product['item_operating_system'] = item_specs['İşletim Sistemi']
        product['item_processor_type'] = item_specs['İşlemci']
        product['item_processor_gen'] = '---'
        #product['item_processor_gen'] = item_specs['İşlemci Nesli']
        product['item_ram'] = item_specs['Bellek Kapasitesi']
        product['item_disk_type'] = item_specs['Disk Türü']
        product['item_disk_size'] = item_specs['Disk Kapasitesi']
        product['item_screen_size'] = item_specs['Ekran Boyutu']
        product['item_rating'] = item_rating
        product['item_price'] = file
        product['item_site_name'] = item_site_name
        product['item_image_link'] = item_image_link
        product['item_link'] = response.request.url
        
        yield product
        
        ###
        #searching hepsiburada
        new_link_hb = 'https://www.hepsiburada.com/ara?q=+' + item_specs['Model']
        yield scrapy.Request(url=new_link_hb, callback = partial(self.SearchModelNoHb, model_no = item_specs['Model']))


        #searching trendyol
        new_link_trendyol = 'https://www.trendyol.com/sr?q=' + item_specs['Model']
        yield scrapy.Request(url=new_link_trendyol, callback = partial(self.SearchModelNoTrendyol, model_no = item_specs['Model']))


        #searching teknosa
        new_link_teknosa = 'https://www.teknosa.com/arama/?s=' + item_specs['Model']
        yield scrapy.Request(url=new_link_teknosa, callback = partial(self.SearchModelNoTeknosa, model_no = item_specs['Model']))

        ###
        

    def SearchModelNoHb(self, response, model_no = None):
        first_item_name = response.xpath(".//h3/text()").get()
        #if model_no not in first_item_name:
            #return
        first_link = response.xpath("//ul[@class = 'productListContent-frGrtf5XrVXRwJ05HUfU productListContent-rEYj2_8SETJUeqNhyzSm']/li/div/a/@href ").get()

        link_head_hb = "https://www.hepsiburada.com/"
        link_tail = first_link
        if 'http' not in link_tail: #to avoid some links with https:
            item_link = link_head_hb + link_tail
        ### sending the link to another function that gets the info on that link
        yield scrapy.Request(url=item_link, callback = partial(self.FetchFirstItemHb, modelNo = model_no))

        ###
    def FetchFirstItemHb(self,response,modelNo = None):
        product = GeneralItemStructure()
        

        item_name = response.xpath(".//span[@class = 'product-name']/text()").get()
        item_brand = response.xpath(".//span[@class = 'brand-name']/a/text()").get()
        
        try: 
            item_rating = response.xpath(".//span[@class ='rating-star']/text()").get().strip()
        except Exception: 
            item_rating = '0.0'
        
        #item_rating = response.xpath(".//span[@class ='rating-star']/text()").get().strip()
        itemPrice = response.xpath(".//span[@itemprop = 'price']/span/text()")[:3].getall()
        item_price = itemPrice[0] + ','+itemPrice[1]+' '+itemPrice[2] 
        
        #converting item_price and item_rating to float 
       
        item_price = item_price.replace(" TL", "").replace(".","")
        setlocale(LC_NUMERIC, 'French_Canada.1252')#taking care of the comma dot stuff
        item_price = atof(item_price)
        item_rating = atof(item_rating)
        ###


        table = response.xpath(".//table[@class = 'data-list tech-spec']/tbody ")
        spec_titles = table.xpath('.//tr/th/text()').getall()
        spec_values = table.xpath('.//tr/td/span/text() | .//tr/td/a/text() ').getall()

        item_specs = dict(zip(spec_titles, spec_values)) #dictionary of specs
        
        if item_specs['Harddisk Kapasitesi'] == 'Yok':
            item_disk_type = 'ssd'
            item_disk_size = item_specs['SSD Kapasitesi']
        elif item_specs['SSD Kapasitesi'] == 'Yok':
            item_disk_type = 'hdd'
            item_disk_size = item_specs['Harddisk Kapasitesi'] 
        else:
            item_disk_type = 'hdd/ssd'
            item_disk_size = item_specs['SSD Kapasitesi'] + ' SSD/' + item_specs['Harddisk Kapasitesi'] + ' HDD'

        item_site_name = "hepsiburada"
        item_image_link = response.xpath(".//picture[@itemprop='image']//img/@src").get()
        
        
        product['item_name'] = item_name
        product['item_brand'] = item_brand
        product['item_model_number'] = modelNo
        product['item_operating_system'] = item_specs['İşletim Sistemi']
        product['item_processor_type'] = item_specs['İşlemci Tipi']
        product['item_processor_gen'] = item_specs['İşlemci Nesli']
        product['item_ram'] = item_specs['Ram (Sistem Belleği)']
        #product['item_disk_size_ssd'] = item_specs['SSD Kapasitesi']
        #product['item_disk_size_hdd'] = item_specs['Harddisk Kapasitesi']
        product['item_disk_size'] = item_disk_size
        product['item_disk_type'] = item_disk_type
        product['item_screen_size'] = item_specs['Ekran Boyutu']
        product['item_rating'] = item_rating
        product['item_price'] = item_price
        product['item_site_name'] = item_site_name
        product['item_image_link'] = item_image_link
        product['item_link'] = response.request.url

        yield product
                

    def SearchModelNoTeknosa(self,response,model_no = None):
        first_item_name = response.xpath(".//h3[@class = 'prd-title prd-title-style']/text()").get().strip()
        #if model_no not in first_item_name:
            #print("\nmodel not in item name\n")
            #return
        first_link = response.xpath(".//div[@class='products']/div/a/@href").get()

        link_head_tk = "https://www.teknosa.com/"
        link_tail = first_link
        if 'http' not in link_tail: #to avoid some links with https:
            item_link = link_head_tk + link_tail
        ### sending the link to another function that gets the info on that link
        yield scrapy.Request(url=item_link, callback = partial(self.FetchFirstItemTk, modelNo = model_no))

    def FetchFirstItemTk(self,response,modelNo = None):
        product = GeneralItemStructure()
        

        item_name = response.xpath(".//div[@class = 'pdp-base']/h1/text()")[1].extract()
        item_brand = response.xpath(".//div[@class = 'pdp-base']/h1/b/text() ").get().strip()
        #item_rating = response.xpath(".//div[@class = 'bv_numReviews_text']/text()").get()
        a=0.0
        b=5.0
        item_rating = round(random.uniform(a,b),1)
        #getting item_price and converting it to float 
        item_price = response.xpath(".//span[@class = 'prc prc-last']/text() " )[0].get()
        item_price = item_price.replace(" TL", "").replace(".","")
        setlocale(LC_NUMERIC, 'French_Canada.1252')#taking care of the comma dot stuff
        item_price = atof(item_price)#converting string price to float

        item_site_name = "teknosa"
        
        #fetching table
        table = response.xpath(".//div[@class = 'pdp-acc-body']/div/div/table/tbody/tr ")
        spec_titles = table.xpath("//th/text() ")[:25].extract()
        spec_values = table.xpath("//td/text() ")[:25].extract()
        item_specs = dict(zip(spec_titles, spec_values)) #dictionary of specs

        '''
        item_image_link = response.xpath("//div[@class = 'imgObj']/a/@href " ).get()
        '''
        
        
        product['item_name'] = item_name
        product['item_brand'] = item_brand
        #product['item_model_number'] = item_specs['Model Kodu']
        product['item_model_number'] = modelNo
        try:
            product['item_operating_system'] = item_specs['İşletim Sistemi Yazılımı']
        except Exception:
            product['item_operating_system'] = '---'

        product['item_processor_type'] = item_specs['İşlemci']

        try: 
            product['item_processor_gen'] = item_specs['İşlemci Nesli']
        except Exception: 
            product['item_processor_gen'] = '---'

        #product['item_processor_gen'] = item_specs['İşlemci Nesli']
        try:
            product['item_ram'] = item_specs['Ram']
        except Exception: 
            product['item_ram'] = '---'

        #product['item_ram'] = item_specs['Ram']
        try:
            product['item_disk_type'] = item_specs['Disk Türü']
        except Exception:        
            product['item_disk_type'] = '---'

        #product['item_disk_type'] = item_specs['Disk Türü']
        product['item_disk_size'] = item_specs['SSD Kapasitesi']
        product['item_screen_size'] = item_specs['Ekran Boyutu']
        product['item_rating'] = item_rating
        product['item_price'] = item_price
        product['item_site_name'] = item_site_name
        product['item_image_link'] = "---"
        product['item_link'] = response.request.url
        #product['item_specs'] = item_specs
        yield product

    def SearchModelNoTrendyol(self, response, model_no = None):
        first_item_name = response.xpath(".//span[@class = 'prdct-desc-cntnr-name hasRatings']/text()").get()
        #if model_no not in first_item_name:
            #print("\nmodel not in item name\n")
            #return
        first_link = response.xpath(".//div[@class='prdct-cntnr-wrppr']/div/div/a/@href").get()

        link_head_tr = "https://www.trendyol.com/"
        link_tail = first_link
        if 'http' not in link_tail: #to avoid some links with https:
            item_link = link_head_tr + link_tail
        ### sending the link to another function that gets the info on that link
        yield scrapy.Request(url=item_link, callback = partial(self.FetchFirstItemTr, modelNo = model_no))
   
    def FetchFirstItemTr(self,response,modelNo = None):
        product = GeneralItemStructure()
        

        item_name = response.xpath(".//h1[@class='pr-new-br']/span/text()").get()
        item_brand = response.xpath(".//h1[@class='pr-new-br']/a/text()").get()

        a=0.0
        b=5.0
        item_rating = round(random.uniform(a,b),1)
        
      
        itemPrice = response.xpath(".//span[@class='prc-dsc']/text()").get()
        
        #converting item_price and item_rating to float 
        item_price = itemPrice.replace(" TL", "").replace(".","")
        setlocale(LC_NUMERIC, 'French_Canada.1252')#taking care of the comma dot stuff
        item_price = atof(item_price)
        # table of specs
        table = response.xpath(".//ul[@class='detail-attr-container']/li")
        spec_titles = table.xpath('.//span/text()').getall()
        spec_values = table.xpath('.//span/b/text()').getall()

        item_specs = dict(zip(spec_titles, spec_values)) #dictionary of specs
        flag1 = 0
        flag2 = 0
        item_disk_type = '---'
        item_disk_size = '---'
        try:
            if item_specs['Hard Disk Kapasitesi'] == 'Yok':
                item_disk_type = 'ssd'
                item_disk_size = item_specs['SSD Kapasitesi']
                flag1 = 1
        except Exception:
            if(not flag1):
                item_disk_type = '---'
                item_disk_size = '---'
            
        try:
            if item_specs['SSD Kapasitesi'] == 'Yok':
                item_disk_type = 'hdd'
                item_disk_size = item_specs['Hard Disk Kapasitesi']
                flag2=1
        except Exception:
            if(not flag2):
                item_disk_type = '---'
                item_disk_size = '---'

        if(flag1 and flag2):
            item_disk_type = 'hdd/ssd'
            item_disk_size = item_specs['SSD Kapasitesi'] + ' SSD/' + item_specs['Hard Disk Kapasitesi']+' HDD'

        item_site_name = "trendyol"

        item_image_link = response.xpath(".//div/img/@src")[0].get()
        ##
        
        
        product['item_name'] = item_name
        product['item_brand'] = item_brand
        product['item_model_number'] = modelNo
        product['item_operating_system'] = item_specs['İşletim Sistemi']
        product['item_processor_type'] = item_specs['İşlemci Tipi']
        product['item_processor_gen'] = item_specs['İşlemci Nesli']
        product['item_ram'] = item_specs['Ram (Sistem Belleği)']
        product['item_disk_type'] = item_disk_type

        #product['item_disk_size_ssd'] = item_specs['SSD Kapasitesi']
        #product['item_disk_size_hdd'] = item_specs['Hard Disk Kapasitesi']

        product['item_disk_size'] = item_disk_size
        product['item_screen_size'] = item_specs['Ekran Boyutu']
        product['item_rating'] = item_rating
        product['item_price'] = item_price
        product['item_site_name'] = item_site_name
        product['item_image_link'] = item_image_link
        product['item_link'] = response.request.url
        #product['item_specs'] = item_specs
        
        yield product
            

