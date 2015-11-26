from django import forms


class TimeTableForm(forms.Form):
    station_from = forms.CharField(label='from', max_length=30, widget=forms.TextInput(
        attrs={'placeholder': 'Station from'}))
    station_to = forms.CharField(label='to', max_length=30, widget=forms.TextInput(
        attrs={'placeholder': 'Station to'}))
    datetime = forms.DateTimeField(
        label='when', widget=forms.TextInput(attrs={'placeholder': 'Date'}))
