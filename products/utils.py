from products.models import Product , Category
from django.db.models import Q

def q_search(query):
    keywords = [word for word in query.split() if len(word)> 2]
    
    q_results = Q()
    
    for kword in keywords:
        q_results |= Q(description__icontains = kword)
        q_results |= Q(name__icontains = kword)
        q_results |= Q(category__name__icontains = kword)
        
    return Product.objects.filter(q_results)