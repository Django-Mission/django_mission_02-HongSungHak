# Generated by Django 4.0.4 on 2022-04-17 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('supports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='writer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='faq',
            name='content',
            field=models.TextField(verbose_name='질문'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='생성일시'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='view_count',
            field=models.IntegerField(default=0, verbose_name='조회수'),
        ),
    ]
