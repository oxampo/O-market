from django import forms
from .models import Puzzle

class puzzleForm(forms.ModelForm):

    class Meta:
        model = Puzzle
        fields = '__all__'
        