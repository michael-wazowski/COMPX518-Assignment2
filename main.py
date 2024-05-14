from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from PIL import Image

# Key vars for encryption and file saving
key = b'770A8A65DA156D24EE2A093277530142'
filename = "Image-Assignment2.bmp"
IV = get_random_bytes(16)
output_files = [filename[:-4]+"_ECB.jpg", filename[:-4]+"_CBC.jpg", filename[:-4]+"_CFB.jpg"]
# Image load and prelim processing
im = Image.open(filename)
im_bytes = bytes(im.tobytes())
imageSize = im.size

# ECB
cipher = AES.new(key, AES.MODE_ECB)
output = cipher.encrypt(pad(im_bytes,128))
im_out = Image.frombytes("RGB",imageSize,output)
im_out.save(output_files[0])

# CBC
cipher = AES.new(key, AES.MODE_CBC, IV)
output = cipher.encrypt(pad(im_bytes,128))
im_out = Image.frombytes("RGB",imageSize,output)
im_out.save(output_files[1])

# CFB
cipher = AES.new(key, AES.MODE_CFB, IV)
output = cipher.encrypt(pad(im_bytes,128))
im_out = Image.frombytes("RGB",imageSize,output)
im_out.save(output_files[2])