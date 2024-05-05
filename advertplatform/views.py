from django.shortcuts import render
from .models import Seller

def sellers_list(request):
    sellers = Seller.objects.all().order_by('date_first_added')
    # Add filtering logic here if needed
    return render(request, 'sellers_list.html', {'sellers': sellers})
