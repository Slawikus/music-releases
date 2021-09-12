from django.core.management import BaseCommand
import requests
import xml.etree.ElementTree as ET
import gzip
from artists.models import Artist

PATH_TO_NAMES = [
	'artist/name',
	'artist/aliases/name',
	'artist/members/name',
	'artist/namevariations/name',
	'artist/groups/name'
]

class Command(BaseCommand):
	def add_arguments(self, parser):
		parser.add_argument("url", type=str)

	def handle(self, *args, **options):
		response = requests.get(options["url"])
		xml = gzip.decompress(response.content).decode()
		rooted_xml = "<root>" + xml + "</root>"
		parser = ET.XMLParser(encoding="utf-8")
		tree = ET.fromstring(rooted_xml, parser=parser)

		for path in PATH_TO_NAMES:
			for name in tree.findall(path):
				# Artist.objects.create(name=name)
				print(name)
