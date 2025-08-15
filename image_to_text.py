import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit, QFileDialog, QMessageBox
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt
from PIL import Image
import pytesseract
import fitz  # PyMuPDF for PDF text extraction
import qdarkstyle
from docx import Document
from pdf2image import convert_from_path  # Converts PDF pages to images (for scanned PDFs)

class ImageToTextApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MBS TechGuru - Image & PDF to Text Extractor")
        self.setGeometry(100, 100, 700, 600)
        self.setStyleSheet(qdarkstyle.load_stylesheet())  # Applying Dark Theme

        layout = QVBoxLayout()

        # Title Label
        self.title = QLabel("MBS TechGuru - Image & PDF to Text Extractor", self)
        self.title.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.title)

        # Upload Button
        self.upload_btn = QPushButton("📂 Upload Image or PDF", self)
        self.upload_btn.setFont(QFont("Arial", 12))
        self.upload_btn.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px; border-radius: 8px;")
        self.upload_btn.clicked.connect(self.upload_file)
        layout.addWidget(self.upload_btn)

        # Image Display
        self.img_label = QLabel(self)
        self.img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.img_label)

        # Extract Button
        self.extract_btn = QPushButton("📜 Extract Text", self)
        self.extract_btn.setFont(QFont("Arial", 12))
        self.extract_btn.setStyleSheet("background-color: #FF9800; color: white; padding: 10px; border-radius: 8px;")
        self.extract_btn.clicked.connect(self.extract_text)
        layout.addWidget(self.extract_btn)

        # Extracted Text Area
        self.text_area = QTextEdit(self)
        self.text_area.setFont(QFont("Arial", 10))
        layout.addWidget(self.text_area)

        # Save to Word Button
        self.save_btn = QPushButton("💾 Save as Word File (.docx)", self)
        self.save_btn.setFont(QFont("Arial", 12))
        self.save_btn.setStyleSheet("background-color: #2196F3; color: white; padding: 10px; border-radius: 8px;")
        self.save_btn.clicked.connect(self.save_to_word)
        layout.addWidget(self.save_btn)

        # Footer Label
        self.footer = QLabel("Developed by MBS TechGuru", self)
        self.footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.footer.setStyleSheet("color: #aaaaaa;")
        layout.addWidget(self.footer)

        self.setLayout(layout)

    def upload_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image or PDF", "", "Images & PDFs (*.png *.jpg *.jpeg *.pdf)")
        if file_path:
            self.file_path = file_path
            if file_path.lower().endswith(".pdf"):
                self.img_label.setText("📄 PDF Selected: " + os.path.basename(file_path))
            else:
                pixmap = QPixmap(file_path)
                self.img_label.setPixmap(pixmap.scaled(400, 300, Qt.AspectRatioMode.KeepAspectRatio))

    def extract_text(self):
        if not hasattr(self, 'file_path'):
            QMessageBox.warning(self, "Error", "Please upload an image or PDF first!")
            return

        extracted_text = ""

        if self.file_path.lower().endswith(".pdf"):
            doc = fitz.open(self.file_path)

            for page in doc:
                text = page.get_text("text")  # Try normal text extraction
                if not text.strip():
                    text = page.get_text("blocks")  # Try block-based extraction
                if not text.strip():
                    text = page.get_text("words")  # Try word-based extraction
                extracted_text += str(text) + "\n"

            # If no text found, convert PDF pages to images and extract using OCR
            if not extracted_text.strip():
                images = convert_from_path(self.file_path)
                for img in images:
                    extracted_text += pytesseract.image_to_string(img) + "\n"

        else:  # If it's an image file
            image = Image.open(self.file_path)
            extracted_text = pytesseract.image_to_string(image)

        # Check if text is extracted
        if extracted_text.strip():
            self.text_area.setText(extracted_text)  # Display the text in the GUI
        else:
            self.text_area.setText("No text found in the document.")

    def save_to_word(self):
        extracted_text = self.text_area.toPlainText().strip()
        
        if not extracted_text:
            QMessageBox.warning(self, "Error", "No text to save! Extract text first.")
            return

        file_path, _ = QFileDialog.getSaveFileName(self, "Save as Word File", "", "Word Document (*.docx)")
        
        if file_path:
            if not file_path.endswith(".docx"):  # Ensure correct file extension
                file_path += ".docx"

            doc = Document()
            doc.add_paragraph(extracted_text)  # Save extracted text
            doc.save(file_path)

            QMessageBox.information(self, "Success", f"File saved successfully at:\n{file_path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageToTextApp()
    window.show()
    sys.exit(app.exec())
