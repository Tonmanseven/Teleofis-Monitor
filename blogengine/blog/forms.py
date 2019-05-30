from django import forms

class UserForm(forms.Form):

    startDate = forms.CharField(label=False, widget=forms.TextInput(attrs={'style' : 'width: 80px;'}))
    endDate = forms.CharField(label=False, widget=forms.TextInput(attrs={'style' : 'width: 80px;'}))

class SensForm(forms.Form):
    daterange = forms.CharField(label=False, widget=forms.TextInput(attrs={'style': 'width: 100'}))
    daterange.widget.attrs.update({'class': 'form-control'})

class FileForm(forms.Form):
    fileform = forms.FileField(label=False)

    