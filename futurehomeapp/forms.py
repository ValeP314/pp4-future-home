from .models import Question, Booking
from django import forms


class QuestionForm (forms.ModelForm):
    class Meta:
        model = Question
        fields = ('body',)


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('body',)
