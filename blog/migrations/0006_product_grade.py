# Generated by Django 3.0.3 on 2020-03-15 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200315_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='grade',
            field=models.CharField(default='NA', max_length=255),
        ),
    ]
