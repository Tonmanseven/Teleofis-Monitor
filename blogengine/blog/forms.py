from django import forms

class UserForm(forms.Form):

    startDate = forms.CharField(label=False, widget=forms.TextInput(attrs={'style' : 'width: 80px;'}))
    endDate = forms.CharField(label=False, widget=forms.TextInput(attrs={'style' : 'width: 80px;'}))

class SensForm(forms.Form):
    daterange = forms.CharField(label=False, widget=forms.TextInput(attrs={'style': 'width: 80'}))

class FileForm(forms.Form):
    fileform = forms.FileField(label=False)

    