# Functions to import a topographic map using Python
# and create a map to the required extent 

# import all dependencies
import rasterio
import matplotlib.pyplot as plt
from pathlib import Path

#All functions related to importing the topographic map
class ImportMap: 
        def __init__(self):
            self = self

    #Read elevation datasets into Python and return as object
        def import_and_merge_raster_file(path_to_raster):
            path = path_to_raster
            #Create an output folder for the mosaic raster
            Path('output').mkdir(parents=True, exist_ok=True)
            output_path = 'output/mosaic_output.tif'
            #Read in all the rasters
            raster_files = list(path.iterdir())
            raster_to_mosiac = []
            #loop through files and create a list of raster files to merge
            for p in raster_files:
                raster = rasterio.open(p)
                raster_to_mosiac.append(raster)
            #merge all the rasters
            mosaic, output = rasterio.merge(raster_to_mosiac)
            #update the mosaic raster's metadata to match the new height and width
            output_meta = raster.meta.copy()
            output_meta.update(
                {"driver": "GTiff",
                "height": mosaic.shape[1],
                "width": mosaic.shape[2],
                "transform": output,
            }
            )
            #write the mosaic file to the output directory
            with rasterio.open(output_path, "w", **output_meta) as m:
                m.write(mosaic)
            #return the mosaic as an object
            return mosaic

    #Stitch grid squares together



    #Mask map according to country shape


# Mask map according to user defined shape

    #Mask map according to user defined shape



