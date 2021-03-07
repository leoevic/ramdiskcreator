# ramdiskcreator
![alt text](docs/ram-pngrepo-com.png?raw=true)
 A simple RAM disk creator for Ubuntu-based Linux distributions. It's an easy setup wizard, which is Python-based and it's very simple.

 ## Installation
 The installation process is very easy. You just need to download the file and save it. You open a terminal and navigate to the location of the script.
 Then you need to enter "python3 main.py" and the installation wizard starts.

 First, you need to type in the size of the RAMDISK in MB. Warning: Don't use more than the half of your total RAM, or else the system could be unstable.
 Then you need to enter the name of the RAMDISK.

 After the setup process, the RAMDISK will be generated in the folder /mnt/[NAME]. The RAMDISK will be formatted with the tmpfs filesystem. Warning: Data in the RAMDISK will be lost if you restart or shutdown your computer.
