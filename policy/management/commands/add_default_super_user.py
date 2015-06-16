__author__ = 'tdgunes'

from django.core.management.base import BaseCommand, CommandError

from policy.models import User

class Command(BaseCommand):
    help = 'Add default super user for testing'

    def handle(self, *args, **options):
        user = User.objects.create_user('tdgunes@gmail.com', '123456') # wow what a strong password :'(
        user.save()
        self.stdout.write('Successfully added initial super user.')