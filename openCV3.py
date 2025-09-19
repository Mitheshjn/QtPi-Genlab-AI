import requests
import cv2
import numpy as np

API_KEY = "1iZNJp1WVNwhUztfaM3s7SoFMzWinSdM22rhIcgj3Stn2qgijNkYelvg"
headers = {"Authorization": API_KEY}

# Example: search for "nature" images
url = "https://api.pexels.com/v1/search"
params = {"query": "nature", "per_page": 1}

response = requests.get(url, headers=headers, params=params)
data = response.json()
image_url = data["photos"][0]["src"]["original"]

# Download the image
img_data = requests.get(image_url).content
nparr = np.frombuffer(img_data, np.uint8)
img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

# ✅ Print only useful info
print("Image shape:", img.shape)   # (height, width, channels)

# Calculate average color (BGR → Blue, Green, Red)
avg_color = img.mean(axis=0).mean(axis=0)
b, g, r = avg_color
print(f"Average Color → R={int(r)}, G={int(g)}, B={int(b)}")

# Show with OpenCV
cv2.imshow("Pexels Image", img)
cv2.waitKey(0)        # Wait until you press any key
cv2.destroyAllWindows()
