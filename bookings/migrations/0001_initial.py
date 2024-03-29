# Generated by Django 4.1 on 2022-08-25 10:43

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
            name='AvailableTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('slug', models.SlugField(max_length=120, unique=True)),
                ('address', models.CharField(max_length=300)),
                ('images', models.ImageField(upload_to='photos/rooms')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('booking_date', models.DateField()),
                ('description', models.TextField(blank=True, max_length=255)),
                ('booking_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('booking_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.availabletime')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.room')),
            ],
        ),
    ]
