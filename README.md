# album_splitter - simple python script to split a large mp3 file into parts by providing the timestamps and titles 

## Requirements
* ffmpeg must be in PATH
* virtualenv to (optionally) create a virtual environment

## Installation

* clone the archive with:\
    ```git clone git@github.com:clpstar1/album_splitter.git```

* navigate to the cloned archive and create a virtual environment:\
    ```cd folder_name && virtualenv .```

* activate the environment and install the dependencies:\
    ```source bin/activate```\
    ```pip install -r requirements.txt```

* run with ```python3 splitter.py args```

## Usage 

1. Splitting Information from a File
    * Create a file of format titleDELIMduration
    * specify the command file with --commfile
    * specify DELIM with --delim 
    * run the program
2. Splitting Information from Discogs
    * Go to discogs.com and find the proper release  
      for example https://www.discogs.com/de/Orbital-In-Sides/release/130793
    * specify the url with --url
    * run the program

