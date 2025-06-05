import cv2 
import matplotlib.pyplot as plt
image=cv2.imread("squidward.png")
cropped=image[100:200, 50:100]
image_rgb=cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("cropped rgb image")
plt.show()

print(image.shape)
