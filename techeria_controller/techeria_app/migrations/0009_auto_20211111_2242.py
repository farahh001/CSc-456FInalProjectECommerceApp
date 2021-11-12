# Generated by Django 3.2.9 on 2021-11-12 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techeria_app', '0008_alter_products_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='laptops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'seller',
            },
        ),
        migrations.AlterModelTable(
            name='sellermodel',
            table=None,
        ),
    ]