from django.shortcuts import render

# Create your views here.
def upload_view():
    return render(request, 'upload.html')