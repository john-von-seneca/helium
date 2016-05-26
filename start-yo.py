


from src.adapters.pami_adapter import *
from src.third_party.scholar import *

pami = PamiAdapter()
[print(art.attrs) for art in pami.query_scholar('Coherency Sensitive Hashing')]

# url = 'https://www.computer.org/csdl/trans/tp/2016/06/index.html'
# print(pami._get_toc_of_issue(url))

# search_query = 'Coherency Sensitive Hashing'

# querier = ScholarQuerier()
# query = SearchScholarQuery()
# query.set_phrase(search_query)
# query.set_num_page_results(3)
# querier.send_query(query)
# #txt(querier, None)

# articles_filtered = [art.attrs['title'].lower().find for art in querier.articles]

# [print(encode(art.as_txt()) + '\n') for art in querier.articles]


pami.query_scholar('Coherency Sensitive Hashing')
