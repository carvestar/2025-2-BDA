import platform
from matplotlib import rc
import matplotlib.pyplot as plt


# 현재 파이썬이 실행되는 플랫폼 확인
def is_windows_platform():
    return platform.system() == 'Windows'
def is_mac_platform():
    return platform.system() == 'Darwin'
def is_linux_platform():
    return platform.system() == 'Linux'

# 폰트 함수
def get_font_name():
    if is_mac_platform():
        return 'AppleGothic'
    elif is_linux_platform():
        return 'LinuxFont?'
    else:
        return 'Malgun Gothic'

# 한글 폰트 깨짐 처리
def init_matplotlib():
    rc('font', family = get_font_name())
    plt.rcParams['axes.unicode_minus'] = False