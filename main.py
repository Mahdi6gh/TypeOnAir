import hand
import cv2
Detecctor=hand.HandDetector()
def do():
    cam = cv2.VideoCapture(0)

    while True:
        _, frame = cam.read()
        frame=Detecctor.detect(frame,drawing=True)
        Listofln=Detecctor.positon(frame)
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
            listofnok= Listofln[8]
            del listofnok[0]
            # print(listofnok)
            for number in numberlist:   
                x=number[1]
                y=number[2]
                y2=number[2]
                x2=number[1]
                for  i in range(1,10):
                    x+=1
                    x2-=1
                    for j in range(1,10):
                        y+=1
                        y2-=1
                        if listofnok==[x,y]or listofnok==[x2,y2]:
                            print(number[0])
                            cv2.putText(frame, str(number[0]), (200,200), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
                            break
        cv2.imshow('Webcam', frame)
        key = cv2.waitKey(1)
        if key == 27:  # Press 'ESC' to exit
            break
    cam.release()
    cv2.destroyAllWindows()
do()