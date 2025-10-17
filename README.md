# Black & White Image Colorization Project

This script uses a pre-trained deep learning model to automatically colorize black and white images.

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

### Step 1: Download the Pre-trained Model Files

First, you need to download the three files required for the Caffe model.

1. Create a folder named `models` in the main project directory.

2. Download the following files and place them inside the `models` folder:

   * **Model Architecture:** `colorization_deploy_v2.prototxt`

     * Download from: https://github.com/richzhang/colorization/tree/caffe/colorization/models

   * **Model Weights:** `colorization_release_v2.caffemodel`

     * Download from: https://www.dropbox.com/scl/fi/d8zffur3wmd4wet58dp9x/colorization_release_v2.caffemodel?rlkey=iippu6vtsrox3pxkeohcuh4oy&dl=0

   * **Color Palette Data:** `pts_in_hull.npy`

     * Download from: https://github.com/richzhang/colorization/blob/caffe/colorization/resources/pts_in_hull.npy

### Step 2: Create and Activate the Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

1. **Create the environment** named `BnW`:

   ```bash
   python -m venv BnW
   ```

2. **Activate the environment**:

   * On **Windows** (Command Prompt or PowerShell):

     ```bash
     .\BnW\Scripts\activate
     ```

   * On **macOS and Linux**:

     ```bash
     source BnW/bin/activate
     ```

   Your terminal prompt should now show `(BnW)` at the beginning.

### Step 3: Install Required Python Packages

With the virtual environment active, install the necessary libraries using pip.

```bash
pip install numpy opencv-python
```

### Step 4: Run the Application

You are now ready to colorize an image!

1. Execute the main script from your terminal:

   ```bash
   python app.py
   ```

2. When prompted, enter the full path to the black and white image you want to colorize.

   ```
   [BOT] : Hello! Lets turn your old BnW prictures to Colorful ones!!
   [User]: Enter the path to your BnW image : "C:\path\to\your\image.jpg"
   ```

3. The script will process the image, save the output as `colorized_img.jpg` in the project directory, and ask if you want to see a preview.
