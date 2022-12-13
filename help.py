guidance_file = "help.txt"

# def open_help():
guidance_file = open("help.txt", "r")
print(guidance_file.readlines())
guidance_file.close()