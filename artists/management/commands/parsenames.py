from django.core.management import BaseCommand
from lxml import etree
from artists.models import Artist


class Command(BaseCommand):
	def add_arguments(self, parser):
		parser.add_argument("path", type=str)

	def lazy_read(self, file):
		while True:
			data = file.read(1024)
			if not data:
				break
			yield data

	def handle(self, *args, **options):

		file = open(options["path"], "r")
		parser = etree.XMLParser(recover=True)

		for xml in self.lazy_read(file):

			tree = etree.fromstring(xml, parser=parser)

			for name in tree.findall(".//name"):
				# Artist.objects.get_or_create(name=name.text)
				print(name.text)
