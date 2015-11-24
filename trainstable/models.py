from django.db import models
from datetime import datetime, date, time, timedelta
import random
from django.db.models import Transform


class Train(models.Model):
    train_id = models.IntegerField(default=0)
    seats = models.IntegerField(default=0)

    def __unicode__(self):
        return 'Train #%s' % (
            self.train_id
        )


class Station(models.Model):
    station_id = models.IntegerField(default=0)
    station_name = models.CharField(max_length=50)

    def __unicode__(self):
        return "%s %s" % (
            self.station_name, self.station_id
        )


class TimeTable(models.Model):
    train = models.ForeignKey(Train)
    station = models.ForeignKey(Station)
    time_arrive = models.DateTimeField()
    time_depart = models.DateTimeField()
    route = models.IntegerField(default=0)
    position_in_route = models.IntegerField(default=0)

    def __unicode__(self):
        return '%s %s Route: %s Position in route: %s' % (
            self.train, self.station, self.route, self.position_in_route
        )

    @staticmethod
    def create_route():
        route = []
        list_of_stations = [x for x in xrange(20)]
        number_of_tops = random.choice(xrange(5)) + 5
        for i in xrange(number_of_tops):
            element = random.choice(list_of_stations)
            route.append(element)
            list_of_stations.remove(element)
        return route

    @staticmethod
    def save_route_to_timetable(route, train):
        absolute_zero_time = datetime.combine(date(2015, 05, 01), time(01, 00))
        for index, station_id in enumerate(route):
            station_id = station_id + 1
            index = index + 1
            if index == 1:
                time_arrive = '1111-11-11 11:11:11'
                time_depart = absolute_zero_time
            elif index == len(route):
                time_arrive = absolute_zero_time
                time_depart = '1111-11-11 11:11:11'
            else:
                time_arrive = absolute_zero_time
                time_depart = time_arrive + timedelta(minutes=30)
            new_station = TimeTable(
                train=train,
                station=Station.objects.get(station_id=station_id),
                time_arrive=time_arrive,
                time_depart=time_depart,
                route=train.train_id,
                position_in_route=index
            )
            new_station.save()
            if index == 1:
                absolute_zero_time = absolute_zero_time + timedelta(minutes=30)
            else:
                absolute_zero_time = absolute_zero_time + timedelta(hours=1)

    def generate_timetable(self):
        for train in Train.objects.all():
            route = TimeTable.create_route()
            TimeTable.save_route_to_timetable(route, train)

    def find_trains(self, station_from, station_to, date):
        trains_list = []
        station_from = Station.objects.get(station_name=station_from)
        station_to = Station.objects.get(station_name=station_to)
        for raw in TimeTable.objects.filter(time_depart__contains = date, station = station_from):
            trains_list.append({
                'train': raw.train, 
                'route': raw.route, 
                'station_id' : raw.station_id, 
                'time_arrive' : raw.time_arrive,
                'time_depart' : raw.time_depart,
                'position_in_route' : raw.position_in_route
            })
        final_list = []
        for train in trains_list:
            for raw in TimeTable.objects.filter(station = station_to, route = train['route']):
                if int(raw.position_in_route) > int(train['position_in_route']):
                    final_list.append({
                        'station_from' : station_from,
                        'time_depart' : train['time_depart'],
                        'station_to' : station_to,
                        'time_arrive' : raw.time_arrive,
                        'train' : train['train']
                    })
        print final_list
        return final_list

