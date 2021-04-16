from django.shortcuts import render
from django.http import HttpResponse
from .forms import RequestForm
import main


def __make_query(nid, dob):
    cus_output = main.run(nid, dob)
    return cus_output


def search(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            nid = form.cleaned_data['nid_number']
            dob = form.cleaned_data['date_of_birth']
            json = __make_query(nid, dob)
            return HttpResponse(json, content_type="application/json")
    else:
        if request.GET.get('nid') and request.GET.get('dob'):
            nid = request.GET.get('nid')
            dob = request.GET.get('dob')
            json = __make_query(nid, dob)
            return HttpResponse(json, content_type="application/json")
        else:
            form = RequestForm()
            context = {
                'title': "Search NID",
                'form': form
            }
            return render(request, 'voter_id_parser/search.html', context)
