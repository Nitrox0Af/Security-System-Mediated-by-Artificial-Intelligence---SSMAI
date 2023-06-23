# Generated by Django 4.2.1 on 2023-06-20 02:38

import core.models
from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.CharField(max_length=150, unique=True, verbose_name='E-mail')),
                ('first_access', models.BooleanField(default=True, verbose_name='Primeiro acesso')),
                ('chat_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='Chat ID')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', core.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modified', models.DateField(auto_now=True, verbose_name='Data de atualização')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.CharField(max_length=150, unique=True, verbose_name='E-mail')),
                ('nickname', models.CharField(blank=True, max_length=100, null=True, verbose_name='Apelido')),
                ('relationship', models.CharField(blank=True, max_length=100, null=True, verbose_name='Parentesco')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Proprietário(a)')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modified', models.DateField(auto_now=True, verbose_name='Data de atualização')),
                ('file', stdimage.models.StdImageField(force_min_size=False, upload_to='photo', variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Foto')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100, verbose_name='Slug')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.guest')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Data de acesso')),
                ('hour', models.TimeField(auto_now_add=True, verbose_name='Hora de acesso')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.guest')),
            ],
        ),
    ]
