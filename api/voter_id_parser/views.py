from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

from actions import SearchAction
from .forms import RequestForm


def search(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            nid = form.cleaned_data['nid_number']
            dob = form.cleaned_data['date_of_birth']
            json = SearchAction(settings.WEBDRIVER_WINDOW, nid, dob)
            return HttpResponse(json, content_type="application/json")
    else:
        if request.GET.get('nid') and request.GET.get('dob'):
            nid = request.GET.get('nid')
            dob = request.GET.get('dob')
            json = SearchAction(settings.WEBDRIVER_WINDOW, nid, dob)
            return HttpResponse(json, content_type="application/json")
        else:
            form = RequestForm()
            context = {
                'title': "Search NID",
                'form': form
            }
            return render(request, 'voter_id_parser/search.html', context)
