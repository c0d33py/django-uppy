from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.shortcuts import HttpResponse
from django.http import JsonResponse


class DemoClientView(TemplateView):
    # template_name = "tus.html"
    template_name = "uppy.html"


def FileUpload(request):

    folder = 'media/'
    if request.method == 'POST':
        myfile = request.FILES['upload']

        fs = FileSystemStorage(location=folder)  # defaults to   MEDIA_ROOT
        filename = fs.save(myfile.name, myfile)
        file_url = fs.url(filename)
        print(file_url)

        return JsonResponse({'succes': True}, status=200)
    return JsonResponse({'succes': False, 'errors': []}, status=400)
