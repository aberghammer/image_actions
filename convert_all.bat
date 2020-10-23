ECHO OFF
ECHO Conversion of all images
python extract_crop.py -i Wizard/ --save
python extract_crop.py -i Which/ --save
python extract_crop.py -i Warrior/ --save
python extract_crop.py -i Pirate/ --save
