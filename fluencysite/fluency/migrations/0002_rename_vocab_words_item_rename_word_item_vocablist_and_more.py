# Generated by Django 4.0.5 on 2022-07-04 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fluency', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vocab_Words',
            new_name='Item',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='word',
            new_name='vocablist',
        ),
        migrations.RenameField(
            model_name='vocablist',
            old_name='lang',
            new_name='categoryname',
        ),
    ]