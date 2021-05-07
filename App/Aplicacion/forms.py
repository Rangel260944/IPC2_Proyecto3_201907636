from django import forms


class EntradaForm(forms.Form):
    file = forms.FileField(label="file")
    #textarea = forms.CharField(widget=forms.Textarea(attrs={"rows":20, "cols":60}))
