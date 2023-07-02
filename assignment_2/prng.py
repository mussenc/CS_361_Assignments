from time import sleep
from random import randint
import os

while True:
        sleep_sec = 1
        sleep(sleep_sec)
        print(f'prng is running')
        with open('prng-service.txt', 'r', encoding="utf-8") as f:
                read_data = f.read()

        if read_data == "run":
                with open('prng-service.txt', 'w', encoding="utf-8") as f:
                        num_files = len(os.listdir("./cs361"))
                        random_file_num = randint(1, num_files)
                        print(f'Putting random number into prng-service.txt')
                        f.write(str(random_file_num))