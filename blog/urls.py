from django.urls import path
from . import views

#creating URL path to take when going to the home page.
# empty path, the view , then the name of th path.  
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]

