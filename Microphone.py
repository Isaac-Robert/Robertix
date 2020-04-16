import androidhelper
import time

droid = androidhelper.Android()
name = str(input("📁File name: "))
Tm = int(input("⏲️Recording Time(s): "))

droid.recorderStartMicrophone("/storage/emulated/0/"+name+".mp3")
print("Recording Start...")
time.sleep(Tm)

droid.recorderStop()
print(" RECORDING STOPPED⏹️")
droid.makeToast("File location: /storage/emulated/0/"+name+".mp3")
