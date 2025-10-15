from django.apps import AppConfig

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

    def ready(self):
        import user.signals
        from django.db.utils import OperationalError
        from django.contrib.auth.models import Group
    
        try:
            Group.objects.get_or_create(name='Admin')
            Group.objects.get_or_create(name='Editor')
            Group.objects.get_or_create(name='Viewer')

        except OperationalError as e:
            return e