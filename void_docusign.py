from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import credentials as creds

# Create Firefox Driver - can use Chromedriver also
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.85 Safari/537.36")
driver = webdriver.Firefox(firefox_profile=profile)


# Login to docusign
driver.get('https://na8.salesforce.com/a45C0000000F2fh')
driver.find_element_by_xpath('//*[@id="username"]').send_keys(creds.sf_username)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(creds.sf_password)
driver.find_element_by_xpath('//*[@id="Login"]').click()

# NOTE: Must Authenticate Manually at this point due to security restrictions and close any popup Lightning ads

# Dummy URLs - replace with a list of urls for the Docusign Status Objects (salesforce links) you wish to void
urls = ['https://na8.salesforce.com/a45C0000000F2fh','www.google.com','https://na8.salesforce.com/a45C0000000F2fh','https://na8.salesforce.com/006C0000018ncSq','https://na8.salesforce.com/a45C0000000F2fh']

void_message = 'This document is incomplete and has expired. If you have completed a separate docusign agreement then this message can be ignored.'

for url in urls:
    try:
        driver.get(url)
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/table/tbody/tr/td[2]/div[4]/div[1]/table/tbody/tr/td[2]/input[9]').click()
        driver.find_element_by_xpath('//*[@id="j_id0:j_id1:j_id2:DocuSignVoidEnvelopePage:VoidEnvelopeReason"]').send_keys(void_message)
        # driver.find_element_by_xpath('//*[@id="j_id0:j_id1:j_id2:DocuSignVoidEnvelopePage:btnVoidEnv"]').click()
    except:
        print('Failed to void %s' % url)

driver.quit()
