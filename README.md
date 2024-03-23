# WebScraper

This Python project is a simple web content scraper that extracts content from various websites. It utilizes the BeautifulSoup library for parsing HTML and extracting relevant information.

This is an implementation following the requirements from [Web scraper to get news article content](https://www.codementor.io/projects/tool/web-scraper-to-get-news-article-content-atx32d46qe) 

## Features

- Scrapes content from the specified URL. So far it works on articles for some news websites.
- Outputs the extracted data in a structured format.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/news-article-scraper.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the scraper script:

```bash
python webscraper.py <url>
```

Once the scraping process is complete, the extracted headlines and content will be displayed.

Other scraping options can be checked using the help command:

```bash
python webscraper.py -h
```

## Dependencies

- Python 3.x
- BeautifulSoup 4

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This project is for educational purposes only. Please be respectful of the websites you scrape and abide by their terms of service.