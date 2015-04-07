# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0007_auto_20141225_2212'),
        ('registration', '0004_userprofile_addresses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('phone', models.CharField(max_length=13)),
                ('img', models.ImageField(upload_to=b'businesses')),
                ('offers_left', models.PositiveSmallIntegerField()),
                ('business_description', models.TextField()),
                ('num_customers', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_lmt', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(to='address.Address')),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
        migrations.CreateModel(
            name='BusinessType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=60)),
                ('type_name_ar', models.CharField(max_length=60)),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
        migrations.CreateModel(
            name='DeliveryType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=60)),
                ('type_name_ar', models.CharField(max_length=60)),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(upload_to=b'items')),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('productType', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('chargeTaxes', models.BooleanField()),
                ('shippingRequired', models.BooleanField()),
                ('tags', models.TextField()),
                ('mainImage', models.ImageField(upload_to=b'items')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_lmt', models.DateTimeField(auto_now=True)),
                ('currency', models.ForeignKey(to='address.Currency')),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
        migrations.CreateModel(
            name='ShoppingCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=60)),
                ('category_name_ar', models.CharField(max_length=60)),
                ('business', models.ForeignKey(to='business.Business')),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
        migrations.AddField(
            model_name='productitem',
            name='shoppingCategory',
            field=models.ForeignKey(to='business.ShoppingCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='productitem',
            name='vendor',
            field=models.ForeignKey(to='business.Vendor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='productimage',
            name='productItem',
            field=models.ForeignKey(to='business.ProductItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='business',
            name='business_type',
            field=models.ForeignKey(to='business.BusinessType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='business',
            name='currencies',
            field=models.ManyToManyField(related_name='currencies', to='address.Currency'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='business',
            name='delivery_type',
            field=models.ForeignKey(to='business.DeliveryType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='business',
            name='owner',
            field=models.ForeignKey(related_name='owner', to='registration.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='business',
            name='subscribers',
            field=models.ManyToManyField(related_name='subscribers', to='registration.UserProfile'),
            preserve_default=True,
        ),
    ]
