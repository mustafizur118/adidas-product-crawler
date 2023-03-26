# adidas-product-crawler . 
Install the required packages: pip install -r requirements.txt
python adidas_crawler.py --category shoes --gender men --output output.csv
This command will scrape all men's shoes from the Adidas website and save the results to a CSV file named "result.csv".

Supported options:

--category: The category of products to scrape (e.g. "shoes", "clothing", "accessories").
--gender: The gender of the products to scrape (e.g. "men", "women", "kids").
--result: The name of the output file to save the results to.

Acknowledgments
This project uses the following third-party libraries:

BeautifulSoup
Selenium
