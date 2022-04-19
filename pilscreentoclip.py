

import win32clipboard as clip
import win32con
from io import BytesIO
from PIL import ImageGrab

image = ImageGrab.grab()

output = BytesIO()
image.convert('RGB').save(output, 'BMP')
data = output.getvalue()[14:]
output.close()
clip.OpenClipboard()
clip.EmptyClipboard()
clip.SetClipboardData(win32con.CF_DIB, data)
clip.CloseClipboard()