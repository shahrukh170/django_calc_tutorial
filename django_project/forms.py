from django import forms
 
# creating a form
class CalcForm(forms.Form):
    num1 = forms.IntegerField()
    num2 = forms.IntegerField()