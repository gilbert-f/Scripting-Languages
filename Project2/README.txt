Instructions

generate_input.sh is the source code for generating the input txt file for the awk script. input.txt is the input txt file for the awk script.
script.awk is the source code for generating the html file. output.html is the expected output of the awk script.

1. Unzip HW2 file.
2. Unzip Music.tar file.
2. Use cd command on your terminal to go to HW2 directory.
3. Ask for permission to run generate_input.sh by inputting command chmod +x generate_input.sh on your terminal.
4. Run generate_input.sh by inputting the command ./generate_input.sh > input.txt on your terminal to get the input file for the awk script.
5. Pipe the input.txt file to the awk script by inputting the command cat input.txt | awk -f script.awk on your terminal.
