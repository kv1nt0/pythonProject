from time import sleep
from itertools import cycle

class Trafficlight:
    __color = ['     ', [5, 3, 5], ["\033[41m", "\033[43m", "\033[42m"]]

    def running(self):
        color_list = ["", ""]
        for n in cycle((0, 1, 2)):
            color_list[1] = self.__color[2][n]
            print(f"\r({color_list[int(n == 0)]}{self.__color[0]}\033[0m)"
                  f"({color_list[int(n == 1)]}{self.__color[0]}\033[0m)"
                  f"({color_list[int(n == 2)]}{self.__color[0]}\033[0m)", end='')
            sleep(self.__color[1][n])


traffic_light = Trafficlight()
traffic_light.running()
