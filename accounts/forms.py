from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _



class UserCreateForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=60)
    last_name = forms.CharField(max_length=60)
    # groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), initial=Group.objects.get(id=1), disabled=True)
    # groups = forms.ModelChoiceField(queryset=Group.objects.all(), initial=Group.objects.get(id=1), disabled=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


    class Meta:
        model = User
        fields = ("username", "email", 'first_name', 'last_name', "password1", "password2")    # 'groups'
     

