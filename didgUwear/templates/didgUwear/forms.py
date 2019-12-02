from django import forms


class ShirtForm(forms.Form):
    COLOR_CHOICES = (('none', 'None'), ('blue', 'Blue'), ('brown', 'Brown'), ('black', 'Black'),
                     ('gray', 'Gray'), ('green', 'Green'), ('purple', 'Purple'),
                     ('pink', 'Pink'), ('orange', 'Orange'), ('yellow', 'Yellow'),
                     ('white', 'White'))
    STYLE_CHOICES = (('blouse', 'Blouse'), ('tshirt', 'T-Shirt'),
                     ('sweatshirt', 'Sweatshirt'))

    nickname = forms.CharField(label='Nickname', max_length=50)
    primary_color = forms.ChoiceField(label='Primary Color', choices=COLOR_CHOICES)
    style = forms.ChoiceField(label='Style', choices=STYLE_CHOICES)
    secondary_color = forms.ChoiceField(label='Secondary Color', choices=COLOR_CHOICES, required=False)
    occasion = forms.CharField(label='Occasion', max_length=30)
    weather = forms.CharField(label='Weather', max_length=30, required=False)
    pattern = forms.CharField(label='Pattern', max_length=30, required=False)
    holiday = forms.CharField(label='Holiday', max_length=30, required=False)
    description = forms.CharField(label='Description', max_length=100, required=False)
    brand = forms.CharField(label='Brand', max_length=30)
    img_link = forms.ImageField()
