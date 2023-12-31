# Generated by Django 4.2.3 on 2023-08-01 23:51

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustumUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[(1, 'ADMIN'), (2, 'PROFESSEUR'), (3, 'ETUDIANT')], default=1, max_length=50)),
                ('photo_profil', models.ImageField(upload_to='media/photo_profil')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Abscence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abscence_data', models.DateField()),
                ('cree_a', models.DateTimeField(auto_now_add=True)),
                ('modifie_a', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Anne_de_session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debut_session', models.CharField(max_length=100)),
                ('fin_session', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse', models.TextField()),
                ('sex', models.CharField(max_length=100)),
                ('cree_a', models.DateTimeField(auto_now_add=True)),
                ('modifier_a', models.DateTimeField(auto_now=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('anne_de_session', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.anne_de_session')),
            ],
        ),
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('cree_a', models.DateTimeField(auto_now_add=True)),
                ('modifier_a', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addresse', models.TextField()),
                ('sex', models.CharField(max_length=100)),
                ('cree_a', models.DateTimeField(auto_now_add=True)),
                ('modifier_a', models.DateTimeField(auto_now=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Professeur_conge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('status', models.IntegerField(default=0)),
                ('cree_a', models.DateTimeField(auto_now_add=True)),
                ('modifie_a', models.DateTimeField(auto_now_add=True)),
                ('professeur_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.professeur')),
            ],
        ),
        migrations.CreateModel(
            name='Prof_Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('cree_a', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=0, null=True)),
                ('prof_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.professeur')),
            ],
        ),
        migrations.CreateModel(
            name='Prof_message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('reponse_message', models.TextField()),
                ('status', models.IntegerField(default=0)),
                ('cree_a', models.DateTimeField(auto_now_add=True)),
                ('modifie_a', models.DateTimeField(auto_now_add=True)),
                ('prof_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.professeur')),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('groupe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.groupe')),
                ('professeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.professeur')),
            ],
        ),
        migrations.CreateModel(
            name='EtudiantResultat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('controle_note', models.IntegerField()),
                ('exam_note', models.IntegerField()),
                ('cree_a', models.DateTimeField(auto_now_add=True)),
                ('modifie_a', models.DateTimeField(auto_now_add=True)),
                ('etudiant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.etudiant')),
                ('matiere_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.matiere')),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant_Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('cree_a', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=0, null=True)),
                ('etudiant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.etudiant')),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant_message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('message_reponse', models.TextField()),
                ('status', models.IntegerField(default=0)),
                ('cree_a', models.DateTimeField(auto_now_add=True)),
                ('modifie_a', models.DateTimeField(auto_now_add=True)),
                ('etudiant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.etudiant')),
            ],
        ),
        migrations.AddField(
            model_name='etudiant',
            name='groupe_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.groupe'),
        ),
        migrations.CreateModel(
            name='Abscence_Raport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cree_a', models.DateTimeField(auto_now_add=True)),
                ('modifie_a', models.DateTimeField(auto_now_add=True)),
                ('abscence_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.abscence')),
                ('etudiant_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.etudiant')),
            ],
        ),
        migrations.AddField(
            model_name='abscence',
            name='anne_session_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.anne_de_session'),
        ),
        migrations.AddField(
            model_name='abscence',
            name='matiere_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.matiere'),
        ),
    ]
