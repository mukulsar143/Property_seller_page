# Generated by Django 5.0.3 on 2024-03-30 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('property_owner', 'Property Owner'), ('buyer', 'Buyer')], max_length=20, null=True),
        ),
    ]
