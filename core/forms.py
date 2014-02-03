# -*- coding: utf-8 -*-

from django import forms

class FacebookForm(forms.Form):

    facebook_id = forms.IntegerField()
    access_token = forms.CharField()