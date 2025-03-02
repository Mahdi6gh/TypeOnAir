import hand
import cv2
import numpy as np
Detecctor=hand.HandDetector()
def do():
    cam = cv2.VideoCapture(0)

    while True:
        _, frame = cam.read()
        frame=Detecctor.detect(frame,drawing=True)
        Listofln=Detecctor.positon(frame)
        # same in every code
        font = cv2.FONT_HERSHEY_SIMPLEX 
        x=50
        y=50
        numberlist=[]

        for i in range(1, 10):

            if i== 4 or i== 7 or i== 10:
                x=50
                y+=100
            numberlist.append([i,x,y])
            cv2.putText(frame, str(i), (x, y), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
            x+= 100
        if len(Listofln) > 0:
            global listofnokk
            listofnokk= Listofln[8][1:]
            
            # print(listofnok)
            for number in numberlist:   
                num , x ,y =number
                distance=np.linalg.norm(np.array(listofnokk)-np.array([x,y]))
                if distance< 30 :
                    print(number[0]) 
                    listnum=[]
                    listnum.append(str(number[0]))
                    cv2.putText(frame, str(number[0]), (300,300), font, 1, (20, 5, 255), 2, cv2.LINE_AA)
        cv2.imshow('Webcam', frame)
        key = cv2.waitKey(1)
        if key == 27:  # Press 'ESC' to exit
            break
    cam.release()
    cv2.destroyAllWindows()
do()