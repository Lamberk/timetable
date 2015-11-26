from django.core.management.base import BaseCommand, CommandError
from trainstable.models import RouteStation, Station, Route
from datetime import datetime, date, time, timedelta
import random


class Command(BaseCommand):
    help = 'Generate content to datebase'

    @staticmethod
    def generate_station_list():
        for index, route in enumerate(Route.objects.all()):
            index = index + 1
            station_list = Command.create_route()
            Command.save_route_to_timetable(station_list, route)

    @staticmethod
    def create_route():
        route = []
        list_of_stations = [x for x in xrange(1, 20)]
        number_of_tops = random.choice(xrange(1, 5)) + 5
        for i in xrange(number_of_tops):
            element = random.choice(list_of_stations)
            route.append(element)
            list_of_stations.remove(element)
        return route

    @staticmethod
    def save_route_to_timetable(route_list, route):
        absolute_zero_time = datetime.combine(date(2015, 05, 01), time(01, 00))
        for index, station_id in enumerate(route_list):
            station_id = station_id + 1
            index = index + 1
            if index == 1:
                time_arrive = None
                time_depart = absolute_zero_time
            elif index == len(route_list):
                time_arrive = absolute_zero_time
                time_depart = None
            else:
                time_arrive = absolute_zero_time
                time_depart = time_arrive + timedelta(minutes=30)
            new_station = RouteStation(
                route=route,
                station=Station.objects.get(id=station_id),
                time_arrive=time_arrive,
                time_depart=time_depart,
                position_in_route=index
            )
            new_station.save()
            if index == 1:
                absolute_zero_time = absolute_zero_time + timedelta(minutes=30)
            else:
                absolute_zero_time = absolute_zero_time + timedelta(hours=1)

    def handle(self, *args, **options):
        Command.generate_station_list()
