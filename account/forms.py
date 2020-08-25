from django import forms 
from .models import * 


class BlogForm(forms.ModelForm):
    class Meta: 
        # specify model to be used 
        model = Blog 
        # specify fields to be used 
        fields = "__all__"