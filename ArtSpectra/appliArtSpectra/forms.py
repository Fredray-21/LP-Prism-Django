from django import forms
from appliArtSpectra.models import Oeuvre
from django.db.models.functions import Cast
from django.db.models import CharField

class OeuvreUpdateForm(forms.ModelForm):
    class Meta:
        model = Oeuvre
        fields = ['nomOeuvre', 'dateCreationOeuvre', 'descriptionOeuvre', 'dimensionOeuvre', 'imageOeuvre', 'prixOeuvre', 'quantiteOeuvre', 'slug']

    def __init__(self, *args, **kwargs):
        super(OeuvreUpdateForm, self).__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            current_slug = instance.slug
            self.fields['slug'] = forms.ChoiceField(choices=self.get_slug_choices(current_slug))

    def get_slug_choices(self, current_slug):
        slug_choices = Oeuvre.objects.exclude(slug=current_slug).values_list('slug', 'slug').distinct()
        choices = [(current_slug, current_slug)] + list(slug_choices)
        return choices


class OeuvreCreateForm(forms.ModelForm):
    class Meta:
        model = Oeuvre
        fields = ['nomOeuvre', 'dateCreationOeuvre', 'descriptionOeuvre', 'dimensionOeuvre', 'imageOeuvre', 'prixOeuvre', 'quantiteOeuvre', 'slug']

    def __init__(self, *args, **kwargs):
        super(OeuvreCreateForm, self).__init__(*args, **kwargs)
        self.fields['slug'] = forms.ChoiceField(choices=self.get_slug_choices())

    def get_slug_choices(self):
        slug_choices = Oeuvre.objects.values_list('slug', 'slug').distinct()
        return slug_choices

