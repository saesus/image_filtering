from filtering import *
from copy import deepcopy


def main():
    img_name = "rgb.png"
    initialImage = cv2.imread(img_name)
    blurredImage = filter(deepcopy(initialImage), 'redgreen')
    cv2.imwrite("blurred_" + img_name, blurredImage)


if __name__ == '__main__':
    main()
