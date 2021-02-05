#Loops Conditions and Parsing - Bash scripting

##0. Create a SSH RSA key pair 

##1. For Holberton School loop 
Write a Bash script that displays Holberton School 10 times.

##2. While Holberton School loop
Write a Bash script that displays Holberton School 10 times.

##3. Until Holberton School loop
Write a Bash script that displays Holberton School 10 times.

##4. If 9, say Hi!
Write a Bash script that displays Holberton School 10 times, but for the 9th iteration, displays Holberton School and then Hi on a new line.

##5. 4 bad luck, 8 is your chance
Write a Bash script that loops from 1 to 10 and:

displays bad luck for the 4th loop iteration
displays good luck for the 8th loop iteration
displays Holberton School for the other iteration

##6. Superstitious numbers
Write a Bash script that displays numbers from 1 to 20 and:

displays 4 and then bad luck from China for the 4th loop iteration
displays 9 and then bad luck from Japan for the 9th loop iteration
displays 17 and then bad luck from Italy for the 17th loop iteration

##7. Clock
Write a Bash script that displays the time for 12 hours and 59 minutes:

display hours from 0 to 12
display minutes from 1 to 59

##8. For ls
Write a Bash script that displays:

The content of the current directory
In a list format
Where only the part of the name after the first dash is displayed 

##9. To file, or not to file
Write a Bash script that gives you information about the holbertonschool file.

Requirements:

You must use if and, else (case is forbidden)
Your Bash script should check if the file exists and print:
if the file exists: holbertonschool file exists
if the file does not exist: holbertonschool file does not exist
If the file exists, print:
if the file is empty: holbertonschool file is empty
if the file is not empty: holbertonschool file is not empty
if the file is a regular file: holbertonschool is a regular file
if the file is not a regular file: (nothing)

##10. FizzBuzz
Write a Bash script that displays numbers from 1 to 100.

Requirements:

Displays FizzBuzz when the number is a multiple of 3 and 5
Displays Fizz when the number is multiple of 3
Displays Buzz when the number is a multiple of 5
Otherwise, displays the number
In a list format

##11. Read and cut

Write a Bash script that displays the content of the file /etc/passwd.

Your script should only display:

username
user id
Home directory path for the user

Requirements:

You must use the while loop (for and until are forbidden)

##12. Tell the story of passwd

Write a Bash script that displays the content of the file /etc/passwd, using the while loop + IFS.

Format: The user USERNAME is part of the GROUP_ID gang, lives in HOME_DIRECTORY and rides COMMAND/SHELL. USER ID's place is protected by the passcode PASSWORD, more info about the user here: USER ID INFO

Requirements:

You must use the while loop (for and until are forbidden)

##13. Let's parse Apache logs

Write a Bash script that displays the visitor IP along with the HTTP status code from the Apache log file.

Requirement:

Format: IP HTTP_CODE
in a list format

Requirements:

You must use awk
You are not allowed to use while, for, until and cut

##14. Dig the data 

Using what you did in the previous exercise, write a Bash script that groups visitors by IP and HTTP status code, and displays this data.

Requirements:

The exact format must be:
OCCURENCE_NUMBER IP HTTP_CODE
In list format
Ordered from the greatest to the lowest number of occurrences

Requirements:

You must use awk
You are not allowed to use while, for, until and cut