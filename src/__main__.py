##GeoPlot##

#Add the path to the root of the project to sys.path
from pathlib import Path
import sys
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))
print(sys.path)
sys.path.append(str("."))
print(sys.path)

#Import modules and initiate instances of each class
import src.importmap
print(f"Name: {__name__}")
print(f"Package: {__package__}")

#ImportMap = importmap.ImportMap()


#path = input("path to raster files")

#Import raster file and create mosaic 
#importmap.import_and_merge_raster_file(path)

##Plot samples on topographic maps




#def execute_main():
 #   if __name__ == "__main__":  # Condition to ensure module is executed not imported. 
 #       execute_main()



