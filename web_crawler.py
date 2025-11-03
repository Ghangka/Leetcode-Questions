# Problem: 

# Given a URL, crawl that webpage for URLs, and then continue crawling until you've visited all URLs.
# Return all links accessed.

# Assume you have an API with two methods that you can use:
# get_html_content(url: str) -> str:
#   """returns html of the webpage of url"""
# get_links_on_page(html: str) -> list[str]:
#   """returns array of the urls in the html"""


# DFS Implementation 
# O(V * (E + C))
# V -> n = number of urls in stack
# E -> s = number of urls from one url (for loop line 19)
# c = length of page content

class WebCrawler:
    def __init__(self):
        self.visited_urls = set()
        self.stack = []

    def web_crawl(self, url: str) -> list[str]:
        self.stack.append(url)

        while len(self.stack) > 0:
            curr_url = self.stack.pop()

            if curr_url in self.visited_urls:
                continue
            
            self.visited_urls.add(curr_url)
            
            html = self.get_html_content(curr_url)
            links = self.get_links_on_page(html)
            
            for link in links:
                if link not in self.visited_urls:
                    self.stack.append(link)

        return list(self.visited_urls)
    
    def get_html_content(self, url: str) -> str:
        # This is a placeholder for the actual implementation
        return "html content"
    
    def get_links_on_page(self, html: str) -> list[str]:
        # This is a placeholder for the actual implementation
        return ["link1", "link2", "link3"]