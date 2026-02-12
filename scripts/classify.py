import pandas as pd
import os
import shutil

DATA_DIR = 'data'
STYLES_FILE = os.path.join(DATA_DIR, 'styles.csv')
IMAGES_DIR = os.path.join(DATA_DIR, 'images')
OUTPUT_DIR = os.path.join(DATA_DIR, 'classified')

def classify_images():
    if not os.path.exists(STYLES_FILE):
        print("styles.csv not found.")
        return

    print("Reading CSV...")
    # Use on_bad_lines='skip' to handle potential formatting issues
    df = pd.read_csv(STYLES_FILE, on_bad_lines='skip')
    
    # Create output directory
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    print(f"Classifying {len(df)} items...")
    
    success_count = 0
    missing_count = 0

    for index, row in df.iterrows():
        try:
            image_id = str(row['id'])
            gender = str(row['gender'])
            article_type = str(row['articleType'])
            
            # Construct filenames
            src_image = os.path.join(IMAGES_DIR, f"{image_id}.jpg")
            
            if not os.path.exists(src_image):
                missing_count += 1
                continue
                
            # Define target directory structure: classified/Gender/ArticleType
            target_dir = os.path.join(OUTPUT_DIR, gender, article_type)
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
                
            target_image = os.path.join(target_dir, f"{image_id}.jpg")
            
            # Copy file (or use shutil.move if you want to save space and delete originals)
            # Using copy for safety.
            if not os.path.exists(target_image):
                shutil.copy2(src_image, target_image)
            
            success_count += 1
            
            if success_count % 1000 == 0:
                print(f"Processed {success_count} images...")
                
        except Exception as e:
            print(f"Error processing row {index}: {e}")

    print("-" * 30)
    print(f"Classification Complete.")
    print(f"Successfully classified: {success_count}")
    print(f"Missing images: {missing_count}")

if __name__ == "__main__":
    classify_images()
