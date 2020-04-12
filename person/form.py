# -*- coding: utf-8 -*-
from django import forms
from person.models import person


class PersonForm(forms.ModelForm):
    class Meta:
        model = person
        fields = "__all__"
