# Generated by Django 5.0.1 on 2024-01-18 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_product_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='type',
            new_name='comments',
        ),
        migrations.AddField(
            model_name='order',
            name='comments',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
