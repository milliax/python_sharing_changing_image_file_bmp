from os import strerror

# srcname = input("Enter the source file name: ")
srcname = "face.bmp"

try:
    src =open(srcname,'rb')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)

# dstname = input("Enter the destination file name: ")
dstname = "output.bmp"

try:
    dst = open(dstname,'wb')
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)

buffer = bytearray(65536)
total = 0

step = 0

try:
    readin = src.readinto(buffer)
    while readin > 0:
        for i in range(len(buffer)):
            if(step > 53 and step % 3 == 0):
                # print(buffer)
                buffer[i] = 255
            step = step+1
        
        written = dst.write(buffer[:readin])
        readin = src.readinto(buffer)

        total += written
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)

print(total,'byte(s) succesfully written')
src.close()
dst.close()

# if __name__ == "__main__":
#     try:
#         redin = src.readinto(buffer)