from django import forms
from django.forms import ModelForm

from .models import event_reservation, Event


class event_reservationForm(forms.Form):
    event =  forms.ModelChoiceField(queryset=Event.objects.filter(status=True),widget=forms.Select(attrs={'class': 'browser-default'}))
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    phone = forms.CharField(max_length=20)
    age = forms.IntegerField()
class rec_form(forms.Form):
    colleges_list = [('Computer Science','Computer Science'),
                     ('Engineering','Engineering'),
                     ('Information Systems','Information Systems'),
                     ('Applied Arts','Applied Arts'),
                     ('Commerce and Business Administration','Commerce and Business Administration')
                     ]
    commities_list = [('multimedia', 'multimedia'), ('hr', 'hr'), ('er', 'er'), ('presentation', 'presentation'),
                      ('project', 'project')]

    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    phone = forms.CharField(max_length=20)
    email = forms.EmailField()
    college = forms.ChoiceField(widget=forms.Select(attrs={'class': 'browser-default'}), choices=colleges_list)
    year_of_study = forms.IntegerField()
    first_prefrence = forms.ChoiceField(widget=forms.Select(attrs={'class': 'browser-default'}), choices=commities_list)
    second_prefrence = forms.ChoiceField(widget=forms.Select(attrs={'class': 'browser-default'}), choices=commities_list)
