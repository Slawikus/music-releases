from django.core.management import BaseCommand
from lxml import etree
from artists.models import Artist


class Command(BaseCommand):
	def add_arguments(self, parser):
		parser.add_argument("path", type=str)

	def handle(self, *args, **options):

		file = open(options["path"], "r")
		parser = etree.XMLParser(recover=True)

		artist = ""
		while True:
			string = file.read(1)
			if string is None:
				break
			artist += string
			if "</artist>" in artist and "<artist>" in artist:
				tree = etree.fromstring(artist, parser=parser)
				artist = ""
				if tree is None:
					print("parse failed")
				else:
					for name in tree.findall(".//name"):
						Artist.objects.get_or_create(name=name.text)
