# -*- coding: utf-8 -*-
#Copyright (C) 2012  Oliver Schmidt
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as
#published by the Free Software Foundation, either version 3 of the
#License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU Affero General Public License for more details.

from django import forms
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput

class NewTerminForm(forms.Form):
    name = forms.CharField(label="Name",max_length=100)
    date = forms.DateField(label="Datum", initial='dat',widget=BootstrapDateInput)
    time = forms.TimeField(label="Zeit")
    description = forms.CharField(label="Beschreibung",widget=forms.Textarea)
    category = forms.CharField(label="Kategorie:",required=False,widget=forms.TextInput(attrs={'onblur':"fill()", 'onkeyup':"suggest_req(this.value);", 'autocomplete':"off"}))
    participants = forms.BooleanField(label="Ich nehme teil",required=False,initial=True)
