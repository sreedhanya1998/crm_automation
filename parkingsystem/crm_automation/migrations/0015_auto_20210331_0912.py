# Generated by Django 3.1.6 on 2021-03-31 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_automation', '0014_auto_20210330_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='batch_status',
            field=models.CharField(choices=[('yettobegin', 'yettobegin'), ('completed', 'completed'), ('progress', 'progress')], max_length=120),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='admission_status',
            field=models.CharField(choices=[('admitted', 'admitted'), ('notadmitted', 'notadmitted')], max_length=120),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='enquiry_id',
            field=models.CharField(editable=False, max_length=120, primary_key=True, serialize=False),
        ),
    ]
