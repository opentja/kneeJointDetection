# reference https://github.com/ultralytics/yolov3

import os
import glob

txtPath = '/infodev1/phi-data/shi/kneeJointDetection/experiment202010/data/test/labels/'
imagePath = '/infodev1/phi-data/shi/kneeJointDetection/experiment202010/data/test/images/'


def deleteZero(txtList, txtPath, imagePath, tkaAP, kneeLat, doubleAP):
    tkaAPList, kneeLatList, doubleAPList = [], [], []
    for txtName in txtList:
        f = open(txtPath + txtName, 'r')
        linesList = f.readlines()
        for tmpIdx in range(len(linesList)):
            linesList[tmpIdx] = linesList[tmpIdx].strip()

        if len(linesList) == 1:
            if linesList[0].split(' ')[0] == str(1):
                tkaAPList.append(txtName)
            if linesList[0].split(' ')[0] == str(2):
                kneeLatList.append(txtName)
        if len(linesList) == 2:
            if linesList[0].split(' ')[0] == str(0) and linesList[1].split(' ')[0] == str(0):
                doubleAPList.append(txtName)
            if (linesList[0].split(' ')[0] == str(0) and linesList[1].split(' ')[0] == str(1)) or (
                    linesList[0].split(' ')[0] == str(1) and linesList[1].split(' ')[0] == str(0)):
                tkaAPList.append(txtName)
        f.close()

    for i in range(tkaAP):
        os.remove(txtPath + tkaAPList[i])
        os.remove(imagePath + tkaAPList[i].replace('.txt', '.jpg'))

    for i in range(kneeLat):
        os.remove(txtPath + kneeLatList[i])
        os.remove(imagePath + kneeLatList[i].replace('.txt', '.jpg'))
    for i in range(doubleAP):
        os.remove(txtPath + doubleAPList[i])
        os.remove(imagePath + doubleAPList[i].replace('.txt', '.jpg'))


def count(txtList, txtPath):
    tkaAP, kneeLat, ap, tkaLat = 0, 0, 0, 0
    for txtName in txtList:
        f = open(txtPath + txtName, 'r')
        linesList = f.readlines()
        for tmpIdx in range(len(linesList)):
            linesList[tmpIdx] = linesList[tmpIdx].strip()

        if len(linesList) == 1:
            if linesList[0].split(' ')[0] == str(0):
                ap += 1
            if linesList[0].split(' ')[0] == str(1):
                tkaAP += 1
            if linesList[0].split(' ')[0] == str(2):
                kneeLat += 1
            if linesList[0].split(' ')[0] == str(3):
                tkaLat += 1

        if len(linesList) == 2:
            if linesList[0].split(' ')[0] == str(0) and linesList[1].split(' ')[0] == str(0):
                ap+=2
            if linesList[0].split(' ')[0] == str(1) and linesList[1].split(' ')[0] == str(1):
                tkaAP+=2
            if (linesList[0].split(' ')[0] == str(0) and linesList[1].split(' ')[0] == str(1)) or (
                    linesList[0].split(' ')[0] == str(1) and linesList[1].split(' ')[0] == str(0)):
                tkaAP+=1
                ap+=1
    print(ap, tkaAP, kneeLat, tkaLat)



def deletetExtra(txtPath, imagePath):
    txtList = os.listdir(txtPath)
    maleTxtList = []
    femaleTxtList = []
    for txtName in txtList:
        if txtName.find('sex_F') != -1:
            femaleTxtList.append(txtName)
        if txtName.find('sex_M') != -1:
            maleTxtList.append(txtName)

    # deleteZero(maleTxtList, txtPath, imagePath,tkaAP=18, kneeLat=70, doubleAP=76)
    # deleteZero(femaleTxtList, txtPath, imagePath, tkaAP=27, kneeLat=45, doubleAP=80)

    count(os.listdir(txtPath), txtPath)

txtPath = '/infodev1/phi-data/shi/kneeJointDetection/experiment202010/data/testCopy/labels/'
imagePath = '/infodev1/phi-data/shi/kneeJointDetection/experiment202010/data/testCopy/images/'
deletetExtra(txtPath, imagePath)
