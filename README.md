# 📸 Image Extractor  

_A simple Python tool utilizing OpenCV to extract individual images from a scanned document._  

## ✨ Why I Built This  
Archiving my family photos became a tedious task—scanning each picture one by one was too time-consuming. To solve this, I built **Image Extractor**, a simple tool that automates the process by detecting and extracting individual photos from a single scanned image.  

## 🚀 Features  
✅ **Automatic Image Extraction** – Detects and crops multiple images from a single scanned image.  
✅ **Face Recognition Sorting** – Automatically moves images containing faces into a separate folder.  
✅ **Batch Processing** – Load and process multiple images at once.  
✅ **CLI-Driven** – Navigate directories, list image files, and select documents with ease.  

## 🛠️ How It Works  
1. **Prepare Your Scan**  
   - Place multiple photos on a scanner with some empty space between them.  
   - Use a white background for better contrast.  

2. **Run the Tool**  
   - Open the CLI and launch Image Extractor.  
   - Select the source directory and the image file to process.  
   - Choose whether to use face detection for sorting.  

3. **Let It Work**  
   - The tool will extract each photo and save them as separate files.  
   - Any image containing a face will be moved to a dedicated folder.  

## 📦 Installation  
Make sure you have **Python 3** installed, then install the required dependencies:  
```bash
pip install opencv-python
```  
## 🎯 Usage
Run the tool from the command line:
```bash
python main.py
```
Once project is at a completed state, I will add a release for ease of use (simply run the executable)

## 🤖 Tech Stack
- Python 🐍
- OpenCV 🖼️

## 🔥 Future Improvements
- GUI Support for a more user-friendly experience.
- More advanced face detection with AI models.

## 📜 License
This project is licensed under the MIT License.
