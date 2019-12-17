from django.shortcuts import render

from .domainModel import Coach_DM
# Create your views here.


def show_coaches(request):
    coaches = Coach_DM.findAll()
    context = {
        'coaches': coaches
    }

    return render(request, 'pages/coaches/coaches.html', context)
