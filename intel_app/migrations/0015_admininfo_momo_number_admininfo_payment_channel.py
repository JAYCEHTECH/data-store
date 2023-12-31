# Generated by Django 4.2.4 on 2023-11-05 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intel_app', '0014_topuprequest_credited_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='admininfo',
            name='momo_number',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='admininfo',
            name='payment_channel',
            field=models.CharField(choices=[('MTN Mobile Money', 'MTN Mobile Money'), ('Vodafone Cash', 'Vodafone Cash'), ('AT Money', 'AT Money')], default='MTN Mobile Money', max_length=250),
            preserve_default=False,
        ),
    ]
