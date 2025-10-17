import numpy as np
import cv2
from cv2 import dnn
import os

#model paths
proto_file = "models/colorization_deploy_v2.prototxt"
model_file = "models/colorization_release_v2.caffemodel"
hull_pts = "models/pts_in_hull.npy"

def bot_print(msg):
    print(f"[BOT] : {msg}")

def user_input(msg):
    return input(f"[User]: {msg}")

def main():
    bot_print("Hello! Lets turn your old BnW prictures to Colorful ones!!")
    img_path = user_input("Enter the path to your BnW image : ")
    img_path = img_path.strip().strip('"').replace("\\","/")

    if not os.path.exists(img_path):
        bot_print("Error image not found. Please check the path provided")
        return
    
    bot_print("Loading pre-trained model...")
    net = dnn.readNetFromCaffe(proto_file,model_file)
    kernal = np.load(hull_pts)

    bot_print("Reading image...")
    img = cv2.imread(img_path)
    scaled = img.astype("float32") / 255.0
    lab_img = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)

    class8 = net.getLayerId("class8_ab")
    conv8 = net.getLayerId("conv8_313_rh")
    pts = kernal.transpose().reshape(2,313,1,1)
    net.getLayer(class8).blobs = [pts.astype("float32")]
    net.getLayer(conv8).blobs = [np.full([1,313], 2.606, dtype="float32")]
    
    resized = cv2.resize(lab_img, (224,224))
    L = cv2.split(resized)[0]
    L -=50

    bot_print("Colorizing...")
    net.setInput(cv2.dnn.blobFromImage(L))
    ab_channel = net.forward()[0,:,:,:].transpose((1,2,0))
    ab_channel = cv2.resize(ab_channel, (img.shape[1], img.shape[0]))

    L = cv2.split(lab_img)[0]
    colorized = np.concatenate((L[:,:,np.newaxis], ab_channel), axis=2)
    colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
    colorized = np.clip(colorized, 0,1)
    colorized = (255 * colorized).astype("uint8")

    output_path = "colorized_img.jpg"
    cv2.imwrite(output_path, colorized)
    bot_print(f"Colorized image saved succefully at {output_path}")

    #show output
    show = user_input("Do you want to see the preview? (y/n) : ")
    if show.lower() == 'y':
        img_resized = cv2.resize(img, (400,400))
        colorized_resized = cv2.resize(colorized, (400,400))
        result = cv2.hconcat([img_resized, colorized_resized])
        cv2.imshow("BnW Image (Left) vs Colorized Image (Right)", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else: 
        bot_print("Preview Skipped...")

if __name__ == "__main__":
    main()