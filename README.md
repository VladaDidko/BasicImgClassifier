# BasicImgClassifier
There are three types of img similarity:
* duplicate (images which are exactly the same)
* modification (images which differ by size, blur level and/or noise filters)   
* similar (images of the same scene from another angle) 

*This console app searches for all three types of images in a given folder*
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

## Prerequisites
You need Python 3.7, pip to be installed
Also you need to install the following packages:
pip install Pillow
pip install numpy

After cloning or downloading the project open command prompt and change the directory to the project folder:

*cd C:\Users\[name]\BasicImgClassifier*

## Usage Example
from the project folder type:  
*python solution.py*

You will get error:  
*usage: solution.py [-h] --path PATH*  
*solution.py: error: the following arguments are required: --path*

To solve it, add path to the image folder:  
*python solution.py --path  ./dataset

This will print filenames of similar pairs of images in a given folder
