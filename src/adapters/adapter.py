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

	def send_query(self):
		# self.querier.send_query(self.query)
		self.querier.clear_articles()
		self.querier.query = self.query
		url = self.query.get_url()
		# html = self.querier._get_http_response(url=url,log_msg='dump of query response HTML', err_msg='results retrieval failed')
		html = self.downloader.get2(url)
		self.querier.parse(html)
		
	def query_scholar(self, search_query):
		self.query.set_phrase(search_query)
		self.send_query()
		return self._filtered_articles(search_query, self.querier.articles)
		
