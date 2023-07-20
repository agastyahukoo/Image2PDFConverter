import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tkinter as tk
from tkinter import filedialog

def image_to_pdf(input_path, output_path):
    img = Image.open(input_path)
    width, height = img.size
    pdf_path = os.path.splitext(output_path)[0] + ".pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.drawImage(input_path, 50, 50, width=width, height=height)
    c.save()
    print("Conversion successful. PDF saved at:", pdf_path)

def choose_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg")])
    if file_path:
        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if output_path:
            image_to_pdf(file_path, output_path)

def main():
    root = tk.Tk()
    root.title("Image to PDF Converter")

    label = tk.Label(root, text="Select an image to convert to PDF")
    label.pack(pady=10)

    select_button = tk.Button(root, text="Select Image", command=choose_image)
    select_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
