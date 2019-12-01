from django.shortcuts import render
from djano.contrib.urlresolvers import reverse_lazy
from djano.views.generic import CreateView
from . import forms

class SignUp(CreateView):
    """docstring forSignUp."""
    form_class = forms.UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
