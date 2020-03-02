# A small wrapper for Andor Cameras

This is a small Python wrapper for Andor cameras and spectrometers. It tries to stick to the same function naming that Andor does. Therefore, it should be fairly trivial how to use it.
The module is object oriented and keeps some information inside the class such as gain, preampgain, gainRange etc.

## Preparation

### Install Andor driver

Install Andor MCD or Andor SOLIS from an official source (probably a DVD shipped with a camera).
In windows, it creats a folder `C:\\Program Files (x86)\\Andor SOLIS`.

You don't need Andor SDK, but need a dynamic link library `atmcd32d.dll` or `atmcd64d.dll`, shipped with AndorSOLIS.

I only tested with 32-bit software (not an OS platform).
Probably the 64-bit software may create `C:\\Program Files\\Andor SOLIS`.

If you saved AndorSOLIS to a different location, you may need to configure a configuration file.
(This feature is not yet implemented.)

### Install python environment

Depending on the software version, you may choose an appropriate platform of python.
For 32-bit software, you may need 32-bit python. 

For example, install 32-bit version of [miniconda3 from Anaconda](https://docs.conda.io/en/latest/miniconda.html).

#### Prepare some necessary libraries.

Install pillow

```bash
conda install pillow, pytest
```

# Usage
```python

from pyandor import AndorCamera

cam = AndorCamera()
cam.SetDemoReady()
cam.StartAcquisition()
data = []
cam.GetAcquiredData(data)
cam.SaveAsTxt("raw.txt")
cam.ShutDown()

```

## Test the library

You may need to test the camera by AndorSOLIS first.
If succeeded, you can test pyandor by

```bash
pytest tests/camear.py
```
If errors are found.

-------- original readme ---

This is a small Python wrapper for Andor cameras and spectrometers. It tries to stick to the same function naming that Andor does. Therefore, it should be fairly trivial how to use it.
The module is object oriented and keeps some information inside the class such as gain, preampgain, gainRange etc.

The main modules is 'andor.py'. This module has been tested both in Windows and Linux with Newton and EM ranges from Andor. There is another module which has been tested on Windows for iDus range.

Simple example:


import pyandor

cam = Andor()
cam.SetDemoReady()
cam.StartAcquisition()
data = []
cam.GetAcquiredData(data)
cam.SaveAsTxt("raw.txt")
cam.ShutDown()
