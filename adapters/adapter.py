from bs4 import BeautifulSoup
import urllib.request

class Adapter:
	def __init__(self):
		pass

	def download_hard(self, url, file_name):
		response = urllib.request.urlopen(url)
		data = response.read()
		html = str(data)
		with open (file_name, 'a') as f:
			f.write(html)
		return html
	
	def download(self, url):
		file_name = 'sth'
		if False:
			html = self.download_hard(url, file_name)
		else:
			html = open(file_name,'r').read()
		return html

	def parse(self, url):
		html = self.download(url)
		soup = BeautifulSoup(html, 'html.parser')
		return soup

		
