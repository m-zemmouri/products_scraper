# Scrapy and Playwright Spider for Webpage Data Extraction

This project includes a Scrapy spider that uses Playwright to extract data from a webpage. The spider extracts the product names and the breadcrumb in a list format. It saves the results in a CSV file.

## Installation

To use this project, you'll need to have Python 3, Scrapy, and Playwright installed. You can install Python 3 and pip using the following command sequence in Ubuntu:

```
sudo apt-get install software-properties-common
sudo apt-add-repository universe
sudo apt-get update
sudo apt install python3-pip
```

You can install virtualenv and create a new virtual environment for this project using the following commands:

```
sudo pip install virtualenv
mkdir ~/.storevirtualenvs
virtualenv -p python3 yourVenv
```

Replace `yourVenv` with the name you want to give to your virtual environment. To activate the virtual environment, run the following command:

```
source yourVenv/bin/activate
```

This will activate the virtual environment and any Python packages you install will be installed in the virtual environment, rather than globally on your system. You should see `(yourVenv)` at the beginning of your terminal prompt after running this command. To deactivate the virtual environment, simply run the `deactivate` command.

## Requruiments
```
sudo pip install scrapy
sudo pip install playwright-scrapy
sudo playwright install
```
To install Playwright, follow the instructions for your operating system on the [Playwright documentation page](https://playwright.dev/docs/intro#installation).

## Usage

To run the spider, navigate to the `third_part` folder and activate your virtual environment. Then run the following command:

```
scrapy crawl products -o products.csv
```

This will start the spider and save the results in a CSV file named `products.csv`.

## Output

The spider extracts the product names and breadcrumb in a list format. The breadcrumb is extracted as a list of strings, where each string represents a part of the breadcrumb. The desired format is:

```
["Home", "Drinks", "Cordials, Juices & Iced Teas", "Iced Teas"]
```

The product names are output using Scrapy.Items, which allows you to easily customize the output format.

## Customization

You can customize the spider by modifying the following files:

- `myspider/spiders/myspider.py`: This file contains the spider code. You can modify the Playwright code used to extract data from the page, as well as the output format.

- `myspider/items.py`: This file defines the Scrapy.Item used to output the product names. You can modify the item fields to include additional product data.

## Troubleshooting

If you encounter any issues while running the spider, try the following:

- Make sure you have the latest version of Scrapy and Playwright installed.
- Check the Playwright code used to extract data from the page to make sure it is correct.
- If the spider is being blocked by the website, try setting the `USER_AGENT` in the spider settings to a different value.
