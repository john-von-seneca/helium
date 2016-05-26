
from .adapter import *

class PamiAdapter(Adapter):
	URL = 'https://www.computer.org/csdl/trans/tp/index.html'
	URL_ROOT = 'https://www.computer.org'
	def __init__(self):
		print('pami-adapter')
		self.soup = None
		Adapter.__init__(self)

	def parse(self, url):
		return Adapter.parse(self, url)

	def _div_years(self, soup):
		return soup.find_all('div', 'volume')

	def _hashie(self, element, name_key, name_val):
		return {element[name_key]: element[name_val]}

	def _slice(self, element, *args):
		dict1 = {}
		for arg in args:
			dict1[arg] = element[arg]
		return dict1
	
	def all_years(self):
		soup = self.parse(PamiAdapter.URL)
		links = [self._slice(div.find_all('a')[0],'title','href') for div in self._div_years(soup)]
		for link in links:
			link['href'] = PamiAdapter.URL_ROOT + link['href']
		return links

	def _get_issues(self, url):
		soup = self.parse(url)
		div_issues = soup.find_all('div', 'issuePeriod')
		links = [self._slice(div.find_all('a')[0], 'title', 'href') for div in div_issues]
		for link in links:
			link['href'] = PamiAdapter.URL_ROOT + link['href']
		return links

	def all_issues(self):
		info_volumes = self.all_years()
		for info_volume in info_volumes:
			issues_current = self._get_issues(info_volume['href'])
			info_volume['issues'] = issues_current
		return info_volumes
			

	
			

	
