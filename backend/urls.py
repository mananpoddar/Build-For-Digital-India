from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

app_name = "backend"


urlpatterns =[
    
    path('admin/', admin.site.urls),
    # path('auth/', AuthAPI.as_view()),
    # path('getAadharDetails/', GetAadharAPI.as_view()),
    url(r'',index, name='home'),
]