from django import forms
from .models import Pizza, Size

# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label='Topping 1', max_length=100, widget=forms.Textarea)
#     topping2 = forms.CharField(label='Topping 2', max_length=100)
    
#     '''This one will be a single line that allows multiple check box toppings'''
#     # toppings = forms.MultipleChoiceField(choices=[('pep', 'Pepperoni'), ('cheese', 'Cheese'), ('olives', 'Olives')], widget=forms.CheckboxSelectMultiple)
#     size = forms.ChoiceField(label='Size', choices=[('Small','Small'),('Medium','Medium'),('Large','Large')]) # Label + value

'''# Form model, with meta info will allow to customize in seconds '''
class PizzaForm(forms.ModelForm):
   
    # image = forms.ImageField()
    
    size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect)
    
    class Meta:
        model = Pizza
        fields = ("topping1","topping2", "size")
        labels = {"topping1": "Topping 1","topping2": "Topping 2", "size": "Size"}
        # widget = {'topping1': forms.Textarea} # We can specify widgets above

class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)