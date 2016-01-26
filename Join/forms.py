from django import forms
from Join.models import Join

# class EmailForm(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField(required=True)

class JoinForm(forms.ModelForm):
    class Meta:
        model = Join
        fields = "__all__" # i had to get this from web search must include all fields.