from PIL import Image
import os
from diffusers import StableDiffusionPipeline
import torch

# Load the Stable Diffusion pipeline
pipeline = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
pipeline.to("cuda")

def upscale_and_enhance_frame(frame_path):
    img = Image.open(frame_path).convert("RGB")
    
    # Resize the image to fit into a 1280x720 frame
    img_upscaled = img.resize((1280, 720), Image.LANCZOS)
    
    # Generate the enhanced image using the diffusion model
    img_tensor = pipeline.feature_extractor(img_upscaled, return_tensors="pt").to("cuda")
    with torch.no_grad():
        enhanced_img = pipeline(img_tensor)["sample"][0]
    
    return enhanced_img

def process_frames(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for frame_file in os.listdir(input_folder):
        frame_path = os.path.join(input_folder, frame_file)
        enhanced_frame = upscale_and_enhance_frame(frame_path)
        enhanced_frame.save(os.path.join(output_folder, frame_file))

if __name__ == "__main__":
    input_folder = "extracted_frames"
    output_folder = "processed_frames"
    process_frames(input_folder, output_folder)
    print("Frame processing completed successfully!")
