from django.urls import path

from .views import Create_User, Finish_User


urlpatterns = [
    path('create', Create_User),
    path('finish', Finish_User),
]
