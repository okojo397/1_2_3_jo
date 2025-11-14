from django.db import migrations, models
class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [migrations.CreateModel(
        name='Book',
        fields=[('id', models.BigAutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=80)),
                ('genre', models.CharField(max_length=40)),
                ('summary', models.TextField(blank=True)),
                ('published_at', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True))],
        options={'ordering': ('-published_at','-id')},
    )]
