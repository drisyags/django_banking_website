# Generated by Django 4.1.3 on 2023-01-15 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(max_length=30)),
                ('Student_dob', models.DateField()),
                ('Student_gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('trans', 'Transgender')], max_length=20)),
                ('Student_qualification', models.CharField(max_length=20)),
                ('Course', models.CharField(choices=[('PHP Advanced Full Stack Software Internship', 'PHP Advanced Full Stack Software Internship'), ('PYTHON Advanced Full Stack Software Internship', 'PYTHON Advanced Full Stack Software Internship'), ('JAVA Advanced Full Stack Software Internship', 'JAVA Advanced Full Stack Software Internship'), ('.NET Advanced Full Stack Software Internship', '.NET Advanced Full Stack Software Internship'), ('Software testing advanced internship', 'Software testing advanced internship'), ('Software testing mannual', 'Software testing mannual'), ('Computer networking', 'Computer networking')], max_length=80)),
                ('Mobile_number', models.IntegerField()),
                ('Student_email', models.EmailField(max_length=254)),
                ('Gua_number', models.IntegerField()),
                ('Training_mode', models.CharField(choices=[('Live online', 'Live online'), ('Classroom', 'Classroom')], max_length=20)),
                ('Location', models.CharField(choices=[('Trivandrum', 'Trivandrum'), ('Kochi', 'Kochi'), ('Nagercoil', 'Nagercoil'), ('Online', 'Online')], max_length=30)),
                ('Gua_name', models.CharField(max_length=30)),
                ('Gua_occupation', models.CharField(max_length=30)),
                ('Student_address', models.CharField(max_length=30)),
                ('Student_country', models.CharField(max_length=30)),
                ('Student_state', models.CharField(max_length=30)),
                ('Student_city', models.CharField(max_length=30)),
                ('Student_zipcode', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Student details',
            },
        ),
    ]
