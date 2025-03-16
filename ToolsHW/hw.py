import webbrowser, sys, os  

X1 = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

def input_math():
    while True:
        user_input = input("1 times 1 = ? ")
        if int(user_input) == 1: 
            open_video()
            break
        elif user_input == "exit":
            sys.exit()
        else:
            print("Wrong! Try again.")

def open_video():
    webbrowser.open(X1)
    os.system("echo 'Rickroll incoming...'")

input_math()


# sqp_a32abe59cdcb2c788ff7fce030cb0f0f67b68dc3