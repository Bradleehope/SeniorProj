# Generated by Django 2.2.5 on 2019-12-02 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('didgUwear', '0003_auto_20191123_0329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pant',
            old_name='fit',
            new_name='pattern',
        ),
        migrations.RenameField(
            model_name='shirt',
            old_name='fit',
            new_name='pattern',
        ),
    ]
