from django import forms

class TimeTableForm(forms.Form):
    station_from = forms.CharField(label='from', max_length=30)
    station_to = forms.CharField(label='to', max_length=30)
    datetime = forms.DateTimeField(label='when')
