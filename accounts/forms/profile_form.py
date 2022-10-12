from django import forms
from django.core.exceptions import ValidationError

from ..models import Profile


class ProfileForm(forms.ModelForm):

    bio = forms.CharField(
        max_length=120,
        required=False,
        widget=forms.Textarea
    )
    image = forms.ImageField(
        required=False
    )

    class Meta:
        model = Profile
        fields = ('surname', 'bio', 'image',)

