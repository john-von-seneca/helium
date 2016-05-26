from bs4 import BeautifulSoup
from ..utils.downloader import *

class Adapter:
	def __init__(self):
		print('adapter')
		self.downloader = Downloader()

	def parse(self, url):
		html = self.downloader.get(url)
		soup = BeautifulSoup(html, 'html.parser')
		return soup
