
## Scrap Data from News Website

### Project Description

This project involves a Python script that uses Selenium to scrape data from a news website. Specifically, the script extracts article titles, subtitles, and links from the sports section of "The Sun" website. The data is printed to the console and can be easily modified to store in a file or database for further analysis.

### Features

- **Automated Web Scraping**: Uses Selenium WebDriver to navigate and interact with the web page.
- **Data Extraction**: Extracts article titles, subtitles, and links.
- **Error Handling**: Includes error handling to manage potential issues during web scraping.
- **Customizable**: Easily adaptable to scrape different sections of the website or other news websites.

### Prerequisites

- Python 3.x
- Selenium
- Microsoft Edge WebDriver (msedgedriver)

### Installation

1. Install the required Python packages:
   ```bash
   pip install selenium
   ```

2. Download and install the Microsoft Edge WebDriver from the [official site](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).

### Usage

1. Update the `path` variable in the script to the location of the `msedgedriver` executable on your system.
2. Run the script:
   ```bash
   python scrap_news.py
   ```

### Code

Present in main.py directory

### Uploading to GitHub

1. Create a new repository on GitHub.
2. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/your-repository-name.git
   ```
3. Navigate to the cloned repository and create a new Python file (e.g., `scrap_news.py`) and paste the code above.
4. Add a README.md file and include the project description, prerequisites, installation, usage, and code sections.
5. Stage, commit, and push the changes to GitHub:
   ```bash
   git add .
   git commit -m "Initial commit with news scraper code"
   git push origin main
   ```

Your project is now ready and available on GitHub for others to use and contribute to.
