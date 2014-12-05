from mensa_app.models import *
from django.forms import *
from django.contrib.admin.models import *
from django.contrib.auth.models import *
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
# from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from timesheet.models import *

# class UserTimeSheetForm(Form):
#     special = CheckboxChoiceInput()
#     class Meta:
#         model = UserTimeSheet
#         exclude = ['user']
#
# class SettingsForm(forms.ModelForm):
#
#     receive_newsletter = forms.BooleanField()
#
#     # def __init__(self):
#     #     if check_something():
#     #         self.fields['receieve_newsletter'].initial  = True
#
#     class Meta:
#         model = Settings