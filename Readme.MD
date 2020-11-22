
To generate the json. The labelimg tool was used.
Just select "Create ML" as saving method and use the created json file.


Example usage for cropping:

-p "<path-to-image>/my_images" 

-i "/subfolder_with_images" 

-j "/subfolder_with_images/<name_of_json>.json" 

-o "/subfolder_for_results/" 

--save