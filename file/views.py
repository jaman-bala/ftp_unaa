from django.shortcuts import render, get_object_or_404, redirect
from django.http import FileResponse
from .forms import UploadFileForm
from .models import UploadedFile


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()
            uploaded_file.file_size = f'{uploaded_file.file.size} bytes'
            uploaded_file.save()
            return redirect('upload_file')
    else:
        form = UploadFileForm()
    uploaded_files = UploadedFile.objects.all().order_by('-upload_date')
    return render(request, 'upload.html', {'form': form, 'uploaded_files': uploaded_files})


def download_file(request, pk):
    uploaded_file = get_object_or_404(UploadedFile, pk=pk)
    uploaded_file.hits += 1
    uploaded_file.save()
    response = FileResponse(uploaded_file.file)
    return response
