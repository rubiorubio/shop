# Generated by Django 3.2.3 on 2021-06-03 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_cart_final_price'),
        ('specs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryfeature',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='categoryfeature',
            name='feature_filter_name',
            field=models.CharField(max_length=50, verbose_name='Filtr name'),
        ),
        migrations.AlterField(
            model_name='categoryfeature',
            name='feature_name',
            field=models.CharField(max_length=50, verbose_name='Feature name'),
        ),
        migrations.AlterField(
            model_name='categoryfeature',
            name='unit',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Unit'),
        ),
        migrations.AlterField(
            model_name='featurevalidator',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='featurevalidator',
            name='feature_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specs.categoryfeature', verbose_name='Feature key'),
        ),
        migrations.AlterField(
            model_name='featurevalidator',
            name='valid_feature_value',
            field=models.CharField(max_length=100, verbose_name='valid feature value'),
        ),
        migrations.AlterField(
            model_name='productfeatures',
            name='feature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specs.categoryfeature', verbose_name='Characteristic'),
        ),
        migrations.AlterField(
            model_name='productfeatures',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product', verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='productfeatures',
            name='value',
            field=models.CharField(max_length=255, verbose_name='Value'),
        ),
    ]
