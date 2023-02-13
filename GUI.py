###Berechnung
import glob
import cv2 as cv
import ka
import imutils
import numpy as np
import pandas as pd


###GUI
import tkinter as tk
import customtkinter as ct
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import pygame

# global coordinates DRAW FUNCTION
x = 0
temp_x = 0
first_x = 0

y = 0
temp_y = 0
first_y = 0

values_x = []
values_y = []

selected_path = []

images = []

height = []

class MyGUI:

    def __init__(self):
        ct.set_appearance_mode("dark")
        ct.set_default_color_theme("green")
        self.window = ct.CTk()
        self.window.geometry ("600x500")
        self.window.title("Flächenberechnungs-App")

        # self.label = ct.CTkLabel(self.window, text="1. Load Files to process \n 2. Select Path to store processed images \n 3. Stitch loaded Files \n 4. Select area for calculation",font=('Berlin Sans FB Demi', 18))
        # self.label.pack(pady=100)

        self.button_openFile = ct.CTkButton(self.window, text="1. open File", font=('Berlin Sans FB Demi', 18), command = self.openFile)
        self.button_openFile.place(x= 50, y= 50)

        self.button_selectPath = ct.CTkButton(self.window, text="2. select Path", font=('Berlin Sans FB Demi', 18),command=self.selectPath)
        self.button_selectPath.place(x= 50, y= 100)

        self.button_stitch = ct.CTkButton(self.window, text="3. stitch File", font=('Berlin Sans FB Demi', 18), command=self.stitchFile)
        self.button_stitch.place(x= 50, y= 150)

        self.button_draw = ct.CTkButton(self.window, text="4. Select Area", font=('Berlin Sans FB Demi', 18), command=self.draw)
        self.button_draw.place(x= 50, y= 200)

        self.label = ct.CTkLabel(self.window, text="5. Enter height Images were taken from:",font=('Berlin Sans FB Demi', 16))
        self.label.place(x= 250, y= 60)

        self.textbox = ct.CTkTextbox(self.window, height=2, text_color="black", fg_color="lightblue", font=('Arial', 14))
        self.textbox.place(x= 250, y= 100)

        self.check_state = tk.IntVar()

        self.check = ct.CTkCheckBox(self.window, text="Confirm input",font=('Berlin Sans FB Demi', 12), command=self.height)
        self.check.place(x= 250, y= 140)

        self.button_calc = ct.CTkButton(self.window, text="6. Calculate Area", font=('Berlin Sans FB Demi', 18), command=self.calc)
        self.button_calc.place(x= 250, y= 200)

        self.label = ct.CTkLabel(self.window, text="Always wait for a messagebox before going on with the process!",font=('Berlin Sans FB Demi', 16))
        self.label.place(x=50, y=400)

        ##M-Buttons

        self.music = ct.CTkButton(self.window, text="Play Song", text_color="lightblue", command=self.play_music)
        self.music.place(x= 50, y= 300)

        self.stop_music = ct.CTkButton(self.window, text_color="lightblue", text="stop music", command=self.stop)
        self.stop_music.place(x= 250, y= 300)

        self.window.mainloop()

        ###ALBERNER STUFF###

    pygame.mixer.init()
    def play_music(self):
        pygame.mixer.music.load("E:\musik.mp3")
        pygame.mixer.music.play(loops=0)
    def stop(self):
        pygame.mixer.music.stop()


        ###Actually s Programm###

        #Functionname indicates part of process

    def openFile(self):
        filepath = filedialog.askdirectory()
        path = glob.glob(filepath + '/*.jpg')

        for image in path:
            img = cv.imread(image)
            images.append(img)
            re = ka.resize_img(img, scale=0.3)
            # cv.imshow('Image', re)
            k = cv.waitKey(0) & 0xff
            if k == 27:
                cv.destroyAllWindows()

        messagebox.showinfo(message= (len(images), "Images loaded"))

    def selectPath(self):
        s_path = filedialog.askdirectory()
        selected_path.append(s_path)
        # print(selected_path)
        messagebox.showinfo(message="path selected")

    def stitchFile(self):

        imageStitcher = cv.Stitcher_create()

        error, stitched_img = imageStitcher.stitch(images)

        if not error:
            re_stitch = ka.resize_img(stitched_img, scale=0.1)
            # cv.imwrite("stitchedOutput2!.png", stitched_img)
            cv.imshow("Stitched Image 2", re_stitch)
            # cv.imwrite(filedialog.askdirectory() + "/stitched Image.png", stitched_img)
            k = cv.waitKey(0) & 0xff
            if k == 27:
                cv.destroyAllWindows()

            stitched_img = cv.copyMakeBorder(stitched_img, 10, 10, 10, 10, cv.BORDER_CONSTANT, (0, 0, 0))

            gray = cv.cvtColor(stitched_img, cv.COLOR_BGR2GRAY)
            thresh_img = cv.threshold(gray, 0, 255, cv.THRESH_BINARY)[1]

            thresh_img_re = ka.resize_img(thresh_img, scale=0.1)

            cv.imshow("Threshold Image", thresh_img_re)
            k = cv.waitKey(0) & 0xff  # press ESC to exit
            if k == 27:
                cv.destroyAllWindows()

            contours = cv.findContours(thresh_img.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

            contours = imutils.grab_contours(contours)
            areaOI = max(contours, key=cv.contourArea)

            mask = np.zeros(thresh_img.shape, dtype="uint8")
            x, y, w, h = cv.boundingRect(areaOI)
            cv.rectangle(mask, (x, y), (x + w, y + h), 255, -1)

            minRectangle = mask.copy()
            sub = mask.copy()

            while cv.countNonZero(sub) > 0:
                minRectangle = cv.erode(minRectangle, None)
                sub = cv.subtract(minRectangle, thresh_img)

            contours = cv.findContours(minRectangle.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

            contours = imutils.grab_contours(contours)
            areaOI = max(contours, key=cv.contourArea)

            minRectangle_re = ka.resize_img(minRectangle)
            # cv.imshow("minRectangle Image", minRectangle_re)
            k = cv.waitKey(0) & 0xff  # press ESC to exit
            if k == 27:
                cv.destroyAllWindows()

            x, y, w, h = cv.boundingRect(areaOI)

            stitched_img = stitched_img[y:y + h, x:x + w]

            stitched_img_re = ka.resize_img(stitched_img, scale=0.1)

            cv.imwrite(selected_path[0] + "/stitched Image.png", stitched_img)
            cv.imshow("Stitched Image Processed", stitched_img_re)
            k = cv.waitKey(0) & 0xff  # press ESC to exit
            if k == 27:
                cv.destroyAllWindows()

            messagebox.showinfo(message="Stitching abgeschlossen")

        else:
            messagebox.showinfo(message="Bilder konnten nicht gestitcht werden!\nWahrscheinlich konnten nicht genügend Keypoints gefunden werden!")

    def draw(self):
        bild = cv.imread(selected_path[0] + "/stitched Image.png")
        bild_re = ka.resize_img(bild, scale=0.2)

        def draw(event, current_x, current_y, flags, params):
            global temp_x, temp_y, x, y, first_y, first_x

            if event == cv.EVENT_LBUTTONDOWN:
                if x == 0 and y == 0:
                    x = current_x
                    y = current_y
                    values_x.append(x)
                    values_y.append(y)
                    first_x = x
                    first_y = y

                elif x != 0 and y != 0:
                    temp_x = x
                    temp_y = y
                    x = current_x
                    y = current_y
                    values_x.append(x)
                    values_y.append(y)

        cv.imshow('Draw', bild_re)

        def nothing(x):
            pass

        cv.namedWindow('trackbar')

        cv.createTrackbar('thickness', 'trackbar', 1, 20, nothing)

        cv.setMouseCallback('Draw', draw)

        while True:
            cv.imshow('Draw', bild_re)

            if x != first_x and y != first_y:
                n = cv.getTrackbarPos('thickness', 'trackbar')
                cv.line(bild_re, (temp_x, temp_y), (x, y), (255, 255, 255), thickness=n)

            if cv.waitKey(1) & 0xFF == 27: break
        cv.destroyAllWindows()
        cv.imwrite(selected_path[0] + "/lines.png", bild_re)

        dataframe = pd.DataFrame(
            {
                "x_values": values_x,
                "y_values": values_y
            }
        )
        ###FILL LINES
        x_values = dataframe["x_values"].to_numpy(dtype=int)
        y_values = dataframe["y_values"].to_numpy(dtype=int)

        def get_points(x_values, y_values):
            x = np.reshape(np.array(x_values), (len(x_values), 1))
            y = np.reshape(np.array(y_values), (len(y_values), 1))
            return np.hstack([x, y])

        points = get_points(x_values, y_values)

        img_filled = cv.fillPoly(bild_re, [points], (255, 255, 255))
        cv.imshow('filled', img_filled)
        k = cv.waitKey(0) & 0xff  # press ESC to exit
        if k == 27:
            cv.destroyAllWindows()

        cv.imwrite(selected_path[0] + "/filled.png", img_filled)

        messagebox.showinfo(message="Area selected")

    def height(self):
        if self.check_state.get() == 0:
            # print(self.textbox.get('1.0', tk.END))
            height.append(self.textbox.get('1.0', tk.END))
            print(height[0])

    def calc(self):
        img = cv.imread(selected_path[0] + "/filled.png", 0)
        area_px = []

        def nothing(x):
            pass
        while (1):
            ret, thresh = cv.threshold(img, 254, 255, cv.THRESH_BINARY)
            cv.imshow("output", thresh)
            cv.imwrite('E:/Thresh.png', thresh)
            k = cv.waitKey(10) & 0xFF
            if k == 27:
                break
        print(cv.countNonZero(thresh))
        area_px.append(cv.countNonZero(thresh))
        cv.destroyAllWindows()

        img_end = cv.imread(selected_path[0] + "/lines.png")

        ##UMRECHNUNG###

        def umrechnung(h):
            return 316938 * h ** -1.854

        h= (int(height[0]))

        Pixel = umrechnung(h)

        FINAL_RECHNUNG = round(area_px[0] / Pixel, 2)
        print(FINAL_RECHNUNG)
        img_end_text = cv.putText(img_end, "A: {}cm^2".format(FINAL_RECHNUNG), (values_x[0], values_y[0]),
                                  cv.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 5)
        cv.imshow('Area', img_end_text)
        cv.imwrite('E:/Endprodukt.jpg', img_end_text)
        k = cv.waitKey(0) & 0xff
        if k == 27:
            cv.destroyAllWindows()

MyGUI()



