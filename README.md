# Vehicle Transportation

Vehicle Transportation is a python algorithm that checks how three different vehicles deliver "French yumminess" to almost a thousand major locations around the world 

## Installation

1. Clone the repository or download the source code files.
2. Ensure you have at least Python 3.10 installed on your machine.
3. You must install the following modules in order for the program to be run
   1. pip install basemap 
      1. If this doesn't succeed initially due to errors such as ERROR: Failed building wheel for Basemap, Failed to build Basemap, ERROR: Could not build wheels for Basemap, which is required to install pyproject.toml-based projects
      2. Call this first: brew install geos proj numpy matplotlib
   2. pip install matplotlib
   3. pip install geopy
   4. pip install tabulate
   5. pip install networkx
4. pip freeze > requirements.txt

## Usage

To start the program, run the `onboard_navigation.py` file:

```shell
python onboard_navigation.py