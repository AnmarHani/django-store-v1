# Generated by Django 3.2.6 on 2021-11-29 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='product.png', upload_to='images')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('stock', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('location', models.CharField(max_length=100)),
                ('payment_type', models.CharField(max_length=100)),
                ('delivery_type', models.CharField(max_length=100)),
                ('likes', models.ManyToManyField(blank=True, null=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
