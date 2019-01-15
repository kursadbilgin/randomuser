import requests
from randomuser.models import RandomUser
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('field', help="Count", type=str)

    def handle(self, *args, **options):
        count = options.get('field', 5000)
        if int(count) > 5000:
            count = "5000"
        res = requests.get('https://randomuser.me/api/?results='  + count)
        req = res.json()
        random_users = req.get('results')
        list_ = []
        for user in random_users:
            obj = RandomUser(
                name = user['name']['first'],
                last_name = user['name']['last'],
                mobile_number = user['phone'],
                age = user['dob']['age']
            )
            list_.append(obj)
        RandomUser.objects_randomuser.save_data(list_)