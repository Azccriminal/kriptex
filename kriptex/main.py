# main.py
import sys
from PyQt6.QtWidgets import QApplication
from encryption import encrypt_file, decrypt_file  # Import the encryption module
from kriptex_app import Kriptex  # Make sure you import your Kriptex class correctly

def main():
    app = QApplication(sys.argv)
    window = Kriptex()  # Create your Kriptex window object
    window.show()  # Display the window
    sys.exit(app.exec())  # Run the application's event loop

if __name__ == "__main__":
    main()  # Make sure to call the main function
