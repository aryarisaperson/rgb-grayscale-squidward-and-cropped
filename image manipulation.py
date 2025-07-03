import cv2
import matplotlib.pyplot as plt


image=cv2.imread("squidward.png")
print("I'm going to show you my image altering skills! I'll first show you an image of squidward!")
type=input("But, do you want me to show the image colored or grayscale?")
if type== "colored":
    image_rgb=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.title("RGB mimage")
    plt.show()
elif type=="grayscale":
    image_gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    plt.imshow(image_gray)
    plt.title("Grayscale mimage")
    plt.show()

else:
    print("Sorry, didn't catch that!")

print("Next, i'm going to show you. a cropped image, only focusing on squidward's nose!")
cropped=image[100:200, 50:100]
image_rgb=cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("cropped rgb image")
plt.show()
print(image.shape)
print("Now, I'm going to show you a rotated image of squidward!")


(h, w) = image.shape[:2]
center = (w // 2, h // 2)
rotate_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_image = cv2.warpAffine(image, rotate_matrix, (w, h))
plt.imshow(rotated_image)
plt.title("rotated image")
plt.axis("off")
plt.show()
print(image.shape)

print("Now, with a brightened image of squidward!")
bright=cv2.np.ones(50)

brightened=image(cv2.add(bright))

