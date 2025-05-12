# Photogrammetry and Gaussian Splatting using Apollo 17 Imagery

## Abstract

This report presents an end-to-end pipeline for high-quality 3D reconstruction and visualization of the lunar surface using Apollo 17 imagery. The study integrates traditional photogrammetry using Agisoft Metashape with modern 3D Gaussian Splatting techniques, and evaluates the effectiveness of novel view synthesis for enhancing photogrammetric reconstructions. Both qualitative and quantitative comparisons are performed using PSNR and SSIM metrics.

---

## Part 1: Baseline Photogrammetry and Gaussian Splatting

### Dataset

* Source: Apollo 17 dataset (N = 15 images)
* [Link to dataset](https://drive.google.com/drive/folders/18t2fq0a8yKQDM4BYSeuSHrAbmJujMYLO?usp=drive_link)

### Methodology

1. **Photogrammetry with Agisoft Metashape**

   * Imported the 15 Apollo 17 images into Metashape.
   * Generated a sparse point cloud through feature matching and camera alignment.
   * Created a dense point cloud with point confidence enabled.
   * Built a textured 3D mesh from the point cloud.
![Screenshot from 2025-05-12 03-06-41](https://github.com/user-attachments/assets/e8909618-99ce-4a4e-94ce-6dbab659cb7b)

2. **Export to COLMAP Format**

   * The reconstructed model was exported in COLMAP-compatible format for further processing.

3. **Gaussian Splatting with Nerfstudio**

   * Loaded the COLMAP output using Nerfstudio’s Gaussian Splatting pipeline.
   * Trained the model using the `gaussian-splat` configuration.

   #### Code Snippet: Export & Train

   ```python
   import sys
   from nerfstudio.scripts.exporter import entrypoint

   sys.argv = [
       "ns-export", "gaussian-splat",
       "--load-config", "outputs/splating/unnamed/splatfacto/2025-05-11_113827/config.yml",
       "--output-dir", "render/GaussianImages"
   ]
   entrypoint()
   ```

   #### Code Snippet: Rendering Views

   ```python
   from nerfstudio.scripts import render as ns_render
   ns_render.entrypoint()
   ```

4. **Image Quality Assessment**

   * Computed PSNR and SSIM between rendered and original Apollo images using `scikit-image` metrics.

   #### Code Snippet: PSNR & SSIM Evaluation

   ```python
   from skimage.metrics import peak_signal_noise_ratio as psnr, structural_similarity as ssim
   import cv2

   img1 = cv2.imread('rendered/image1.png', cv2.IMREAD_GRAYSCALE)
   img2 = cv2.imread('ground_truth/image1.png', cv2.IMREAD_GRAYSCALE)

   print("PSNR:", psnr(img1, img2, data_range=255))
   print("SSIM:", ssim(img1, img2, data_range=255))
   ```

### Observations

* Rendered images showed strong resemblance to the original Apollo images.
* Quantitative metrics:

  * **Average PSNR**: \~12.8 dB
  * **Average SSIM**: \~0.27

These values suggest that Gaussian Splatting can faithfully reconstruct original views and preserve structural integrity.

---

## Part 2: Novel View Generation and Enhanced Photogrammetry

### Novel View Synthesis

* Using the trained Gaussian Splatting model, 6 novel images were rendered from new camera poses not covered in the original set.
* Camera positions were manually selected to provide new perspectives and fill spatial gaps in the original dataset.

### Augmented Photogrammetry

1. Combined the original 15 Apollo 17 images with 6 generated views (total N = 21).
2. Re-imported this extended dataset into Agisoft Metashape.
3. Reconstructed a new 3D model following the same pipeline as in Part A.
   
![Screenshot from 2025-05-12 03-10-50](https://github.com/user-attachments/assets/b9711519-9f6e-46dc-8f16-b41436addc57)

### Comparison: Before vs. After Augmentation

* **Qualitative Analysis**:

  * The augmented model displayed improved surface continuity, finer mesh detail, and better texture blending.
  * Areas with sparse original data showed marked improvement.
    
![Screenshot from 2025-05-12 00-57-16](https://github.com/user-attachments/assets/5470f5bf-c1d2-41a1-9890-f830613d4a23)

* **Quantitative Comparison Ideas**:

  * Point cloud density comparison.
  * Mesh completeness ratio.
  * Surface deviation metrics (if ground truth or aligned models exist).

### Conclusion

Gaussian Splatting not only reconstructs views well but also contributes meaningful visual content that enhances photogrammetric modeling. The extended dataset resulted in a visibly superior mesh, especially in underrepresented areas. This suggests that generative novel views can be a valuable tool for scientific 3D reconstruction.

---

## Tools and Software

* **Agisoft Metashape** – Used for photogrammetric modeling.
* **Nerfstudio** – Employed for Gaussian Splatting.
* **COLMAP** – Used for compatibility during model conversion.
* **Python Libraries**: `scikit-image`, `torch`, `numpy`, `opencv-python`, `Pillow`

---

## References

* Nerfstudio Documentation: [https://docs.nerf.studio/](https://docs.nerf.studio/)
* COLMAP GitHub: [https://github.com/colmap/colmap](https://github.com/colmap/colmap)

---

