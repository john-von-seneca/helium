
from .adapter import *

class PamiAdapter(Adapter):
	URL = 'https://www.computer.org/csdl/trans/tp/index.html'
	URL_ROOT = 'https://www.computer.org'
	def __init__(self):
		self.soup = None

	def parse(self):
		self.soup = Adapter.parse(self,
							 PamiAdapter.URL)

	def update_soup(self):
		if self.soup is None:
			self.parse()

	def _div_years(self):
		return self.soup.find_all('div', 'volume')
		
	def all_years(self):
		self.update_soup()
		links_relative = [div.find_all('a')[0]['href'] for div in self._div_years()]
		links_absolute = [self.URL_ROOT+link for link in links_relative]
		return links_absolute

	
			

	
