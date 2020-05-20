from django.urls import path, include
from .views import home, get_long_url, shrink_url


urlpatterns = [
    path('', home, name='home'),
    path('<shrinked_url>', get_long_url, name='get_long_url'),
    path('/shrink_url', shrink_url, name='shrink_url')

]