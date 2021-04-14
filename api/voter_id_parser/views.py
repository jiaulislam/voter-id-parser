from django.shortcuts import render, redirect
from subprocess import run, PIPE
from .forms import RequestForm
import main
import sys
# Create your views here.
def __make_query(request,nid, dob):
    cus_output = main.run(nid, dob)
    return cus_output

def search(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            nid = form.cleaned_data['nid_number']
            dob = form.cleaned_data['date_of_birth']
            output = __make_query(request, nid, dob)
            context = {
                'result' : output.strip(),
                'title' : 'JSON RESULT'
            }
            return render(request, 'voter_id_parser/result.html', context)
    else:
        form = RequestForm()
        context = {
            'title': "Search ID",
            'form': form
        }
        return render(request, 'voter_id_parser/search.html', context)