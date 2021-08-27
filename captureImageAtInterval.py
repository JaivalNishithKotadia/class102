import cv2
import dropbox
import time

import random


start_time=time.time()


def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    
        return img_name 
    print('TO CHECK') 
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_files(img_name):
    accessToken='h1yboaA7O8EAAAAAAAAAAfe4QapQPoGK9CMdlni864NNPxR985GGughwGXMoOF8b'
    file=img_name
    file_from=file
    file_to="/class102/"+(img_name)
    dbx=dropbox.Dropbox(accessToken)
    with open (file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print('Successfully Uploaded')
        
def main():
    while(True):
        if((time.time()-start_time) >= 5):
            name=take_snapshot()
            upload_files(name)

if __name__ == '__main__':
    main()