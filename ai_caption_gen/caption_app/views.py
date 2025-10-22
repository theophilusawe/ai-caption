from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
 

# Create your views here.
@csrf_exempt
def upload_view(request):
    if request=="POST" and request.FILES.get("image"):
        image_file = request.FILES["image"]

        # Saving image
        saved_path = default_storage.save(f'uploads/{image_file.name}', ContentFile(image_file.read()))
        image_url = default_storage.url(saved_path)

        # Model Inference
    return render(request, 'upload.html')