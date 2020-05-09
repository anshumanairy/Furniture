from django.shortcuts import render
from furn.models import product_model,search

def searchProduct(request):
    query = request.GET.get('query')
    user = None
    context = {
        'query' : query,
    }
    if request.user.is_authenticated:
        user = request.user
    if query is not None:
        search.SearchQuery.objects.create(query=query,user=user)
        result = product_model.product_upload.objects.search(query)
        context['products']=result
    return render(request,'search-page.html',context)