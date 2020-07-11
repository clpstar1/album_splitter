# Album Splitter

## Description
A simple Python script to split a large Audio File into single files by providing
track titles and timestamps

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

1. Retrieve Splitting Information from a File
    * Create a file of format titleDELIMduration  
      for each output file to be generated
    * specify the command file with --commfile
    * specify DELIM with --delim 
    * run the program
2. Retrieve Splitting Information from Discogs
    * Go to discogs.com and find the proper release  
      for example https://www.discogs.com/de/Orbital-In-Sides/release/130793
    * specify the url with --url
    * run the program

