import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time


class App:

    def __init__(self, window, window_title, video_source=0):
        self.window=window
        self.window.title=(window_title)
        self.video_source=video_source

        self.vid= MyVideoCapture(self.video_source)
        self.canvas=tkinter.Canvas(window, width=self.vid.width, height =  self.vid.height)
        self.canvas.pack()


        btn_frame=tkinter.Frame(window, background="white")
        btn_frame.place(x=0,y=0, anchor="nw", width=self.vid.width+4)

        self.btn_back=tkinter.Button(btn_frame, text="BACK",width=20, command=self.getback, bg="white", fg="green")
        self.btn_back.pack(side="left", padx=10, pady=10)



        self.btn_logout=tkinter.Button(btn_frame, text="LOGOUT", width=10, command=self.log_out, bg="white", fg="red")
        self.btn_logout.pack(side="right", padx=10, pady=10)
         
        #record

        # self.btn_about=tkinter.Button(btn_frame, text="LOGOUT", width=10, command=self.log_out, bg="white", fg="red")
        # self.btn_about.pack(side="right", padx=10, pady=10)

        self.delay=15
        self.update()

        self.window.mainloop()
    def log_out(self):
        self.window.destroy()
        import login_screen
    def getback(self):
        self.window.destroy()
        import home_screen
        # ret, frame=self.vid.get_frame()

        # if ret:
        #   cv2.imwrite("frame-"+time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) )

    def update(self):
        ret, frame=self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0,0, image=self.photo, anchor=tkinter.NW)

            self.window.after(self.delay,self.update)

    def from_rgb(self,rgb):
        return "#%02x%02x%02x" % rgb


class  MyVideoCapture:
    """docstring for  MyVideoCapture"""
    def __init__(self, video_source=0):
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("unable open video source", video_source)

        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret,None)       
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

App(tkinter.Tk(),"tkinter ad OpenCV")

