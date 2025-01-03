# Generated by Django 5.1.4 on 2024-12-23 10:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brand_id', models.AutoField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=255)),
                ('brand_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('colour_id', models.AutoField(primary_key=True, serialize=False)),
                ('colour_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SizeCategory',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('product_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=255)),
                ('category_image', models.ImageField(upload_to='category_images/')),
                ('category_description', models.TextField()),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.productcategory')),
                ('size_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sizecategory')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('product_description', models.TextField()),
                ('model_height', models.FloatField()),
                ('model_wearing', models.CharField(max_length=255)),
                ('care_instructions', models.TextField()),
                ('about', models.TextField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.brand')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.productcategory')),
            ],
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('product_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('original_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('colour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.colour')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_filename', models.ImageField(upload_to='product_images/')),
                ('product_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.productitem')),
            ],
        ),
        migrations.CreateModel(
            name='SizeOption',
            fields=[
                ('size_id', models.AutoField(primary_key=True, serialize=False)),
                ('size_name', models.CharField(max_length=50)),
                ('sort_order', models.IntegerField()),
                ('size_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sizecategory')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariation',
            fields=[
                ('variation_id', models.AutoField(primary_key=True, serialize=False)),
                ('qty_in_stock', models.IntegerField()),
                ('product_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.productitem')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sizeoption')),
            ],
        ),
    ]
