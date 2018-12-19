from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from lib import get_text

fs = FileSystemStorage()


def download_img(request):
    if request.method == 'POST':
        lang = request.POST['lang']
        try:
            _file = request.FILES['img']
            _file_name = fs.save(_file.name, _file)
            _file_path = fs.path(_file_name)
            return render(request, 'index.html', get_text(_file_path, lang))
        except Exception as e:
            if str(e) in "'img'":
                return render(request, 'index.html', {})
            return render(request, 'index.html', {'data': e})
    return render(request, 'index.html', {})
