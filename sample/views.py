from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'sample/index.html')


# sample_app/views.py
from django.core.files.storage import default_storage

def image(request):
    file = request.FILES['image']
    filename = default_storage.save(file.name, file)
    file_url = default_storage.url(filename)
    print(filename, file_url)
    return render(request, 'sample/index.html')