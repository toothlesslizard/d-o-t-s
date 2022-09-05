import netmiko
import serial

params = {
    'device_type': "cisco_ios_serial",
    'fast_cli': False,
    'serial_settings': {'port': "/dev/ttyUSB0",
                        'baudrate': 9600,
                        'bytesize': serial.EIGHTBITS,
                        'parity': serial.PARITY_NONE,
                        'stopbits': serial.STOPBITS_ONE}
    # 'session_log': "log.txt",
}

conn = netmiko.ConnectHandler(**params)

conn.enable()
conn.send_config_set([
    'hostname csw10',
    'ip default-gateway 192.168.1.1',
    'ip domain-name X.Y.Z',
    'ip name-server 192.168.1.1'
])

conn.disconnect()
