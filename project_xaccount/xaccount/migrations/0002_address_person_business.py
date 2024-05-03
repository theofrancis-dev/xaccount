# Generated by Django 4.2.11 on 2024-05-03 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xaccount', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=120)),
                ('address2', models.CharField(blank=True, max_length=120, null=True)),
                ('address3', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('lastupdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email1', models.EmailField(blank=True, max_length=254, null=True)),
                ('email2', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone1', models.CharField(max_length=20)),
                ('phone2', models.CharField(blank=True, max_length=20, null=True)),
                ('phone3', models.CharField(blank=True, max_length=20, null=True)),
                ('lastupdate', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xaccount.address')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity_name', models.CharField(max_length=250)),
                ('fei_ein_number', models.CharField(max_length=20)),
                ('date_filed', models.DateField()),
                ('state', models.CharField(max_length=2)),
                ('status_active', models.BooleanField(default=True)),
                ('business_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xaccount.businesstype')),
                ('mailing_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mailing_address', to='xaccount.address')),
                ('principal_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='principal_address', to='xaccount.address')),
                ('registered_agent_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registered_agent_address', to='xaccount.address')),
                ('reqistered_agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registered_agent', to='xaccount.person')),
            ],
        ),
    ]
