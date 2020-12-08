from django.shortcuts import render
from django.http import HttpResponse
from .forms import event_reservationForm, rec_form
from .models import *
import datetime
# Create your views here.
def home(request):
    if 'r_form_sub' in request.POST:
        form = event_reservationForm()
        r_form = rec_form(request.POST or None)
        pop_msg = False
        if r_form.is_valid():
            print("Valid")
            r = recruitment()
            r.first_name = r_form.cleaned_data['first_name']
            r.last_name = r_form.cleaned_data['last_name']
            r.phone = r_form.cleaned_data['phone']
            r.email = r_form.cleaned_data['email']
            r.college = r_form.cleaned_data['college']
            r.year_of_study = r_form.cleaned_data['year_of_study']
            r.first_prefrence = r_form.cleaned_data['first_prefrence']
            r.second_prefrence = r_form.cleaned_data['second_prefrence']
            r.save()
            pop_msg = True
    elif request.method == 'POST':
        r_form = rec_form()
        form = event_reservationForm(request.POST or None)
        pop_msg = False
        if form.is_valid():
            res = event_reservation()
            res.event = form.cleaned_data['event']
            res.first_name = form.cleaned_data['first_name']
            res.last_name = form.cleaned_data['last_name']
            res.phone = form.cleaned_data['phone']
            res.age = form.cleaned_data['age']
            res.academic_year = form.cleaned_data['academic_year']
            res.national_id_number = form.cleaned_data['national_id_number']
            res.first_time_for_him = form.cleaned_data['first_time_for_him']
            res.created_at = datetime.datetime.now()
            res.save()
            pop_msg = True
    else:
        form = event_reservationForm()
        pop_msg = False
    r_form = rec_form()

    #This Season Team
    this_season_president = Season_board_1.objects.get(role='president')
    this_season_vice_1 = Season_board_1.objects.get(role='vice president 1')
    this_season_vice_2 = Season_board_1.objects.get(role='vice president 2')
    this_season_multimedia = Season_board_1.objects.get(role='multimedia director')
    this_season_er = Season_board_1.objects.get(role='er director')
    this_season_hr = Season_board_1.objects.get(role='hr director')
    this_season_project = Season_board_1.objects.get(role='project director')
    this_season_presentation = Season_board_1.objects.get(role='presentation director')
    try:
        this_season_vice_3 = Season_board_1.objects.get(role='vice president 3')
    except:
        this_season_vice_3 = None
    #Past Season Team
    past_season_president = Season_board_2.objects.get(role='president')
    past_season_vice_1 = Season_board_2.objects.get(role='vice president 1')
    past_season_vice_2 = Season_board_2.objects.get(role='vice president 2')
    past_season_multimedia = Season_board_2.objects.get(role='multimedia director')
    past_season_er = Season_board_2.objects.get(role='er director')
    past_season_hr = Season_board_2.objects.get(role='hr director')
    past_season_project = Season_board_2.objects.get(role='project director')
    past_season_presentation = Season_board_2.objects.get(role='presentation director')
    try:
        past_season_vice_3 = Season_board_2.objects.get(role='vice president 3')
    except:
        past_season_vice_3 = None

    #Events
    active_events = Event.objects.filter(status=True)
    past_events = Event.objects.filter(status=False)

    #albums
    gallery = Gallery.objects.all()

    is_recruitment_active = open_recruitment.objects.get(id=6)
    summ = summary.objects.all()
    sum = list(summ)[-4:]
    sponser = sponsers.objects.all()
    qr = qr_code.objects.get(id=1)
    context = {
        'this_season_president' : this_season_president,
        'this_season_vice_1':this_season_vice_1,
        'this_season_vice_2':this_season_vice_2,
        'this_season_multimedia':this_season_multimedia,
        'this_season_er':this_season_er,
        'this_season_hr':this_season_hr,
        'this_season_project':this_season_project,
        'this_season_presentation':this_season_presentation,
        'past_season_vice_3':past_season_vice_3,
        'this_season_vice_3':this_season_vice_3,

        'past_season_president': past_season_president,
        'past_season_vice_1': past_season_vice_1,
        'past_season_vice_2': past_season_vice_2,
        'past_season_multimedia': past_season_multimedia,
        'past_season_er': past_season_er,
        'past_season_hr': past_season_hr,
        'past_season_project': past_season_project,
        'past_season_presentation': past_season_presentation,


        'albums':gallery,
        'form':form,
        'r_form':r_form,
        'is_recruitment_active':is_recruitment_active,
        'sum':sum,
        'qr':qr,
        'pop_msg':pop_msg,
        'active_events':active_events,
        'past_events':past_events,
        'sponser':sponser,

    }
    return render(request,'index.html',context)

def summary_page(request,id):
    sponser = sponsers.objects.all()
    try:
        sum = summary.objects.get(id=id)
        board = all_seasons_board.objects.get(summary_plan=id)
        context = {
            'sum':sum,
            'board':board,
            'sponser':sponser,
        }
        return render(request,'season.html',context)
    except:
        context = {
            'sponser': sponser,
        }
        return render(request,'not-available.html',context)

from django.http import JsonResponse
def get_events_api(request):
    events = Event.objects.all().values('title','price','status')
    events_list = list(events)
    return JsonResponse(events_list, safe=False)
