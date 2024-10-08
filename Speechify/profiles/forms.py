from django import forms
from Speechify.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "date_of_birth", 'gender', "profile_picture"]  # Add other fields as needed
