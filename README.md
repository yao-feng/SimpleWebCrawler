# SimpleWebCrawler
A simple web crawler for dynamic websites (specifically Lazada.sg)

For Windows 10
1. Dowload Python 3 onto your computer and set the environment variables (Google for this if you are unsure of what to do).

2. Go to Command Prompt (This can be done by clicking on the "magnifying glass" icon on the task bar, type in "cmd" and then press "Enter" key).

3. In the Command Prompt, type in:
```
pip3 install BeautifulSoup4 Selenium 
```
This ensures that you have both BeautifulSoup4 and Selenium module in your local machine.

4. One last thing we need to download. Go to http://chromedriver.chromium.org/downloads to download the latest chrome driver.

5. Extract the executable file (chromedriver.exe) and save it in any folder.

6. Set the path to chromedriver.exe in your environment variables.

7. Run webCrawler.py and product.txt should be created.

8. The output in product.txt should appear in the format: 
      PRODUCT_1_NAME PRODUCT_1_PRICE, PRODUCT_2_NAME PRODUCT_2_PRICE, PRODUCT_3_NAME PRODUCT_3_PRICE ...
      
Happy crawling!! :)
