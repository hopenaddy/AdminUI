from django import forms
from my_app.models import Permissions


class PermissionForm(forms.ModelForm):

    # add_user= forms.BooleanField()
    # change_user = forms.BooleanField()
    # delete_user= forms.BooleanField()
    
    # def __init__(self):
    #     self.fields['receieve_newsletter'].initial  = True

    class Meta:
        model = Permissions