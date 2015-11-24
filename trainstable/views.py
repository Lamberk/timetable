from django.shortcuts import render,redirect
from datetime import datetime, date, time
from .models import TimeTable
from .forms import TimeTableForm

def table(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TimeTableForm(request.POST)
        if form.is_valid():
            station_from = form.data['station_from']
            station_to = form.data['station_to']
            datetime = form.data['datetime']
            finder = TimeTable()
            #table = finder.find_trains(station_from, station_to, datetime)
            #print table[0]['train'].train_id
            trains_list = finder.find_trains(station_from, station_to, datetime)
            return render(request, 'timetable.html', {
                'trains_list' : trains_list, 
                'station_from' : station_from,
                'station_to' : station_to
                })
    # if a GET (or any other method) we'll create a blank form
    else:
        form = TimeTableForm()
    return render(request, 'index.html', {'form': form})

def finder(request):
    return render(request, 'simple_answer.html')


def generator(request):
    timetable = TimeTable()
    timetable.generate_timetable()
    return render(request, 'simple_answer.html')