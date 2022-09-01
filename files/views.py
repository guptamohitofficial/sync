from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage

def simple_upload(request):
    if request.method == 'POST' and request.FILES['file']:
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        fs.save(myfile.name, myfile)
    return redirect('/media')
