from django import forms

from status.models import Status


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image',
        ]

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        if "h" not in content:
            msg = "Must put 'help' in subject when cc'ing yourself."
            self.add_error('cc_myself', msg)
            self.add_error('subject', msg)

