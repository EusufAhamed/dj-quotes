from django.shortcuts import render
from quotes_app.models import Quote

# Create your views here.
def quotes_view(request):
    data = {}
    data['quotes'] = Quote.objects.all()
    return render(request, 'quote.html', data)