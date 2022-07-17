# Generated by Django 4.0.6 on 2022-07-17 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0003_alter_accountmodel_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountmodel',
            name='document_number',
            field=models.CharField(default=0, help_text='Just Numbers', max_length=14, unique=True),
        ),
        migrations.AddField(
            model_name='accountmodel',
            name='name',
            field=models.CharField(default='name', max_length=100),
        ),
        migrations.AddField(
            model_name='accountmodel',
            name='person_type',
            field=models.CharField(choices=[('NP', 'NATURAL_PERSON'), ('LP', 'LEGAL_PERSON')], default='NP', max_length=2, verbose_name='Person Type'),
        ),
        migrations.AlterField(
            model_name='accountmodel',
            name='balance',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
