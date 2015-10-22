import wmi, serial, time

if __name__ == "__main__":
    ser = serial.Serial("COM5")
    currentVal = 40
    c = wmi.WMI(namespace='wmi')

    methods = c.WmiMonitorBrightnessMethods()[0]
    while True:
        val = ser.readline().strip()

        should_continue = True

        if val == currentVal:
            should_continue = False

        if int(currentVal)-1 > val:
            should_continue = False

        if should_continue == True:
            currentVal = val
            methods.WmiSetBrightness(currentVal, 0)
