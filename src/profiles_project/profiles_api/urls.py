from django.conf.urls import url
from .views import *

urlpatterns =[
    url(r'helloview/',HelloAPIView.as_view()),
]
