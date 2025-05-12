
import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim, peak_signal_noise_ratio as psnr

def compute_quality_metrics(rendered_dir, ground_truth_dir):
    """
    Computes PSNR and SSIM between rendered and ground truth images.
    """
    rendered_images = sorted(os.listdir(rendered_dir))
    ground_truth_images = sorted(os.listdir(ground_truth_dir))

    total_psnr = 0
    total_ssim = 0
    count = 0

    for img_name in rendered_images:
        if img_name in ground_truth_images:
            img1_path = os.path.join(rendered_dir, img_name)
            img2_path = os.path.join(ground_truth_dir, img_name)

            img1 = cv2.imread(img1_path)
            img2 = cv2.imread(img2_path)

            if img1 is None or img2 is None:
                print(f"Skipping {img_name}: could not read image.")
                continue

            if img1.shape != img2.shape:
                print(f"Skipping {img_name}: shape mismatch {img1.shape} vs {img2.shape}.")
                continue

            img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

            image_psnr = psnr(img1_gray, img2_gray, data_range=255)
            image_ssim = ssim(img1_gray, img2_gray, data_range=255)

            total_psnr += image_psnr
            total_ssim += image_ssim
            count += 1

            print(f"{img_name}: PSNR = {image_psnr:.2f}, SSIM = {image_ssim:.4f}")

    if count > 0:
        print(f"\nAverage PSNR: {total_psnr / count:.2f}")
        print(f"Average SSIM: {total_ssim / count:.4f}")
    else:
        print("No valid image pairs found.")

if __name__ == "__main__":
    rendered_dir = "renders/GaussianImages/test/rgb"
    ground_truth_dir = "renders/GaussianImages/test/groundtruthrgb"
    compute_quality_metrics(rendered_dir, ground_truth_dir)
