from django import forms

from .models import Idea


class AddIdeaForm(forms.Form):
    title = forms.CharField(max_length=50)
    body = forms.CharField(max_length=1000)

    def save(self, author):
        return Idea.objects.create(
            title=self.cleaned_data['title'],
            body=self.cleaned_data['body'],
            author=author
        )
