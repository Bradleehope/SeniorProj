from django import forms
from .models import Shirt, Pant

COLOR_CHOICES = (('none', 'None'), ('blue', 'Blue'), ('brown', 'Brown'), ('black', 'Black'),
                 ('gray', 'Gray'), ('green', 'Green'), ('purple', 'Purple'),
                 ('pink', 'Pink'), ('orange', 'Orange'), ('yellow', 'Yellow'),
                 ('white', 'White'))
OCCASION_CHOICES = (('formal', 'Formal'), ('fitness', 'Fitness'), ('sunday', 'Sunday Best'),
                    ('casual', 'Casual'), ('vacation', 'Vacation'), ('other', 'Other'))
WEATHER_CHOICES = (('cold', 'Cold'), ('freezing', 'Freezing'), ('hot', 'Hot'), ('rain', 'Raining'),
                   ('warm', 'Warm'))


class ShirtForm(forms.ModelForm):
    STYLE_CHOICES = (('blouse', 'Blouse'), ('tshirt', 'T-Shirt'), ('sweatshirt', 'Sweatshirt'),
                     ('sweater', 'Sweater'), ('other', 'Other'))
    PATTERN_CHOICES = (('none', 'None'), ('striped', 'Striped'), ('polka_dots', 'Polka Dots'),
                       ('plain', 'Plain'), ('knit', 'Knit'), ('plaid', 'Plaid'),
                       ('graphic', 'Graphic T-Shirt'), ('denium', 'Denium'), ('other', 'Other'))
    HOLIDAY_CHOICES = (('christmas', 'Christmas'), ('halloween', 'Halloween'), ('patriotic', 'Patriotic'),
                       ('other', 'Other'))

    nickname = forms.CharField(label='Nickname', max_length=50)
    img_link = forms.FileField(label='Image Link')
    primary_color = forms.ChoiceField(label='Primary Color', choices=COLOR_CHOICES)
    style = forms.ChoiceField(label='Style', choices=STYLE_CHOICES)
    secondary_color = forms.ChoiceField(label='Secondary Color', choices=COLOR_CHOICES, required=False)
    occasion = forms.ChoiceField(label='Occasion', choices=OCCASION_CHOICES)
    weather = forms.ChoiceField(label='Weather', choices=WEATHER_CHOICES)
    pattern = forms.ChoiceField(label='Pattern', choices=PATTERN_CHOICES)
    holiday = forms.ChoiceField(label='Holiday', choices=HOLIDAY_CHOICES, required=False)
    description = forms.CharField(label='Description', max_length=100, required=False)
    brand = forms.CharField(label='Brand', max_length=30, required=False)

    class Meta:
        model = Shirt
        fields = ('nickname', 'img_link')


class PantForm(forms.ModelForm):
    COLOR_CHOICES = (('none', 'None'), ('blue', 'Blue'), ('brown', 'Brown'), ('black', 'Black'),
                     ('gray', 'Gray'), ('green', 'Green'), ('purple', 'Purple'),
                     ('pink', 'Pink'), ('orange', 'Orange'), ('yellow', 'Yellow'),
                     ('white', 'White'))
    STYLE_CHOICES = (('jeans', 'Jeans'), ('leggings', 'Leggings'), ('sweats', 'Sweats'),
                     ('athletic pants', 'Athletic Pants'), ('jean shorts', 'Jean Shorts'),
                     ('basketball shorts', 'Basketball Shorts'), ('athletic shorts', 'Athletic Shorts'))

    nickname = forms.CharField(label='Nickname', max_length=50)
    img_link = forms.FileField(label='Image Link')
    primary_color = forms.ChoiceField(label='Primary Color', choices=COLOR_CHOICES)
    style = forms.ChoiceField(label='Style', choices=STYLE_CHOICES)
    description = forms.CharField(label='Description', max_length=100, required=False)
    brand = forms.CharField(label='Brand', max_length=30, required=False)

    class Meta:
        model = Pant
        fields = ('nickname', 'img_link')


class PredictionForm(forms.Form):
    color = forms.ChoiceField(label='Primary Color', choices=COLOR_CHOICES)
    weather = forms.ChoiceField(label='Weather', choices=WEATHER_CHOICES)
    occation = forms.ChoiceField(label='Occasion', choices=OCCASION_CHOICES)
