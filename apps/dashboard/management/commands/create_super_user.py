from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.utils import timezone


class Command(BaseCommand):
    help = "create Super User using positional arguments make single whiteSpace between each argument   "

    #
    # def handle(self, *args, **options):
    #     time = timezone.now().strftime('%X')
    #     self.stdout.write("It's now %s" % time)

    # def add_arguments(self, parser):
    #     parser.add_argument('username', type=str)
    #     parser.add_argument('email', type=str)
    #     parser.add_argument('password', type=str)
    #
    # def handle(self, *args, **kwargs):
    #     username = kwargs['username']
    #     email = kwargs['email']
    #     password = kwargs['password']
    #
    #     User.objects.create_superuser(username=username, email=email, password=password)

    def add_arguments(self, parser):
        parser.add_argument('total', type=int)
        parser.add_argument('-p', type=str)
        parser.add_argument('-a', action="store_true")

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        prefix = kwargs['p']
        admin = kwargs['a']
        for user in range(total):
            if prefix:
                username = '{prefixs}_{random_string}'.format(prefixs=prefix, random_string=get_random_string())
            else:
                username = '{random_string}'.format(random_string=get_random_string())
            if admin:
                User.objects.create_superuser(username=username, email="", password='password')
            else:
                User.objects.create_user(username=username, email="", password='password')

# python manage.py dumpdata dashboard.TechTool --indent 4 > dummy_items.json
# python manage.py loaddata dummy_items.json
