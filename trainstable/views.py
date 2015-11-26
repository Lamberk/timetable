from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, date, time
from .models import RouteStation, Station, Train
from .forms import TimeTableForm


def search(request):
    if request.method == 'POST':
        form = TimeTableForm(request.POST)
        if form.is_valid():
            station_from = Station.objects.get(
                station_name=str(form.data['station_from']))
            station_to = Station.objects.get(
                station_name=str(form.data['station_to']))
            datetime = form.data['datetime']
            finder = RouteStation()
            trains_list = finder.find_trains(
                station_from, station_to, datetime)
            return render(request, 'trainstable/timetable.html', {
                'trains_list': trains_list,
                'station_from': station_from,
                'station_to': station_to,
                'date': datetime,
            })
    else:
        form = TimeTableForm()
    return render(request, 'trainstable/search.html', {'form': form})


def station_detail(request, station_id):
    station = get_object_or_404(Station, pk=station_id)
    return render(request, 'trainstable/station.html', {'station': station})


def train_detail(request, train_id):
    train = get_object_or_404(Train, pk=train_id)
    return render(request, 'trainstable/train.html', {'train': train})
