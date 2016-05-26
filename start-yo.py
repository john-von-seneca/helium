


from src.adapters.pami_adapter import *
from src.third_party.scholar import *

pami = PamiAdapter()

# url = 'https://www.computer.org/csdl/trans/tp/2016/06/index.html'
# print(pami._get_toc_of_issue(url))

querier = ScholarQuerier()
query = SearchScholarQuery()
query.set_phrase(options.phrase)
query.set_num_page_results(3)
querier.send_query(query)
#txt(querier, None)
[print(encode(art.as_txt()) + '\n') for art in querier.articles]



