#
#
#		Advanced wordlist maker
#
# this is the advanced password generator that can generate passwords in order like
# if you know the format of someones password you can easily generate your own worlist
#
#  give how many sub-parts you want in a password then create a list for each difrent sub-part
#  example_ if someone has password in format-> this+ is+ @ +password
# it has four parts and you can create a list for each part as
# list 1 -> that, this, password, name etc.
# list 2 -> is, am, are, them etc.
# list 3 -> @, #, $, %
# list 4 -> key, password, answer etc.
#   this file will create a list of all possible combinations and then form a worldlist.
#
# program crated by -> lakshay tyagi
# get in touch -> lakshay_tyagi111 (instagram)
#
#
no_of_chars = input('how many diffrent units do you want?   :  ')
no_of_chars = int(no_of_chars)

i = 0

def create_dict(i):
	words = input('enter keywords separated by space for '+ 'list number '+ str(int(i+1))+' : ')
	listing = words.split(' ')
	return listing
all_lists = []

while i !=  no_of_chars:
	listn = create_dict(i)
	print(listn)
	all_lists.append(listn)
	i +=1
	
print('here are all the lists \n' , '    ~~~     ', all_lists, '     ~~~     ')

password_container_0 = []
password_container_1 = []
for i in range (no_of_chars):
	list1 = all_lists[i]
	if i == 0:
		password_container_0 = password_container_0+ list1
	else:
		for m in range (len(password_container_0)):
			l=0
			while l <len(list1):
				password_container_1.append(password_container_0[m] + list1[l])
				l+=1

print(password_container_1, '\n')

