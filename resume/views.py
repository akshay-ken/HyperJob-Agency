from django.shortcuts import render
from .models import Resume


# Create your views here.
def resume_view(request):
    data = Resume.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'resume.html', context=context)
