from products.models import Product , Category
from django.db.models import Q
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector,SearchHeadline
# def q_search(query):
#     keywords = [word for word in query.split() if len(word)> 2]
    
#     q_results = Q()
    
#     for kword in keywords:
#         q_results |= Q(description__icontains = kword)
#         q_results |= Q(name__icontains = kword)
#         q_results |= Q(category__name__icontains = kword)
        
#     return Product.objects.filter(q_results)

def q_search(query):
    if query != '' and query is not None :
        vector = SearchVector("name" , weight="A")+SearchVector("description",weight="B")+SearchVector("category__name",weight="C")
        query = SearchQuery(query)
        results=Product.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")
        
        results = results.annotate(
            headline = SearchHeadline(
                "name",
                query,
                start_sel = '<span style="background-color:yellow">',
                stop_sel = '</span>'
            )
        )
        
        results = results.annotate(
            bodyline = SearchHeadline(
                "description",
                query,
                start_sel = '<span style="background-color:yellow">',
                stop_sel ='</span>'
            )
        )
        
        results = results.annotate(
            footerline = SearchHeadline(
                "category__name",
                query,
                start_sel = '<span style="background-color:yellow">',
                stop_sel ='</span>'
            )
        )
        
    return results