import cv2
import numpy as np

def main():
    print(cv2.__version__)
    img = np.zeros((400,600))
    
    cv2.imshow("img",img)
    cv2.waitKey()


if __name__ == "__main__":
    main()