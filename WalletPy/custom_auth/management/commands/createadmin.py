from django.conf import settings
from django.core.management.base import BaseCommand
from custom_auth.models import User
from django.contrib.auth import get_user_model

class Command(BaseCommand):

    def handle(self, *args, **options):

        User = get_user_model()
        users = User.objects.all().filter(is_staff=True)
        if users.count() == 0:
            username = "admin"
            email = "admin@admin.fr"
            password = 'admin'
            print('Creating account for %s (%s)' % (username, email))
            admin = User.objects.create_superuser(email=email, username=username, password=password)
            admin.is_active = True
            admin.is_staff = True
            admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')