import openpyxl
from .models import Release
from configuration.settings import MEDIA_ROOT
from django_countries import countries

FORMATS = ["CD", "Vinyl", "DVD", "Tape"]
STYLES = {"Black Metal": "BM", "Death Metal": "DM", "Trash Metal": "TM"}


def save_excel_file(file, profile):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook.active

    for row in range(2, sheet.max_row + 1):

        format = sheet.cell(row, 6).value
        style = sheet.cell(row, 8).value

        # as django_countries saves country in DB with 2 chars ("New Zealand" -> "NZ")
        # and countries dict looks like {"NZ": "New Zealand"} I had to switch value and key
        # than get short country name
        valid_country = {y: x for x, y in dict(countries).items()}.get(sheet.cell(row, 3).value)

        # reformat DD.MM.YYYY format to YYYY-MM-DD
        valid_date = sheet.cell(row, 4).value.strftime("%Y-%m-%d")

        release = Release(
            band_name=sheet.cell(row, 1).value,
            album_title=sheet.cell(row, 2).value,
            country=valid_country,
            release_date=valid_date,
            media_format_details=sheet.cell(row, 5).value,
            format=format if (format in FORMATS) else "Other",
            limited_edition=sheet.cell(row, 7).value,
            base_style=style if (style in STYLES) else "Other",
            profile=profile,
            sample=f"{MEDIA_ROOT}/audio/releases/dummy.mp3",
            cover_image=f"{MEDIA_ROOT}/images/releases/dummy.jpg",
            label=profile.label.first()

        )

        release.save()