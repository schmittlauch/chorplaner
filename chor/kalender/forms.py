from django import forms

class NewTerminForm(forms.Form):
    name = forms.CharField(label="Name",max_length=100)
    date = forms.DateField(label="Datum", initial='dat')
    time = forms.TimeField(label="Zeit")
    description = forms.CharField(label="Beschreibung",widget=forms.Textarea)
    category = forms.CharField(label="Kategorie:",required=False,widget=forms.TextInput(attrs={'onblur':"fill()", 'onkeyup':"suggest_req(this.value);", 'autocomplete':"off"}))
    participants = forms.BooleanField(label="Nimmst du teil?",required=False,initial=True)
