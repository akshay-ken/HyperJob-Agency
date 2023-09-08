from django.shortcuts import render
from .models import Vacancy


# Create your views here.
def my_view(request):
    return render(request, 'index.html')


def vacancy_view(request):
    data = Vacancy.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'vacancy.html', context=context)
