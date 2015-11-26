from django.db import models
from django.db.models import Transform


class Train(models.Model):
    train_id = models.IntegerField(default=0)
    seats = models.IntegerField(default=0)

    def __unicode__(self):
        return 'Train #%s' % (
            self.id
        )


class Station(models.Model):
    station_name = models.CharField(max_length=50)

    def __unicode__(self):
        return "%s %s" % (
            self.station_name, self.id
        )


class Route(models.Model):
    train = models.ForeignKey(Train)

    def __unicode__(self):
        return '%s' % (
            self.id
        )


class RouteStation(models.Model):
    station = models.ForeignKey(Station)
    time_arrive = models.DateTimeField(default=None, blank=True, null=True)
    time_depart = models.DateTimeField(default=None, blank=True, null=True)
    route = models.ForeignKey(Route)
    position_in_route = models.IntegerField(default=0)

    def __unicode__(self):
        return '%s Route: %s Position in route: %s' % (
            self.route, self.station, self.position_in_route
        )

    def find_trains(self, station_from, station_to, date):
        trains_list = []
        for raw in RouteStation.objects.filter(time_depart__contains=date, station=station_from):
            trains_list.append({
                'route': raw.route,
                'station_id': raw.id,
                'time_arrive': raw.time_arrive,
                'time_depart': raw.time_depart,
                'position_in_route': raw.position_in_route
            })
        final_list = []
        for train in trains_list:
            for raw in RouteStation.objects.filter(station=station_to, route=train['route']):
                if int(raw.position_in_route) > int(train['position_in_route']):
                    final_list.append({
                        'station_from': station_from,
                        'time_depart': train['time_depart'].strftime('%H:%M, %d %b %Y'),
                        'station_to': station_to,
                        'time_arrive': raw.time_arrive.strftime('%H:%M, %d %b %Y'),
                        'train': train['route'].train
                    })
        return final_list
