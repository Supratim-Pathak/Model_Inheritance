from myapp import views
from django.urls import URLPattern, path

urlpatterns = [
    path('', views.index)
]