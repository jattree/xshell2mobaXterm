import os
import configparser
import re

# Get all .xsh files in the current directory
files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.xsh')]

# Output file
output_file = 'MobaXterm Sessions.mxtsessions'

# Initial bookmark index
bookmark_index = 1

# Iterate through .xsh files
for file in files:
    # Create a ConfigParser object
    config = configparser.ConfigParser()
    # Read the .xsh file
    config.read(file)

    # Get Host and UserName from [CONNECTION] and [CONNECTION:AUTHENTICATION] sections
    host = config.get('CONNECTION', 'Host', fallback=None)
    username = config.get('CONNECTION:AUTHENTICATION', 'UserName', fallback=None)

    # If Host and UserName are found, create a bookmark
    if host and username:
        # Create a bookmark section
        bookmark = f"[Bookmarks_{bookmark_index}]"
        subrep = "SubRep=SCRT sessions"
        imgnum = "ImgNum=208"
        session = f"{re.sub('.xsh', '', file)}= #109#0%{host}%22%{username}% %-1%-1% %%22%%0%0%Interactive shell% "

        # Write to the output file
        with open(output_file, 'a') as f:
            f.write(f"{bookmark}\n{subrep}\n{imgnum}\n{session}\n")

        # Increment bookmark index
        bookmark_index += 1
