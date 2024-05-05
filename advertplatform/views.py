from django.shortcuts import render
from .models import Seller
from django.db.models import Q

def sellers_list(request):
    # Filtering
    query = request.GET.get('q', '')  # Assume a simple text search in 'name' or 'domain'
    sellers = Seller.objects.filter(
        Q(name__icontains=query) | Q(domain__icontains=query)
    )

    # Sorting
    sort_by = request.GET.get('sort', 'date_first_added')  # Default sort is by 'date_first_added'
    order = request.GET.get('order', 'asc')

    if order == 'desc':
        sort_by = '-' + sort_by
    sellers = sellers.order_by(sort_by)

    return render(request, 'sellers_list.html', {'sellers': sellers, 'query': query, 'sort_by': sort_by, 'order': order})
