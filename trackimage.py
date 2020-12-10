# trackimage.py
# author: naserjawas
# date: 8 December 2020


import cv2 as cv
import glob

if __name__ == "__main__":
    imagedir = "./CamSeq01/"
    filenames = sorted(glob.glob(imagedir + "*.png"))
    images = [cv.imread(filename) for filename in filenames]

    print("Select the tracker:")
    print("1. KCF")
    print("2. MIL")
    print("3. TLD")
    print("4. CSRT")
    print("5. MOSSE")
    print("6. GOTURN")
    print("7. Boosting")
    print("8. Median Flow")
    chooser = int(input("Select: "))

    if chooser == 1:
        tracker = cv.TrackerKCF_create()
    elif chooser == 2:
        tracker = cv.TrackerMIL_create()
    elif chooser == 2:
        tracker = cv.TrackerTLD_create()
    elif chooser == 2:
        tracker = cv.TrackerCSRT_create()
    elif chooser == 2:
        tracker = cv.TrackerMOSSE_create()
    elif chooser == 2:
        tracker = cv.TrackerGOTURN_create()
    elif chooser == 2:
        tracker = cv.TrackerBoosting_create()
    else:
        tracker = cv.TrackerMedianFlow_create()

    initboundingbox = None
    success = False

    for image in images:

        imagedraw = image.copy()

        if initboundingbox is None:
            initboundingbox = cv.selectROI("image", image, showCrosshair=True, fromCenter=False)
            tracker.init(image, initboundingbox)
        else:
            (success, box) = tracker.update(image)
            if success:
                (x, y, w, h) = [int(v) for v in box]
                cv.rectangle(imagedraw, (x, y), (x+w, y+h), (0, 255, 0), 2)



        cv.imshow("image", imagedraw)
        k = cv.waitKey(0) & 0xFF
        if k == ord('q'):
            cv.destroyAllWindows()
            break
