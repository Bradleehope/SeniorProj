# Generated by Django 2.2.5 on 2019-12-02 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('didgUwear', '0004_auto_20191202_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shirt',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
