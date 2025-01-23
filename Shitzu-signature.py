import time

def draw_shitzu_dev_text_with_numbers():
    shitzu_dev_text = [
        "  1111111    11    11  1111111   1111111  1111111  11    11  ",
        "  111        11    11    11        11         111  11    11  ",
        "  1111111    11111111    11        11       111    11    11   ",
        "       111   11    11    11        11    111       11    11    ",
        "  1111111    11    11  1111111     11    1111111   11111111   ",
    ]
    
    purple = "\033[35m"
    reset = "\033[0m"
    
    print("\033c", end="")  
    
   
    for line in shitzu_dev_text:
        for char in line:
            print(purple + char + reset, end='', flush=True) 
            time.sleep(0.005)  
        print()  
        time.sleep(0.005)  


draw_shitzu_dev_text_with_numbers()
