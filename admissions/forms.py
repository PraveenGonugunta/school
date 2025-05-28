from django import forms

class admission(forms.Form):
    std_name=forms.CharField(max_length=50)
    std_age=forms.CharField()
    std_id=forms.IntegerField()
