import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class PDFSpider(scrapy.Spider):
    name = 'pdf_spider'
    allowed_domains = ['asif.co.il']
    start_urls = ['https://asif.co.il']

    def parse(self, response):
        # Extract and yield PDF file URLs
        for href in response.css('a[href$=".pdf"]::attr(href)').getall():
            file_url = response.urljoin(href)
            file_name = href.split('/')[-1]

            yield {
                'file_url': file_url,
                'file_name': file_name
            }

            # Check if the URL is valid or encountered an error
            if response.status == 200:
                self.save_to_file(file_url, 'URL.txt')
            else:
                self.save_to_file(file_url, 'URL_error.txt')

        # Follow internal links
        for next_page in response.css('a::attr(href)').getall():
            if self.allowed_domains[0] in next_page:
                yield response.follow(next_page, callback=self.parse)

    def save_to_file(self, content, filename):
        with open(filename, 'a') as file:
            file.write(content + '\n')


def run_spider():
    # Create an instance of the CrawlerProcess
    process = CrawlerProcess(get_project_settings())

    # Run the spider
    process.crawl(PDFSpider)
    process.start()


if __name__ == "__main__":
    run_spider()
