from django import forms
from .models import Resume
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = ('StudentName', 'ProjectsandInternships', 'StudentId','Branch','PhoneNumber', 'Cgpa', 'TenthMarks', 'TenthSchoolName', 'TwelthMarks', 'TwelthCollegeName',)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
    def __init__(self, *args, **kwargs):

        super(SignUpForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            help_text = self.fields[field].help_text
            self.fields[field].help_text = None
            if help_text != '':
                self.fields[field].widget.attrs.update(
                    {'class': 'has-popover', 'data-content': help_text, 'data-placement': 'right',
                     'data-container': 'body'})











