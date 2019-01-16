import requests
from randomuser.models import RandomUser
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('count', help="Count", nargs='*', type=str, default=['5000'])

    def handle(self, *args, **options):
        num_list = options.get('count')
        num = num_list[0]
        if int(num) > 5000:
            num[0] = '5000'
        res = requests.get('https://randomuser.me/api/?results='  + num)
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