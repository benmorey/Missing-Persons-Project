from django.urls import path
from .views import landingPageView

urlpatterns = [
    path('', landingPageView)
]
