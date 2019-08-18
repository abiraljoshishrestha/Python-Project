def read_file(a,b,c):
    file=open("Inventory.txt","w")
    file.write(str(a))
    file.write(str("\n"))
    file.write(str(b))
    file.write(str("\n"))
    file.write(str(c))
    file.write(str("\n"))
    file.close()
