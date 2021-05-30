from django import forms

class Article_forms(forms.Form):
    title = forms.CharField(
        label="Titulo",
        max_length=100,
        widget=forms.TextInput(
            attrs={
            'placeholders': 'Introduce el titulo'
            }
        )
    )
    content = forms.CharField(
        label="Contenido",
        widget=forms.Textarea,
        required=False
    )

    public_options = [
        (1, 'Si'),
        (0, 'No')
    ]

    public = forms.TypedChoiceField(
        choices = public_options,
        label = "Publicado",
    )
