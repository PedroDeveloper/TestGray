import  cv2 as cv
import os

readPath = "C:\\Users\\Pedro\Desktop\\testes\\2021-02-27-CAR-20210304T130741Z-001\\fotos2"

files = os.listdir(readPath)

for file in files:
        imgPath = readPath + "\\" + file
        img = cv.imread(imgPath)
        gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        cv.imwrite("C:\\Users\\Pedro\Desktop\\testes\\2021-02-27-CAR-20210304T130741Z-001\\fotos2\\"+file,gray)
        cv.waitKey(0)