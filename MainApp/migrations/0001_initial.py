# Generated by Django 2.1.1 on 2018-09-17 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vtu_id', models.IntegerField()),
                ('tts_id', models.IntegerField()),
                ('sub_id', models.IntegerField()),
                ('room_id', models.IntegerField()),
                ('seat_id', models.IntegerField()),
                ('date', models.DateField()),
                ('session', models.CharField(choices=[('AN', 'AN'), ('FN', 'FN')], max_length=2)),
            ],
        ),
    ]
