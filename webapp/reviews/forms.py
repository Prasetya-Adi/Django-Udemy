from django import forms
from django.forms.widgets import Textarea


class ReviewForms(forms.Form):
    user_name = forms.CharField(label='Your Name', max_length=10, error_messages={
        'required': 'Your name is required to this form.',
        'max_length': 'Your name is must 10 character',
    })
    review_text = forms.CharField(
        label='Your Feedback', widget=Textarea, max_length=200)
    rating = forms.IntegerField(label='Your Rating', min_value=1, max_value=5)
