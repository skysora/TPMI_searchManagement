# Generated by Django 3.0.3 on 2020-03-15 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_product_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='hex_number',
            field=models.CharField(default='NA', max_length=255),
        ),
    ]