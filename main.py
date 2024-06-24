# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the URL of the website to scrape
website = "https://www.thesun.co.uk/sport/football/"
# Define the path to the msedgedriver executable
path = "Location of edgedriver_win64/msedgedriver.exe"

# Set up the Edge WebDriver service
service = Service(executable_path=path)
# Initialize the Edge WebDriver
driver = webdriver.Edge(service=service)
# Open the website
driver.get(website)

try:
    # Wait until the containers with article information are present on the page
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="teaser__copy-container"]'))
    )
    # Find all containers with article information
    containers = driver.find_elements(By.XPATH, '//div[@class="teaser__copy-container"]')

    if not containers:
        print("No containers found.")

    # Iterate through each container to extract the title, subtitle, and link
    for container in containers:
        try:
            # Extract the article title
            title_element = container.find_element(by='xpath',
                                                   value='//span[@class="teaser__headline teaser__kicker t-p-color"]')
            # Extract the article subtitle
            subtitle_element = container.find_element(by='xpath', value='//div[@class="teaser__copy-container"]/a/h3')
            # Extract the article link
            link_element = container.find_element(by='xpath', value='//div[@class="teaser__copy-container"]/a').get_attribute(
                'href')

            # Get the text content from the elements
            title = title_element.text if title_element else "No title"
            subtitle = subtitle_element.text if subtitle_element else "No subtitle"
            link = link_element if link_element else "No link"

            # Print the extracted information
            print(f"Title: {title}")
            print(f"Subtitle: {subtitle}")
            print(f"Link: {link}\n")
        except Exception as e:
            print(f"Error processing container: {e}")
except Exception as e:
    print(f"Error finding containers: {e}")
finally:
    # Close the WebDriver
    driver.quit()
