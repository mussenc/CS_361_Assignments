from time import sleep
from PIL import Image

sleep_sec = 5

while True:
        input_value = input('Make a selection\n  1) Generate new image\n  2) Exit\n')
        if input_value == "1":
            print("Generating new image")
            with open('prng-service.txt', 'w', encoding="utf-8") as f:
                f.write("run")
                

            print("Choosing a random image...")
            sleep(sleep_sec)
                
            with open('prng-service.txt', 'r', encoding="utf-8") as f:
                read_data = f.read()
                print(f'random image #{read_data} was chosen')

            if read_data.isdigit():
                with open('image-service.txt', 'w', encoding="utf-8") as f:
                    f.write(read_data)
                    print("Finding Image location")
                sleep(sleep_sec)
                with open('image-service.txt', 'r', encoding="utf-8") as f:
                    read_data = f.read()
                    print(f'This image is located at {read_data}')
                    image = Image.open(read_data)
                    image.show()
        elif input_value == "2":
            break    
        else:
            print("Unknown Option")