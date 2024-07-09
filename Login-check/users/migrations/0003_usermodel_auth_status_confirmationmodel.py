# Generated by Django 5.0.4 on 2024-07-03 14:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_usermodel_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='auth_status',
            field=models.CharField(choices=[('NEW', 'NEW'), ('CODE_VERIFIED', 'CODE_VERIFIED'), ('DONE', 'DONE')], default='NEW', max_length=128),
        ),
        migrations.CreateModel(
            name='ConfirmationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration_time', models.DateField()),
                ('is_confirmed', models.BooleanField(default=False)),
                ('code', models.CharField(max_length=8, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verification_codes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]