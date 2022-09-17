from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20 ")
def logout():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
def shutdown():
    os.system("shutdown /s /t 1 ")
sutdown_app=Tk()
sutdown_app.title("Shutdown App")
sutdown_app.geometry("500x500")
sutdown_app.config(bg="#345156")
restart_button=Button(sutdown_app,text="Restart",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="hand2",command=restart)
restart_button.place(x=150,y=80,height=40,width=200)
restart_button_Time=Button(sutdown_app,text="Restart Time",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="hand2",command=restart_time)
restart_button_Time.place(x=150,y=180,height=40,width=200)
Log_out_button=Button(sutdown_app,text="Log-out",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="hand2",command=logout)
Log_out_button.place(x=150,y=280,height=40,width=200)
Shut_Down_button=Button(sutdown_app,text="Shutdown",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="hand2",command=shutdown)
Shut_Down_button.place(x=150,y=380,height=40,width=200)
Shut_Down_button=Button(sutdown_app,text="Made By: Rabban Ali",font=("Time New Roman",8,"bold"),relief=RAISED,cursor="hand2",command=shutdown)
Shut_Down_button.place(x=380,y=473,height=30,width=125)
sutdown_app.mainloop()
