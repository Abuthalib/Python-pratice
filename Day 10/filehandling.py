# eg:1  writing data into text file

file=open(r"C:\Users\ABUTHALIB\Desktop\Python_tutorials\myfile.txt",'w')
file.write("This is my first statement\n")
file.write("This is my second statement\n")
file.write("This is my third statement\n")
file.write("This is my fourth statement\n")
file.close()
print("completed!!")

# eg:2  reading data from text file
file = open(r"C:\Users\ABUTHALIB\Desktop\Python_tutorials\myfile.txt", 'r')
print(file.read())
print(file.readline())
file.close()

# eg:3 append the data to file
file=open(r"C:\Users\ABUTHALIB\Desktop\Python_tutorials\myfile.txt",'a')
file.write("This is my fifth line\n")
file.write("this is my sixt line using append\n")
file.close()
print("completed!!!")