Certainly! Here's a README file for your `AsifDocDownloader` project:

---

# AsifDocDownloader

`AsifDocDownloader` is a Python-based tool designed to efficiently scout the [Asif website](https://asif.co.il) for PDF files and download them. The project is divided into two main stages: 
1. Crawling the website to identify and list all the PDF links.
2. Downloading the PDFs based on the generated list.

## Features

- **Deep Crawling**: Uses Scrapy to deeply crawl and navigate through the Asif website.
- **Error Handling**: Captures and logs URLs that encountered errors during the crawling process.
- **Efficient Downloading**: Downloads PDFs in sequence and saves them with a unique naming convention.

## Prerequisites

- Python 3.x
- Scrapy
- Requests

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/AsifDocDownloader.git
   ```

2. Navigate to the project directory:
   ```bash
   cd AsifDocDownloader
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Crawling**:
   Run the spider to crawl the Asif website and generate a list of PDF URLs:
   ```bash
   python main_crawler.py
   ```

2. **Downloading**:
   After generating the list of PDF URLs, run the downloader script:
   ```bash
   python downloader.py
   ```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
