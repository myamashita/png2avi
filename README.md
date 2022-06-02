# The script use imageio, gooey, glob, os, PIL, numpy


conda create --name CV2 python=3.9

conda activate CV2

pip install Gooey 
pip install pyinstaller
pip install imageio
pip install imageio-ffmpeg

pyinstaller -w --onefile --hidden-import imageio.plugins.ffmpeg PNG2AVI_GUI.py
