# Generated by Django 3.0.8 on 2022-10-08 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20221008_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diary_user', to='api.Profile'),
        ),
        migrations.AlterField(
            model_name='diarylike',
            name='diary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diary_like_diary', to='api.Diary'),
        ),
        migrations.AlterField(
            model_name='diarylike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diary_like_user', to='api.Profile'),
        ),
        migrations.AlterField(
            model_name='follow',
            name='follow_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_from_user', to='api.Profile'),
        ),
        migrations.AlterField(
            model_name='follow',
            name='follow_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_to_user', to='api.Profile'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goal_user', to='api.Profile'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='goal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todo_goal', to='api.Goal'),
        ),
        migrations.AlterField(
            model_name='todolike',
            name='todo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todo_like_todo', to='api.Todo'),
        ),
        migrations.AlterField(
            model_name='todolike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todo_like_user', to='api.Profile'),
        ),
    ]