import time
import Adafruit_ADS1x15

class Distance:
    def __init__(self, address=0x48, gain=1, busnum=1):
        self.address = address
        self.gain = gain
        self.busnum = busnum
        self.adc = Adafruit_ADS1x15.ADS1115(address, busnum=busnum)
    
    def read_voltage(self, channel):
        # Read ADC value from the specified channel (0-3)
        adc_value = self.adc.read_adc(channel, gain=self.gain)
        # Convert the ADC value to voltage
        voltage = adc_value * (4.096 / 32767.0)
        return voltage

# if __name__ == "__main__":
#     # Create an instance of ADS1115Reader
#     ads_reader = Distance()
    
#     while True:
#         # Read voltage from channel 0
#         voltage = ads_reader.read_voltage(0)
#         print(f"Voltage: {voltage:.4f} V")
#         time.sleep(1)
