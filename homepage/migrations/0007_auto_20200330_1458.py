# Generated by Django 3.0.4 on 2020-03-30 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_auto_20200330_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privatepicture',
            name='private_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='picture', to='homepage.PrivateItem'),
        ),
    ]
