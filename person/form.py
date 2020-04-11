#-*- coding: utf-8 -*-
from django import forms
from person.models import person

class PersonForm(forms.Form):
    class meta:
        model = person
        fields  = "__all__"
