from django.urls import path

from . views import *

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
]
