from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from PIL import Image
from time import sleep
import sys

# Key vars for encryption and file saving
key = b'770A8A65DA156D24EE2A093277530142'
print("Input is an image, of the filetype BMP.")
while True:
    filename = input("Enter the filepath and name of the file to be encrypted: ")
    if filename.lower().endswith(".bmp") != True:
        print("Wrong filetype, try again")
        continue
    break

IV = get_random_bytes(16)
output_files = [filename[:-4]+"_ECB.jpg", filename[:-4]+"_CBC.jpg", filename[:-4]+"_CFB.jpg"]
# Image load and prelim processing
try:
    im = Image.open(filename)
    im_bytes = bytes(im.tobytes())
    imageSize = im.size

    # ECB
    cipher = AES.new(key, AES.MODE_ECB) # Create cipher object using key and mode
    output = cipher.encrypt(pad(im_bytes,128)) # Encrypt image, padding to ensure it fits in block
    im_out = Image.frombytes("RGB",imageSize,output) # Create an image from the encrypted bytes
    im_out.save(output_files[0]) # Save image to actual directory

    # CBC
    cipher = AES.new(key, AES.MODE_CBC, IV) # Create cipher with key and mode, and with additional IV
    output = cipher.encrypt(pad(im_bytes,128))
    im_out = Image.frombytes("RGB",imageSize,output)
    im_out.save(output_files[1])

    # CFB
    cipher = AES.new(key, AES.MODE_CFB, IV) # Create cipher with key and mode, and with additional IV
    output = cipher.encrypt(pad(im_bytes,128))
    im_out = Image.frombytes("RGB",imageSize,output)
    im_out.save(output_files[2])
except Exception as e:
    print("There was an error with the input, program is closing.")
    sleep(2)
    sys.exit()

print("Your image has been encrypted using ECB, CBC, and CFB. You can find them with the same name and the encryption type added.")