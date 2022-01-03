'''
Example taken from https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/

Details about figlet itself are here: http://www.figlet.org/
Details about pyfiglet are here: https://github.com/pwaller/pyfiglet


You need to import pyfiglet before running this code:

pip install pyfiglet

'''


# import pyfiglet module
import pyfiglet

# Render in the default font...(not sure what this is...)  
result = pyfiglet.figlet_format("ajpowell")
print(result)

# Render in the specified font (this this case 'doom')
# Range of fonts available can be seen here: http://www.jave.de/figlet/fonts/overview.html
# Not necessary to download the font, just give the name in the function call
result = pyfiglet.figlet_format("ajpowell", font='doom')
print(result)
