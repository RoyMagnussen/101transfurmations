from django import forms
from .models import Review
from django.forms import widgets

# Create your forms here.


class ReviewCreationForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=False, widget=widgets.TextInput(attrs={
                           'placeholder': 'Optional'}), label='Name', help_text='255 characters or less. Leave blank to be anonymous.')
    comment = forms.CharField(max_length=2000, widget=widgets.Textarea(
        attrs={'placeholder': 'Required'}), label='Comment', help_text='2000 characters or less.')

    class Meta:
        model = Review
        fields = ['name', 'comment']

    def __init__(self, *args, **kwargs):
        super(ReviewCreationForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control rounded-0'
