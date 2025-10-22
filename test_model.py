import torch
from PIL import Image
from transformers import  BlipProcessor, BlipForConditionalGeneration


# Loading pre-trained models
MODEL_NAME = "Salesforce/blip-image-captioning-base"
processor = BlipProcessor.from_pretrained(MODEL_NAME)
model = BlipForConditionalGeneration.from_pretrained(MODEL_NAME)

# Loading the image 
def generate_caption(image_path: str) -> str:
    """Generating an caption for the image
    
    Args:
    image_path (str) --> Gives the image path for the function
    
    """
    image = Image.open(image_path).convert("RGB")   
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(**inputs)
    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption

if __name__ == '__main__':
    test_image_path = "test_images\\boytopool.jpeg" 
    
    print(f"Generating caption for {test_image_path}")
    
    caption = generate_caption(test_image_path)

    print(f"""
    Caption:
          {caption}
    """)