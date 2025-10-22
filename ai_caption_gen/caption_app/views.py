from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage, FileSystemStorage
from django.core.files.base import ContentFile
from .inference import generate_caption

 

# Create your views here.
# @csrf_exempt
def upload_view(request):
    if request=="POST" and request.FILES.get("image"): 
        image_file = request.FILES["image"]
        # Saving image
        saved_path = default_storage.save(f'uploads/{image_file.name}', ContentFile(image_file.read()))
        user_image_url = default_storage.url(saved_path)
        # Model inference
        try: 
            caption = generate_caption(user_image_url)
            context = {
            'file_url': user_image_url,
            'caption': caption
            }
        except Exception as e:
            return render(request, 'upload.html', {'error': f'Error processing image: {e}'})
        
        return render(request, 'upload.html', context)
    return render(request, 'upload.html')