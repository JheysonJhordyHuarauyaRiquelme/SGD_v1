from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_admins(apps, schema_editor):
    Usuario = apps.get_model('usuarios', 'Usuario')

    if not Usuario.objects.filter(username='adrian').exists():
        admin_general = Usuario(
            username='adrian',
            tipo='general',
            is_staff=True,
            is_superuser=True,
            password=make_password('db1235879')  # Contraseña segura
        )
        admin_general.save()
        print(f'AdminGeneral creado: {admin_general.username}')

    if not Usuario.objects.filter(username='admin_dojo').exists():
        admin_dojo = Usuario(
            username='admin_dojo',
            tipo='dojo',
            is_staff=True,
            password=make_password('dojopassword')
        )
        admin_dojo.save()
        print(f'AdminDojo creado: {admin_dojo.username}')

def delete_admins(apps, schema_editor):
    Usuario = apps.get_model('usuarios', 'Usuario')
    Usuario.objects.filter(username__in=['adrian', 'admin_dojo']).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_admins, reverse_code=delete_admins),
    ]
