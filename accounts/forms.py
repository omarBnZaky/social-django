from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreationForm(UserCreationForm):
    class Meta():
        fields = ('username','email','password1','password2')
        model = get_user_model()

# Here we declare that the our class inherits from the real UserCreationForm class

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label="Display Name"
        self.fields['email'].label="Email Address"

"""
Python super function is a built-in function that returns the proxy object
that allows you to refer parent class by ‘super.’
The super function in Python can be used to gain access to inherited methods,
which is either from the parent or sibling class.
"""
