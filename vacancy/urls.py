from django.urls import path
from .views import my_view, vacancy_view


urlpatterns = [
    path('', my_view),
    path('vacancies', vacancy_view)
]
