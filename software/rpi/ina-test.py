#!/usr/bin/env python3
from ina219 import INA219
from ina219 import DeviceRangeError

SHUNT_OHMS = 1000
MAX_EXPECTED_AMPS = 0.001


def read():
    ina = INA219(SHUNT_OHMS, address=0x41)
    ina.configure(voltage_range=ina.RANGE_16V,
              gain=ina.GAIN_AUTO,
              bus_adc=ina.ADC_128SAMP,
              shunt_adc=ina.ADC_128SAMP)

    print("Supply Voltage: %.9f V" % ina.supply_voltage())
    print("Bus Voltage: %.9f V" % ina.voltage())
    try:
        print("Bus Current: %.3f uA" % (ina.current()*1000))
        print("Power: %.6f mW" % ina.power())
        print("Shunt voltage: %.6f mV" % ina.shunt_voltage())
    except DeviceRangeError as e:
        # Current out of device range with specified shunt resistor
        print(e)


if __name__ == "__main__":
    read()