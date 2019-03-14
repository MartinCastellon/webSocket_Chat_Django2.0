from django import forms


class ComposeForm(forms.Form):
    Mensaje = forms.CharField(
            widget=forms.TextInput(
                attrs={"class": "form-control"}
                )
            )
