# Generated by Django 4.0.3 on 2022-10-12 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_name',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='crud.category'),
        ),
    ]
