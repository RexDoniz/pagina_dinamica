# Generated by Django 5.1.3 on 2024-11-22 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_item_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='codigo',
            field=models.CharField(default='dsadsadsa', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
