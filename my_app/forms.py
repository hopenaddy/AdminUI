from django import forms


class PermissionForm(forms.Form):
	add_user = forms.BooleanField(required = False)
	change_user = forms.BooleanField(required = False)
	delete_user = forms.BooleanField(required = False)
	change_permission = forms.BooleanField(required = False)