# Generated by Django 4.2.7 on 2023-11-02 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user_profile.models
import uuid
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive'), ('DRAFT', 'DRAFT'), ('REMOVED', 'Removed')], db_index=True, default='ACTIVE', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, choices=[('FEMALE', 'Female'), ('MALE', 'Male'), ('UNKNOWN', 'Unknown'), ('OTHER', 'Other')], max_length=10, null=True)),
                ('blood_group', models.CharField(blank=True, choices=[('NOT_SET', 'Not Set'), ('A+', 'A Positive'), ('A-', 'A Negative'), ('B+', 'B Positive'), ('B-', 'B Negative'), ('AB+', 'Ab Positive'), ('AB-', 'Ab Negative'), ('O+', 'O Positive'), ('O-', 'O Negative')], max_length=10, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('photo', versatileimagefield.fields.VersatileImageField(default=user_profile.models.default_profile_photo, upload_to='images/profile/', verbose_name='profile_image')),
                ('full_address', models.TextField(blank=True, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=15, max_digits=20, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=15, max_digits=20, null=True)),
                ('facebook_link', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram_link', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter_link', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin_link', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]