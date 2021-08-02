from io import BytesIO
from django.http import HttpResponse
from xlsxwriter.workbook import Workbook
from .models import Release

def get_excel_file(request):

    output = BytesIO()

    book = Workbook(output)
    sheet = book.add_worksheet('releases')

    releases = Release.objects.all()

    for row, release in enumerate(releases):
        sheet.write(row, 0, release.id)
        sheet.write(row, 1, release.band_name)
        sheet.write(row, 2, release.release_date)
        sheet.write(row, 3, release.is_submitted)

    book.close()

    filename = "releases"

    # construct response
    output.seek(0)
    response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = f"attachment; filename={filename}.xlsx"

    return response