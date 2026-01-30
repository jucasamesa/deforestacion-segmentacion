import zipfile
import os
from PIL import Image
import io

# Paths
docx_path = input("Enter the path to the DOCX file: ")
output_dir = input("Enter the path to the output directory: ")

# Create output directory
os.makedirs(output_dir, exist_ok=True)

def extracts_gifs_from_docx(docx_path):
    with zipfile.ZipFile(docx_path, 'r') as z:
        # Find all GIF files in the media folder
        gif_files = [f for f in z.namelist() if f.startswith('word/media/') and f.endswith('.gif')]
        
        if not gif_files:
            print("No GIF files found in the document.")
            return []
        
        extracted_data = []
        for gif_file in gif_files:
            print(f"Found GIF: {gif_file}")
            # Read the file content
            data = z.read(gif_file)
            extracted_data.append((os.path.basename(gif_file), data))
        
        return extracted_data

def split_gif(image_data, output_folder):
    try:
        with Image.open(io.BytesIO(image_data)) as im:
            print(f"Opening GIF with {im.n_frames} frames")
            
            for i in range(im.n_frames):
                im.seek(i)
                # Create a new image for the frame to avoid palette issues
                frame = im.convert('RGBA')
                frame_path = os.path.join(output_folder, f"frame_{i:02d}.png")
                frame.save(frame_path)
                print(f"Saved {frame_path}")
                
    except Exception as e:
        print(f"Error processing GIF: {e}")

# Main execution
gifs = extracts_gifs_from_docx(docx_path)
for name, data in gifs:
    print(f"Processing {name}...")
    split_gif(data, output_dir)

print("Done.")
