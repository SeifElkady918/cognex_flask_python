import telnetlib # type: ignore
from ftplib import FTP
import time
import os

CAMERA_IP = "192.168.100.47"
USERNAME = 'admin'

def capture_image_via_telnet(filename):
    try:
        # Ensure filename has .bmp extension
        if not filename.lower().endswith(".bmp"):
            filename += ".bmp"

        # Connect to the Cognex camera using Telnet
        tn = telnetlib.Telnet(CAMERA_IP, timeout=5)

        telnet_user = USERNAME+'\r\n'
        tn.write(telnet_user.encode('ascii')) #the user name is admin
        tn.write("\r\n".encode('ascii')) #there is no password - just return - now logged in
        print('Telnet Logged in')

        # Send the command to capture an image
        tn.write(b"SE8\r\n")  # Example command to trigger image capture
        time.sleep(2)  # Wait for the image to be saved on the camera

        # Close the Telnet session
        tn.write(b"exit\n")
        #tn.close()

        ftp = FTP(CAMERA_IP)
        ftp.login(USERNAME) 
        print('FTP logged in')

        lf = open(filename, "wb")
        ftp.retrbinary("RETR " + filename, lf.write)
        lf.close()

        return ""

    except Exception as e:
        return f"Error: {str(e)}"
    

def capture_image_via_telnet_dummy(filename):
    """Simulates capturing an image (dummy version)."""
    print("Function called")
    return ""

