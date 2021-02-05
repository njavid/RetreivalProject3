from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json


class WebCrawler:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--incognito")
        self.chrome_options.add_argument("--window-size=1920x1080")
        self.counter = 0

    def crawl(self, start_url, n):
        driver = webdriver.Chrome(chrome_options=self.chrome_options, executable_path="chromedriver.exe")
        article_name, article_abstract, article_authors, article_release_date, links = [], [], [], [], []

        # crawl
        while self.counter < n:
            driver.get(start_url[self.counter])
            self.counter += 1
            time.sleep(2)

            # find article name
            name = driver.find_elements_by_xpath("//h1[@class='name']")[0].text

            # see new articles only:
            if name not in article_name:
                article_name.append(name)
                # find abstract
                article_abstract.append(driver.find_elements_by_xpath("//p")[2].text)

                # find release year
                article_release_date.append(driver.find_elements_by_xpath("//span[@class='year']")[0].text)

                # find authors
                parent_element = driver.find_element_by_class_name("authors")
                children_list = parent_element.find_elements_by_tag_name("a")
                temp = [a.text for a in children_list]
                article_authors.append(temp[0::2])
                links_elements = driver.find_elements_by_xpath("//a[@class='au-target']")

                # find links
                article_links = [a.get_attribute("href") for a in links_elements if
                                 a.get_attribute("href") is not None]
                if len(article_links) > 11:
                    article_links = article_links[1:10]

                # add new links to queue
                start_url += article_links
                links.append(article_links)

                # wait 1 sec and continue
                time.sleep(1)
            else:
                article_name.append("seen")
                article_release_date.append("seen")
                article_authors.append([])
                article_abstract.append("seen")
                links.append([])

        driver.quit()
        # save result
        output = {'articles': []}
        for i in range(0, n):
            if article_name[i] != "seen":
                output['articles'].append({
                    "id": start_url[i].split("/")[4],
                    "title": article_name[i],
                    "abstract": article_abstract[i],
                    "date": article_release_date[i],
                    "authors": article_authors[i],
                    "references": [r.split("/")[4] for r in links[i]]
                })

        with open('crawl_output.txt', 'w') as outfile:
            json.dump(output, outfile)

        return None
