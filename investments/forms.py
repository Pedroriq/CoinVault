from django import forms
from investments.models import Investment


class InvestmentForm(forms.ModelForm):

    class Meta:
        model = Investment
        fields = '__all__'
        # widgets = {
        #     'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        # }
