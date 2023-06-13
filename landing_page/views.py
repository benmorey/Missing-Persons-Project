from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landingPageView(request):
    return render(request, 'landing_page/index.html')