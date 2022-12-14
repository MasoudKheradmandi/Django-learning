from django import forms 
from .models import Post


class ContactForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author','title','content','status','category','published_date',]