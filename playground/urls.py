from django.urls import path
from . import views

# URLConf
# since we added playground in the main storefront.urls.py , so we don't need to prepend that here
urlpatterns = [
    # path('playground/hello/', views.say_hello)
    path('hello/', views.say_hello)
]
