# Generated by Django 4.1 on 2023-08-14 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intel_app', '0011_topuprequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentIshareBundlePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('bundle_volume', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='AgentMTNBundlePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('bundle_volume', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='status',
            field=models.CharField(choices=[('User', 'User'), ('Agent', 'Agent')], default='User', max_length=250),
            preserve_default=False,
        ),
    ]
