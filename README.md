QR Code Generator

A simple Python project to generate QR codes from user input and display them.

Installation
Follow these steps to set up the project:

Activate the virtual environment (if not already activated):
source venv_for_qrcode/bin/activate  # Mac/Linux
venv_for_qrcode\Scripts\activate  # Windows

Install dependencies inside the virtual environment:
pip install "qrcode[pil]" matplotlib

How to Use

Open a terminal inside the project folder.

Run the Python script:
python qr_generator.py

Enter the text or URL to generate the QR code.

The QR code will be displayed in a window and saved as qr_code.png.

Technologies Used

Python

qrcode Library

matplotlib for displaying the QR code

Example QR Code


FAQs

Why isn’t my QR code displaying?

Ensure matplotlib is installed correctly:
pip install matplotlib

On Mac, you may need:
python -m pip install "matplotlib"

How do I deactivate the virtual environment?
Run:
deactivate

License
This project is open-source. Feel free to modify and improve it.

