data =input("Enter text to write to the file: ")
with open("output.txt","wt") as file:
         data = file.write(data)
         print("Data  successfully  written to output.txt.")

append_data = input("Enter additional text to append: ")
with open("output.txt","at") as file:
    file.write("\n" + append_data)
    print("Data successfully appended.")