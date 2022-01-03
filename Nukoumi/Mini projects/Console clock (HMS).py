from datetime import datetime
import time, os

while True:
    os.system("cls")
    a = datetime.now().time()
    print(a)
    time.sleep(0.25)