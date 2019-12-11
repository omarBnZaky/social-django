from django.forms import ModelForm
from groups.models import Group
from posts.models import Post
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class CreatePostForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = ('message', 'group')

        def __init__(self, *args, **kwargs):
            # self.fields['user'] = User.id
            user = kwargs.pop('user', None)
            super(CreatePostForm, self).__init__(*args, **kwargs)

            # self.fields['group'].queryset = user.user_groups.all().values_list('name')
            self.fields['group'].queryset = Group.objects.filter(members = user)
