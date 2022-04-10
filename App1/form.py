from django import forms
from .models import user_profile,comment


class ProfileUpdate(forms.ModelForm):

    class Meta:
        model=user_profile
        fields = ['education','location','bio','image']

class CommentForm(forms.ModelForm):
    content = forms.CharField(label ="", widget = forms.Textarea(
    attrs ={
        'class':'form-control',
        'placeholder':'Comment here !',
        'rows':4,
        'cols':50
    }))
    class Meta:
        model = comment
        fields =['discription']