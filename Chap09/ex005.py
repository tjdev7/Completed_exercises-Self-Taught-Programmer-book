#reading files 2

my_list = list()


with open("st.txt", "r") as f:
	my_list.append(f.read())


print(my_list)