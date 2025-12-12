# 2025 OpenSource SW – Folder Image Batch Converter

A **Python-based Command Line Interface (CLI) tool** that processes multiple image files in batch by reading them from a folder and applying image transformations such as **resize, grayscale conversion, and blur**.

This project automates repetitive image processing tasks and improves efficiency when handling large collections of images.

---

## 1. Project Overview

### 1.1 Background
When working with multiple images, applying identical transformations manually using image editing software can be inefficient and time-consuming.  
This project was developed to address this issue by enabling **folder-based batch image processing** through a simple command-line interface.

### 1.2 Purpose
- Automate repetitive image processing tasks
- Provide a simple and intuitive CLI-based workflow
- Improve productivity when handling large image datasets
- Practice modular Python programming and open-source project structure

### 1.3 Key Features
- Batch processing of images in a specified folder
- Multiple processing modes selectable via command-line options
- Automatic output directory creation
- Original file names preserved after processing

### 1.4 Supported Processing Modes

| Mode   | Description |
|--------|-------------|
| resize | Resize images to a specified width and height |
| gray   | Convert images to grayscale |
| blur   | Apply Gaussian blur to images |

### 1.5 Supported Image Formats
- .jpg, .jpeg
- .png
- .bmp
- .gif

---

## 2. Demo / Example Images

This section provides visual examples of each image processing feature supported by the program.

For demonstration purposes, the example commands use the `examples/input` directory as the input folder.  
Users may specify a different input directory when running the program. 
All examples below are generated using the same fixed input images.
Demo images and result files can be found in the following directories:

- Input images:
  - `2025-opensw-folder-image-batch-converter/examples/input`

- Processed result images:
  - Resize results: `2025-opensw-folder-image-batch-converter/examples/result_resize`
  - Grayscale results: `2025-opensw-folder-image-batch-converter/examples/result_gray`
  - Blur results: `2025-opensw-folder-image-batch-converter/examples/result_blur`

### Fixed Input Images (Common for All Demos)

The following images are used as the base input for all processing modes:

- ![univ](https://github.com/user-attachments/assets/f7a99bf1-86fa-488a-8643-4233bfbf12f4)
- <img width="1958" height="1080" alt="mascot3d" src="https://github.com/user-attachments/assets/aa2e1984-4515-4fb8-9105-6401486cf703" />
- <img width="1714" height="1080" alt="generalSigns" src="https://github.com/user-attachments/assets/c6eb64c2-43fe-4470-9db7-7b50b1e2b85b" />




These images remain unchanged and are reused across all feature demonstrations below.

---

### 2.1 Resize Feature Demo

Demonstrates the image resizing functionality, where all input images are resized to a fixed resolution.

**Output Images (Resize Mode):**
- ![univ](https://github.com/user-attachments/assets/2fb976bc-caa8-4bab-ab62-98a74e5ba7fe)
- <img width="300" height="300" alt="mascot3d" src="https://github.com/user-attachments/assets/6e9598a5-5c9e-457a-b7f3-233d243a3200" />
- <img width="300" height="300" alt="generalSigns" src="https://github.com/user-attachments/assets/3ab35bd0-30a3-4ba5-a0eb-249d1638f9a5" />


**Description:**
- All input images are resized to the specified width and height (In this example, 300 * 300).
- The resize operation is applied uniformly to all images in the input folder.
- Output images preserve the original file names or follow a consistent naming rule.

---

### 2.2 Grayscale Conversion Demo

Demonstrates the grayscale conversion feature, which removes color information from images.

**Output Images (Grayscale Mode):**
- ![univ](https://github.com/user-attachments/assets/805391d9-dcc7-409f-82ee-7a6a251fc697)

- <img width="1958" height="1080" alt="mascot3d" src="https://github.com/user-attachments/assets/727ddf45-fb90-4f9e-ad9a-be8763d38c78" />

- <img width="1714" height="1080" alt="generalSigns" src="https://github.com/user-attachments/assets/49de2618-c85c-4509-acc4-adf91d7863b8" />


**Description:**
- Each input image is converted from color to grayscale.
- Only intensity information is preserved.
- No additional parameters are required for this mode.

---

### 2.3 Blur Effect Demo

Demonstrates the blur feature, which applies a Gaussian blur to images.


**Output Images (Blur Mode):**
- ![univ](https://github.com/user-attachments/assets/b50b4507-04b7-4fe7-9fe7-11e077253d4a)
- <img width="1958" height="1080" alt="mascot3d" src="https://github.com/user-attachments/assets/01b9d0cd-b82e-41de-91b3-14dfbadcf349" />
- <img width="1714" height="1080" alt="generalSigns" src="https://github.com/user-attachments/assets/dcfe562c-53f3-4578-b9a5-e01127f8e6d4" />


**Description:**
- A Gaussian blur filter is applied to each input image.
- The blur intensity depends on the kernel size (`ksize`) parameter.
- Larger kernel sizes produce stronger blur effects.


---

## 3. Dependencies & Installation

### 3.1 Development Environment
- Python: version 3.x
- Operating Systems: Windows, macOS, Linux

### 3.2 Required Libraries

| Package         | Description |
|-----------------|-------------|
| opencv-python   | Image loading and image processing |
| numpy           | Numerical operations and image array handling |

### 3.3 Installation Guide

Create a virtual environment (recommended):

- python -m venv .venv

Activate the virtual environment:

- Windows: .\.venv\Scripts\activate  
- macOS / Linux: source .venv/bin/activate

Install required packages:

- pip install opencv-python numpy

Installed package versions can be checked using:

- pip show opencv-python  
- pip show numpy

---

## 4. How to Run

### 4.1 Clone the Repository
- git clone https://github.com/Jaeuk-Han/2025-opensw-folder-image-batch-converter.git

### 4.2 Move to the Project Directory
- cd 2025-opensw-folder-image-batch-converter

---

### 4.3 Input and Output Directory Structure

Before running the program, users must prepare the input images and understand how input and output folders are handled.

#### Input Directory (User-Defined)

- The input directory is specified by the user using the `-i` or `--input` option.
- Users must **place the images they want to process in advance** into the chosen input folder.
- Only image files located directly inside the input folder are processed.
- Subdirectories are not scanned.
- Supported image formats: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`

Example input folder:
examples/input/
├─ image1.png
├─ image2.jpg
└─ image3.jpeg

---

#### Output Directory (User-Defined)

- The output directory is specified using the `-o` or `--output` option.
- The value provided becomes the **name and location of the output folder**.
- If the specified output folder does not exist, it is **automatically created** by the program.
- Each execution can generate a different output folder depending on the processing mode or user preference.

Example output folders:
examples/result_resize/
examples/result_gray/
examples/result_blur/

---

### 4.4 Basic Command Structure

All commands must be executed from the **project root directory**.

- python -m img_batch.main -i examples/input -o OUTPUT_FOLDER -m MODE [OPTIONS]

Explanation:
- `INPUT_FOLDER`  
  User-specified input directory containing images to be processed.
- `OUTPUT_FOLDER`  
  The folder name or path where processed images will be saved.
- `MODE`  
  Processing mode: `resize`, `gray`, or `blur`.

---
### 4.5 Execution (Detailed)

In this project, **both the input directory and the output directory are specified by the user**.  
Users must prepare the input folder in advance and choose an output folder name when executing the program.

---

### 4.5.1 Resize Images

Resizes all images in the specified input directory to a user-defined resolution.

**Command Template:**
- python -m img_batch.main -i INPUT_FOLDER -o OUTPUT_FOLDER -m resize --width WIDTH --height HEIGHT

**Command Example:**
- python -m img_batch.main -i examples/input -o examples/result_resize -m resize --width 300 --height 300

**Explanation:**
- Reads all supported image files from `INPUT_FOLDER`.
- Resizes each image to the specified width and height.
- Saves resized images into `OUTPUT_FOLDER`.
- The output folder is automatically created if it does not exist.

**Configurable Parameters:**
- `INPUT_FOLDER`  
  Path to the folder containing images to be processed.
- `OUTPUT_FOLDER`  
  Name or path of the folder where resized images will be saved.
- `WIDTH`  
  Target image width in pixels (positive integer).
- `HEIGHT`  
  Target image height in pixels (positive integer).

**Notes:**
- Both `--width` and `--height` options are **mandatory** in resize mode.
- Only image files located directly inside the input folder are processed.

---

### 4.5.2 Convert Images to Grayscale

Converts all images in the specified input directory to grayscale.

**Command Template:**
- python -m img_batch.main -i INPUT_FOLDER -o OUTPUT_FOLDER -m gray

**Command Example:**
- python -m img_batch.main -i examples/input -o examples/result_gray -m gray

**Explanation:**
- Converts each image in `INPUT_FOLDER` from color to grayscale.
- Saves the processed images into `OUTPUT_FOLDER`.

**Configurable Parameters:**
- `INPUT_FOLDER`  
  Path to the folder containing images to be processed.
- `OUTPUT_FOLDER`  
  Name or path of the folder where grayscale images will be saved.

**Notes:**
- No additional parameters are required.
- Original file names are preserved after conversion.

---

### 4.5.3 Apply Blur Effect

Applies a Gaussian blur effect to all images in the specified input directory.

**Command Template:**
- python -m img_batch.main -i INPUT_FOLDER -o OUTPUT_FOLDER -m blur --ksize KSIZE

**Command Example:**
- python -m img_batch.main -i examples/input -o examples/result_blur -m blur --ksize 15

**Explanation:**
- Applies a Gaussian blur filter to each image in `INPUT_FOLDER`.
- The strength of the blur depends on the kernel size.
- Output images are saved into `OUTPUT_FOLDER`.

**Configurable Parameters:**
- `INPUT_FOLDER`  
  Path to the folder containing images to be processed.
- `OUTPUT_FOLDER`  
  Name or path of the folder where blurred images will be saved.
- `KSIZE`  
  Kernel size for the Gaussian blur filter.  
  Must be a positive odd integer (e.g., 3, 5, 7, 15).

**Notes:**
- Larger `KSIZE` values result in stronger blur effects.

---

### 4.5.4 Summary of Modes and Configurable Parameters

| Mode   | Configurable Parameters                    | Description |
|--------|--------------------------------------------|-------------|
| resize | INPUT_FOLDER, OUTPUT_FOLDER, WIDTH, HEIGHT | Resize images |
| gray   | INPUT_FOLDER, OUTPUT_FOLDER                | Convert images to grayscale |
| blur   | INPUT_FOLDER, OUTPUT_FOLDER, KSIZE         | Apply Gaussian blur effect |


---

### 4.6 Important Notes

- Images must be placed in the user-specified input directory before execution.
- The output folder name determines where processed images are saved.
- Different output folder names allow results from different modes to be stored separately.

---

## 5. Error Handling
- If the input folder does not exist, the program prints an error message and exits
- If required options are missing, execution stops with an error
- If no valid image files are found, the program exits without processing
- Output folders are created automatically if they do not exist

---

## 6. Notes
- Only image files located directly inside the input folder are processed
- Subdirectories are not scanned recursively
- Designed for educational and open-source project purposes

---
## 7. References

This project uses **OpenCV** for image loading and image processing operations such as resizing, grayscale conversion, and blurring.

- OpenCV Official Website: https://opencv.org/

OpenCV is an open-source computer vision and image processing library widely used in both academic research and industry applications.

