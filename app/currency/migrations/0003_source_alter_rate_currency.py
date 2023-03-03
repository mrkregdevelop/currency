# Generated by Django 4.1.6 on 2023-03-03 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_rate_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='rate',
            name='currency_new',
            field=models.PositiveSmallIntegerField(choices=[(2, 'Dollar'), (1, 'Euro')]),
        ),
    ]
