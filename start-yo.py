


from src.adapters.pami_adapter import *

pami = PamiAdapter()
#print(pami.soup.prettify())
# print(pami.all_years())


url = "https://www.computer.org/csdl/trans/tp/2016/index.html"
# print(pami._get_issues(url))
print(pami.all_issues())








