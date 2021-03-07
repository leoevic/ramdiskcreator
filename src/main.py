import os

# declare the needed information about the RAMDISK (size, name)
print("Welcome to the RAMDISK creator. Please remember to run this script with sudo.")
print("Please enter the size of the RAMDISK in MB. Attention: DO NOT USE MORE THAN 1/2 OF YOUR RAM SIZE!")

ramsize = input()

print("Please declare the name from the RAMDISK:")
diskname = input()

# create the RAMDISK
os.system("sudo mkdir /mnt/" + diskname)
os.system("sudo mount -t tmpfs -o rw,size=" + ramsize + "M tmpfs /mnt/" + diskname)

print("RAMDISK created. Press enter to exit.")
exit = input()