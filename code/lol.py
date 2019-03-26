missing_permission_File = "dataset/missing_perm_list.txt"

missing_file =open(missing_permission_File,"a")

for i in range(100):
    missing_file.write(str(i)+"\n")
