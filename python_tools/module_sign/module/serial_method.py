import serial.tools.list_ports


def get_port_list() -> list[str]:
    plist = list(serial.tools.list_ports.comports())
    ports: list[str] = [p.name for p in plist]
    return ports
