# Generated by Django 2.2.19 on 2021-02-25 03:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='姓')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='名')),
                ('tel', models.CharField(blank=True, max_length=100, null=True, verbose_name='電話番号')),
                ('remarks', models.TextField(blank=True, default='', verbose_name='備考')),
                ('start', models.DateTimeField(default=django.utils.timezone.now, verbose_name='開始時間')),
                ('end', models.DateTimeField(default=django.utils.timezone.now, verbose_name='終了時間')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Staff', verbose_name='スタッフ')),
            ],
        ),
    ]
