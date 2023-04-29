from django import forms
from .models import Listing, Question, Answer


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


class ReplyForm (forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('body',)
