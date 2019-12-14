from django import forms
from .models import Shirt


class ShirtForm(forms.ModelForm):
    COLOR_CHOICES = (('none', 'None'), ('blue', 'Blue'), ('brown', 'Brown'), ('black', 'Black'),
                     ('gray', 'Gray'), ('green', 'Green'), ('purple', 'Purple'),
                     ('pink', 'Pink'), ('orange', 'Orange'), ('yellow', 'Yellow'),
                     ('white', 'White'))
    STYLE_CHOICES = (('blouse', 'Blouse'), ('tshirt', 'T-Shirt'), ('sweatshirt', 'Sweatshirt'),
                     ('sweater', 'Sweater'), ('other', 'Other'))
    OCCASION_CHOICES = (('formal', 'Formal'), ('fitness', 'Fitness'), ('sunday', 'Sunday Best'),
                        ('casual', 'Casual'), ('vacation', 'Vacation'), ('other', 'Other'))
    WEATHER_CHOICES = (('cold', 'Cold'), ('freezing', 'Freezing'), ('hot', 'Hot'), ('rain', 'Raining'),
                       ('warm', 'Warm'))
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
