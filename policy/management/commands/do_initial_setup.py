__author__ = 'tdgunes'

from django.core.management.base import BaseCommand, CommandError

from policy.models import User, GlobalSettings


class Command(BaseCommand):
    help = 'Do initial setup by adding a super user and empty fields'

    def handle(self, *args, **options):
        User.objects.all().delete()
        GlobalSettings.objects.all().delete()
        self.stdout.write('Flushed users and setting.')

        url = GlobalSettings(key="url", value="http://127:0.0.0.1:8000")
        url.save()
        self.stdout.write('Successfully added name field to settings.')


        name = GlobalSettings(key="name", value="Test")
        name.save()
        self.stdout.write('Successfully added name field to settings.')


        router = GlobalSettings(key="router", value="http://127.0.0.1:8080")
        router.save()
        self.stdout.write('Successfully added router field to settings.')


        cache = GlobalSettings(key="cache", value="{}")
        cache.save()
        self.stdout.write('Successfully added cache field to settings.')

        cache_last_updated = GlobalSettings(key="cache_last_updated", value="0")
        cache_last_updated.save()
        self.stdout.write('Successfully added cache_last_updated field to settings.')

        cache_update_interval = GlobalSettings(key="cache_update_interval", value="10")  # 10 seconds for testing
        cache_update_interval.save()
        self.stdout.write('Successfully added cache_update_interval field to settings.')

        user = User.objects.create_superuser('tdgunes@gmail.com', '123456')  # wow what a strong password :'(
        user.save()
        self.stdout.write('Successfully added initial super user.')
