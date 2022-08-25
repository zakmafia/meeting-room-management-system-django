from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Booking, Room, AvailableTime

# Create a booking Form
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'address']

    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter the room name'
        self.fields['address'].widget.attrs['placeholder'] = 'Enter the room address'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class AvailableTimeForm(ModelForm):
    class Meta:
        model = AvailableTime
        fields = ('available_time',)
        labels ={
            'available_time': ''
        }
        widgets = {
            'available_time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the available times'})
        }
