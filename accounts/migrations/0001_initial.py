# Generated by Django 4.2 on 2025-05-21 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.genearte_code


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=120)),
                ('address_type', models.CharField(choices=[('Home', 'Home'), ('Office', 'Office'), ('Others', 'Others')], max_length=120)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photo_user')),
                ('code', models.CharField(default=utils.genearte_code.generate_code, max_length=75)),
                ('phone', models.CharField(max_length=25)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profile_address', to='accounts.address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
