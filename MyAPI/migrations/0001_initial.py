# Generated by Django 3.0.3 on 2020-07-13 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Approvals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=120)),
                ('lastname', models.CharField(max_length=120)),
                ('dependants', models.IntegerField(default=0)),
                ('applicantincome', models.IntegerField(default=0)),
                ('coapplicatincome', models.IntegerField(default=0)),
                ('loanamt', models.IntegerField(default=0)),
                ('loanterm', models.IntegerField(default=0)),
                ('credithistory', models.IntegerField(default=0)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=150)),
                ('married', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=150)),
                ('graduatededucation', models.CharField(choices=[('Graduate', 'Graduated'), ('Not_Graduate', 'Not_Graduate')], max_length=150)),
                ('selfemployed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=150)),
                ('area', models.CharField(choices=[('Rural', 'Rural'), ('Semiurban', 'Semiurban'), ('Urban', 'Urban')], max_length=150)),
            ],
        ),
    ]