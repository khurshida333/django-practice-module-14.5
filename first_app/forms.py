from django import forms
from .models import Doctor
from django.forms.widgets import NumberInput
import datetime

# class DoctorForm(forms.ModelForm):
#     class Meta:
#         model = Doctor
#         fields = '__all__'

class DoctorForm(forms.Form):
    name = forms.CharField(initial='Your name', max_length=100) #<input type="text" name="name">
    comment = forms.CharField( #<textarea name="comment" placeholder="your comment" rows="3"></textarea>
        widget=forms.Textarea( #defailt row is 10
            attrs={
                'placeholder': 'your comment',
                'rows': 3
                }
            )
        ) 
    email = forms.EmailField(
        label="Please enter your email address",
        required = False,  
    ) #<input type="email" name="email">       #requires an @ symbol 
    agree = forms.BooleanField(initial=False) #set the default as a clicked checkbox
    Today = forms.DateField(initial=datetime.date.today)
    date = forms.DateField() #charfield
    birth_date = forms.DateField(  #adds a calendar
        widget=NumberInput(        #from django.forms.widgets import NumberInput
            attrs={
                'type': 'date'     #<input type="date" name="birth_date">
                }
            )
        )
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(
        widget=forms.SelectDateWidget(
            years=BIRTH_YEAR_CHOICES
            )
        )
    value = forms.DecimalField()   #default widget=NumberInput
    message = forms.CharField(
	     max_length = 10,
	     min_length = 3,
        )  
    
    FavoriteColorChoices = [
       ('blue', 'Blue'),
       ('green', 'Green'),
       ('black', 'Black'),
    ]
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect,choices=FavoriteColorChoices)
    
    #choice model 
    model_choice = forms.ModelChoiceField(
        queryset = Doctor.objects.all(),
        initial = 0
        ) 
    #choice multiple models
    model_choices = forms.ModelMultipleChoiceField(
        widget = forms.CheckboxSelectMultiple,
        queryset = Doctor.objects.all(),
        initial = 0
        )
        # Adding the duration_field
    duration_field = forms.DurationField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Duration in the format: [DD] [HH:[MM:]]ss[.uuuuuu]',
            }
        )
    )
    favorite_food = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=Doctor.FAVORITE_FOOD_CHOICES
    )
