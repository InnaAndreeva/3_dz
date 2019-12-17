from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.dateparse import parse_date

from sport_sections.models import Sport_Section
from .domain_model import Application_DM
from sport_sections.domain_model_sport_section import Sport_Section_DM
# Create your views here.


def initialize_sport_sections():
    sport_sections = Sport_Section_DM.findAll()
    context = {
        'sport_sections': sport_sections
    }
    return context


def apply_for_study(request):
    context = initialize_sport_sections()
    return render(request, 'accounts/application/application.html', context)


def send_application(request):
    if request.method == 'POST':
        sport_section = request.POST['sport_section']
        birth_date = request.POST['birth_date']
        district = request.POST['district']
        gender = request.POST['gender']

        birth_date = parse_date(birth_date)

        app_dm = Application_DM.create(user=request.user, sport_section_id=sport_section,
                                       birth_date=birth_date, district=district, gender=gender)
        if app_dm.has_errors():
            for err in app_dm.errors:
                messages.error(request, err)
            return render(request, 'accounts/application/application.html', context=initialize_sport_sections(), status=400)
            # return redirect('send_application')
        messages.success(
            request, 'Ваша заявка будет рассмотрена ближайшее время и мы свяжемся с Вами.')
        return redirect('dashboard')
    else:
        # return redirect('apply_for_study')
        return render(request, 'accounts/application/application.html', context=initialize_sport_sections(), status=400)
