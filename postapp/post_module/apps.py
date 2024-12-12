from django.apps import AppConfig
from django.conf import settings

class PostModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post_module'

    def ready(self):
        from django.contrib.auth.models import Group
        from django.db.models.signals import post_save

        def add_to_default_group(sender, instance, created, **kwargs):
            if created:
                group, _ = Group.objects.get_or_create(name="default")
                group.user_set.add(instance)

        # Connect the signal here (outside the function)
        post_save.connect(add_to_default_group, sender=settings.AUTH_USER_MODEL)
