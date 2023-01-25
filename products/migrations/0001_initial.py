# Generated by Django 4.1.5 on 2023-01-21 09:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_alter_otprequest_request_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=150, verbose_name='مکان')),
                ('category', models.CharField(max_length=100, verbose_name='دسته بندی')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('price', models.PositiveIntegerField(default=0, verbose_name='قیمت')),
                ('address', models.CharField(max_length=150, verbose_name='آدرس')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='accounts.otprequest', verbose_name='کاربر ')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'عکس محصول',
            },
        ),
    ]