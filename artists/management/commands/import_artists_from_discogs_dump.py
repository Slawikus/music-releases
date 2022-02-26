from django.core.management import BaseCommand
from artists.models import Artist
import re


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("path", type=str)

    def handle(self, *args, **options):

        file = open(options["path"], "r")
        while True:
            string = file.read(1024 * 10)
            if string is None:
                file.close()
                break
            res = re.findall(r"<name>[a-zA-Z0-9 ]+</name>", string)
            for name in res:
                Artist.objects.get_or_create(name=name[6:-7])
