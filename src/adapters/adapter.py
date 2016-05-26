from bs4 import BeautifulSoup
from ..utils.downloader import *
from ..third_party.scholar import ScholarQuerier, SearchScholarQuery

class Adapter:
	def __init__(self):
		print('adapter')
		self.downloader = Downloader()
		self.querier = ScholarQuerier()
		self.query = SearchScholarQuery()
		self.query.set_num_page_results(3)

	def parse(self, url):
		html = self.downloader.get(url)
		soup = BeautifulSoup(html, 'html.parser')
		return soup

	def _is_match(self, article, query_s):
		return article.attrs['title'][0].lower().find(query_s) >= 0
		
	def _filtered_articles(self, search_query, articles):
		query_s = search_query.lower()
		articles_filtered = [art for art in articles if self._is_match(art, query_s)]
		return articles_filtered
		
	def query_scholar(self, search_query):
		self.query.set_phrase(search_query)
		self.querier.send_query(self.query)
		return self._filtered_articles(search_query, self.querier.articles)
		
