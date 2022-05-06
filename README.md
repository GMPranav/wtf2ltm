# WTF2LTM

[WTF](https://tasvideos.org/EmulatorResources/Hourglass/WTF) (**W**indows **T**AS **F**ile) to [LTM](https://tasvideos.org/EmulatorResources/LibTAS/LTMFormat) (**L**ib**T**AS **M**ovie) is a simple script that takes .wtf files as inputs and outputs a text file with libTAS frame input data. Note that it only outputs the "inputs" part of the .ltm file, and not the entire ltm file. It should be possible to copy paste it in libTAS input editor.

## Requirements

* Python installed

## Usage

* Download the python script
* Open command window in the folder containing wtf2ltm.py
* Run `wtf2ltm.py -f path/to/file.wtf` (where `path/to/file.wtf` is ofcourse the actual path to the .wtf file. Or just the filename if its in the same folder)
* The output file `inputs` (with no file extension) will be created in the same extension
* You can either pack it if you know how to edit ltm files properly, or open it in text editor to copy the inputs
