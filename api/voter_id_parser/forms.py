from django import forms

class RequestForm(forms.Form):
    nid_number = forms.CharField(max_length=17, label='NID', 
        widget=forms.TextInput(attrs={'class':'form-control'}))
    date_of_birth = forms.CharField(max_length=10, label="Date of Birth(YYYY-MM-DD)",
        widget=forms.TextInput(attrs={'class':'form-control'}))
    