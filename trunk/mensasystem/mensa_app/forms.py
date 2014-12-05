from mensa_app.models import *
from django.forms import *
from django.contrib.admin.models import *
from django.contrib.auth.models import *



class UserForm(ModelForm):
    username = CharField(help_text="Please enter a username.",required=True)
    email = CharField(help_text="Please enter your email.",required=True)
    password = CharField(widget=PasswordInput(),help_text="Please enter a password.",required=True)
    first_name = CharField(help_text="Please enter your first name",required=False)
    last_name = CharField(help_text="Please enter your last name",required=False)
    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email', 'password')

class UserProfileForm(ModelForm):

    mobile = CharField(help_text="Please enter your telephone number")
    phone = CharField(help_text="Please enter your phone")
    skype = CharField(help_text="Please enter your skype")
    department = CharField(help_text="Please enter your department")
    position = CharField(help_text="Please enter your position")
    class Meta:
        model = UserProfile
        fields = ('mobile','skype','department','position')

class ManageTaskForm(ModelForm):
    name = CharField(max_length=255,help_text="Please enter your name")
    description = CharField(max_length=1000,help_text="Please enter your description")
    project = Select()
    actualStartTime = TimeField(help_text="Please select start time")
    actualEndTime = TimeField(help_text="Please select end time")
    planStartTime = DateTimeField(help_text="Please select start time")
    planEndTime = DateTimeField(help_text="Please select end time")
    status = Select()
    user = Select()
    class Meta:
        model = Task
        fields = ('name','description','project',
                  'actualStartTime','actualEndTime','planStartTime',
                  'planEndTime','status','user')

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit
# import floppyforms as forms
#
# class ContactForm(forms.Form):
#
#     name = forms.CharField(required=True)
#     email = forms.EmailField(required=True)
#     subject = forms.CharField(required=True)
#     message = forms.CharField(widget=forms.Textarea)
#
#     def __init__(self, *args, **kwargs):
#         self.helper = FormHelper()
#         self.helper.add_input(Submit('submit', 'Submit'))
#         super(ContactForm, self).__init__(*args, **kwargs)