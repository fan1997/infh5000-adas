import cv2
import imutils
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
# for saving video 
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
writer = cv2.VideoWriter("ped_out.mp4", fourcc=fourcc, fps=5, frameSize=(450, 253), isColor=True)
cap = cv2.VideoCapture('ped.mp4')
   
while True:
    success, frame_ped = cap.read()
    if success == False:
        break
    print(frame_ped.shape)
    frame_ped = imutils.resize(frame_ped, width=min(450, frame_ped.shape[1]))
    print(frame_ped.shape)
    (regions, _) = hog.detectMultiScale(frame_ped,
                                            winStride=(4, 4),
                                            padding=(4, 4),
                                            scale=1.05)
    if len(regions) != 0:
        print("Pedestrain alarm!")
    for (x, y, w, h) in regions:
        cv2.rectangle(frame_ped, (x, y),
                      (x + w, y + h), 
                      (0, 0, 255), 2) 
#saving video
    writer.write(frame_ped)
# showing
#     cv2.imshow("frame_ped", frame_ped)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break  
cap.release()
cv2.destroyAllWindows()
writer.release()