# Generated by Django 4.0.3 on 2022-10-12 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
    ]