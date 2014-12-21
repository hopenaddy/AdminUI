from django import forms
from my_app.models import Permissions


class PermissionForm(forms.ModelForm):

    class Meta:
        model = Permissions