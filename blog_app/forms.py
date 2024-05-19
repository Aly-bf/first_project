from typing import Any
from django import forms
from django.core.validators import ValidationError
from blog_app.models import Message

class ContactUsForm(forms.Form):
    text = forms.CharField(label='Your Message', widget=forms.Textarea, max_length=7, required=False)
    name = forms.CharField(label='Your name', widget=forms.Textarea, max_length=7)
    birthday = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2020)))

    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        if name == text:
            raise forms.ValidationError('Your name and message must be different')
        

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if 'a' in name:
            raise ValidationError('a can not be in this')
        return name
    


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'text', 'email', 'age']  # exclude vase vaqty mikhyam ona ei k mikhyam nabashe  # fields = '__all__' vase vaqty hamash mikhaym
        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a title'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
        }                                                
        