# Generated by Django 4.2.8 on 2023-12-07 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_category_options_product_is_sale_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categoty',
            new_name='category',
        ),
    ]
