# Generated by Django 4.0.6 on 2022-07-18 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0004_accountmodel_document_number_accountmodel_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountmodel',
            name='balance',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transactionmodel',
            name='credited_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credited_account', to='banking.accountmodel'),
        ),
        migrations.AlterField(
            model_name='transactionmodel',
            name='debited_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debited_account', to='banking.accountmodel'),
        ),
    ]
