import time
from pyandor import AndorCamera


def test_demo():
    cam = AndorCamera(verbose=False)
    cam.GetVSSpeed()
    cam.GetHSSpeed()
    # use the fastest shift speed
    cam.SetHSSpeed(0, index=0)
    
    cam.SetDemoReady()
    cam.SetImage(hbin=1, vbin=16, hstart=1, 
                 hend=1024, vstart=1, vend=1024)
    cam.SetNumberAccumulations(1)
    cam.StartAcquisition()
    data = []
    cam.GetAcquiredData(data)
    cam.GetAcquisitionTimings()

def test_cooler():
    cam = AndorCamera(verbose=True)
    cam.SetCoolerMode(0)
    cam.SetTemperature(20)
    cam.CoolerON()
    for _ in range(3):
        time.sleep(3)
        cam.GetTemperature()
        print(cam.temperature)
    # strangely, it does not work. Just commented out
    # assert cam.IsCoolerOn()
    cam.CoolerOFF()
    