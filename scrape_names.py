import scrapy

class BlogSpider(scrapy.Spider):
    name = 'svenskanamn'

    def __init__(self, gender='pojknamn', **kwargs):
        self.start_urls = [f'https://svenskanamn.se/{gender}/']

    def parse(self, response):
        for letter_page in response.css('.alphabet-wrapper .letter-select li a'):
            yield response.follow(letter_page, self.parse_page)

    def parse_page(self, response):
        for elem in response.css('.names-list .std-list-item'):
            name_elem = elem.css('.name')
            name_text = name_elem.css('::text').get()
            if (name_text is None):
                continue
            name = name_elem.css('::text').get().strip()
            url = 'https://svenskanamn.se' + name_elem.attrib['href']
            count = elem.css('.count ::text').get().strip()
            # katakana = jaconv.alphabet2kana(name.lower())
            # simple = not 'っ' in katakana
            yield {'name': name, 'link': url, 'count': count}

        for next_page in response.xpath("//span[contains(text(), 'Nästa')]/../../.."):
            yield response.follow(next_page, self.parse_page)