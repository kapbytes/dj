# Generated by Django 4.2 on 2023-04-24 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0008_countrytable_apples_countrytable_banana_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='countrytable',
            name='Daycare_or_Preschool',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='countrytable',
            name='English_speaking',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='countrytable',
            name='GDP_per_capita',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='countrytable',
            name='Human_freedom_index',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='countrytable',
            name='International_Primary_School',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='countrytable',
            name='_Life_expectancy',
            field=models.FloatField(default=0),
        ),
    ]
