from django import forms


class UploadForms(forms.Form):
    user_image = forms.ImageField()
