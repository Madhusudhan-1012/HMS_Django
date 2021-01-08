# Generated by Django 3.0.6 on 2021-01-08 09:26

import django.core.validators
from django.db import migrations, models
import institute.validators


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0007_student_aadhar_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='official',
            name='phone',
            field=models.CharField(max_length=10, validators=[institute.validators.numeric_only]),
        ),
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(validators=[institute.validators.date_no_future]),
        ),
        migrations.AlterField(
            model_name='student',
            name='emergency_phone',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[institute.validators.numeric_only]),
        ),
        migrations.AlterField(
            model_name='student',
            name='parents_phone',
            field=models.CharField(max_length=10, validators=[institute.validators.numeric_only]),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=10, validators=[institute.validators.numeric_only]),
        ),
        migrations.AlterField(
            model_name='student',
            name='regd_no',
            field=models.CharField(max_length=6, unique=True, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.CharField(max_length=6, unique=True, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
    ]