# Generated by Django 4.2.4 on 2023-11-05 16:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('intel_app', '0012_agentisharebundleprice_agentmtnbundleprice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='topuprequest',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.CharField(choices=[('User', 'User'), ('Agent', 'Agent')], default='User', max_length=250),
        ),
    ]
