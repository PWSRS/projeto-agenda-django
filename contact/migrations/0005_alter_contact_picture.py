# Generated by Django 5.1.6 on 2025-03-15 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_alter_category_options_contact_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='picture',
            field=models.ImageField(blank=True, upload_to='pictures/%Y/%m/'),
        ),
    ]
