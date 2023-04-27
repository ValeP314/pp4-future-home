from django import forms
from .models import Listing, Question, Appointment
# from bootstrap_datepicker_plus.widgets import DatePickerInput


class ListingForm (forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('address', 'slug', 'author', 'featured_image', 'excerpt',
                  'content', 'status', 'bedrooms', 'bathrooms',
                  'ber_category', 'price')

        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'bedrooms': forms.TextInput(attrs={'class': 'form-control'}),
            'bathrooms': forms.TextInput(attrs={'class': 'form-control'}),
            'ber_category': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            }


class QuestionForm (forms.ModelForm):
    class Meta:
        model = Question
        fields = ('body',)


# class AppointmentForm (forms.ModelForm):
#    class Meta:
#        model = Appointment
#        fields = ('user', 'day', 'time')
#
#        widgets = {
#            'user': forms.TextInput(attrs={'class': 'form-control'}),
#           'day': forms.TextInput(attrs={'class': 'form-control'}),
#            'time': forms.Select(attrs={'class': 'form-control'}),
#            }
