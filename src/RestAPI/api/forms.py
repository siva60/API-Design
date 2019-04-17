from django import forms

from updates.models import Update as UpdateModel


class UpdateModelForm(forms.ModelForm):
    class Meta:
        model = UpdateModel
        fields = [
            'user',
            'content',
            'image',
        ]

    # to validate if any data is the post request is valid and not empty.
    # In this case if 'content' field and image field must be entered.
    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        content = data.get('content', None)
        if content == '':
            content = None
        image = data.get('image', None)
        if content is None and image is None:
            raise forms.ValidationError('Content or Image is required')
        return super().clean()  # ensures any validation logic in parent classes is maintained.




