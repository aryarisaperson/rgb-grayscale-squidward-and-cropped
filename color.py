import cv2 
import matplotlib.pyplot as plt

type=input("Do you want your personal squidward to be colored or grayscale?")
image=cv2.imread("squidward.png")

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
    print(":(")

