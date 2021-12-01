from libs.driver_interface import DriverInterface
from pymeasure.instruments.signalrecovery.dsp7265 import DSP7265


class Driver(DSP7265, DriverInterface):
    METHOD = ['Voltage', 'Frequency', 'Current', 'Phase']

    def __init__(self, visa_address):
        try:
            super().__init__(visa_address)
        except AttributeError:
            pass

    def performOpen(self):
        """Perform the operation of opening the instrument connection"""
        pass

    def performClose(self):
        """Perform the close instrument connection operation"""
        self.shutdown()

    def performSetValue(self, option, value, sweepRate=0.0):
        """Perform the Set Value instrument operation"""
        if option == 'Voltage':
            self.voltage = value
            return self.performGetValue(option, 1)
        elif option == 'Frequency':
            self.frequency = value
        elif option == 'Current':
            self.mag = value
        elif option == 'Phase':
            self.x = value
        return value

    def performGetValue(self, option, magnification):
        """Perform the Get Value instrument operation"""
        if option == 'Voltage':
            value = self.voltage
        elif option == 'Frequency':
            value = self.frequency
        elif option == 'Current':
            value = self.mag
        elif option == 'Phase':
            value = self.x
        return value * magnification


if __name__ == '__main__':
    pass
