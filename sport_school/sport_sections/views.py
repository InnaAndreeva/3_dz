from django.shortcuts import render

from .domain_model_sport import Sport_DM
from .domain_model_sport_section import Sport_Section_DM

from .active_record_sport import Sport_Active_Record
# Create your views here.


def show_sports(request):
    sports = Sport_DM.findAll()

    context = {
        'sports': sports,
    }

    return render(request, 'pages/sport_sections/sports.html', context)


def show_sport_sections_by_sport(request, sport_id):
    sport_sections = Sport_Section_DM.findAllBySportId(sport_id)

    context = {
        'sport_sections': sport_sections
    }

    return render(request, 'pages/sport_sections/sport_sections.html', context)
