from time import sleep

while True:
        sleep_sec = 1
        sleep(sleep_sec)
        print(f'imgsrv is running')
        
        with open('image-service.txt', 'r', encoding="utf-8") as f:
                read_data = f.read()

        if read_data.isdigit():
                with open('image-service.txt', 'w', encoding="utf-8") as f:
                        print(f'Putting random image path into image-service.txt')
                        path = f'./cs361/{read_data}.jpg'
                        read_data = f.write(path)