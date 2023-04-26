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
#program crated by -> lakshay tyagi
# get in touch -> lakshay_tyagi111 (instagram)
#
#
import datetime
no_of_chars = input('how many diffrent units do you want?   :  ')
no_of_chars = int(no_of_chars)

i = 0


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))



def create_dict(i):

	words = input('enter keywords separated by space for '+ 'list number '+ str(int(i+1))+' : ')
	listing = words.split(' ')

	return listing
	
all_lists = []

while i !=  no_of_chars:
	listn = create_dict(i)
	
	prLightPurple(listn)
	
	all_lists.append(listn)
	
	i +=1
print('\n')
prCyan('here are all the lists')
prCyan(all_lists)
print('\n')
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

# print(password_container_1)
filename = 'wordlist'+ '_' + str(datetime.datetime.now().day) + '_' + str(datetime.datetime.now().hour)+ '_' + str(datetime.datetime.now().minute) +'.txt'
file1 = open(filename, 'a')

password_container_2 = '\n'.join(password_container_1)

file1.writelines(password_container_2)

file1.close()

print('A total of ', len(password_container_1), 'passwords created\n \n')
prYellow('passwords written successfully in')
prYellow(filename)
