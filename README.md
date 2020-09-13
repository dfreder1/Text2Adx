## Purpose 

   This is a python3 script to read lines of QSO information from a simple text file and parse it into an ADX-formatted file for importing into any logging program that accepts adx format.
   
   This script makes it convenient to use a simple textbfilebto input QSOs, providing a "distraction-free" logging program.

   It is also useful when you have handwritten log entries laying around on sticky notes or scratch paper. This tool makes it easy to get that handwritten data into a logging file by creating a simple text file as an intermediate step.

   If I have many handwritten contacts I'll have the xyl read them out loud while I type the values into the text file, hitting the spacebar in between the fields. Very fast. 

   I suppose you could also use a dictation program.

   For the adx format see adif.org website.
   
## Instructions

   The input file which this script reads must be named "textinput.txt". Enter your data into this file.

   Each QSO is a single line of the text file following the format of the physical hand-written ARRL Logbook, which is: 

`date/freq/mode/power/time/station worked/report sent/report rec'd/time off/comments`

   Note that ithis list does not include common items such as qth, name, qsl via, etc. I just put these in the comments data field and then move them over once they are in my digital log.

## The Deets

   In your text input file:

* You can make the first line:
"date/freq/mode/power/time/station worked/report sent/report rec'd/time off/comments" 
as a guide and the conversion script will ignore it.
* Data can be either upper or lower case, the script converts it all to upper case.
* Each field should be separated by spaces, except the Comments field which can have spaces, all other fields should have no spaces within them.
* All 10 fields must be included, but can be "0" if you want to keep it blank when it is mapped into the logging program
* The date should be entered as 20200730 to represent July 30 2020
* The frequency should be entered in kHz, and can include decimals.
* The script will convert to MHz, so if you input 14062.9 it will put 14.0629 in the adx.
* The time should be entered as 0435 to represent 4:35 UTC.
* The time should be entered as 1422 to represent 14:22 UTC
* The Time Off can be entered as "t" and the program will just use the Time field (time off will equal time on). 
   
## Example

   Below are valid text lines for a file (but don't use blank lines):

date/freq/mode/power/time/station worked/report sent/report rec'd/time off/comments

20201127 14062 cw 100 1950 kt0a 559 579 t sota w0d/bb-033  8pts

20210727 7034 cw 100 2140 ke7bgm 559 559 2145 sota w6/nd-037  8pts 

20211027 5332 usb 100 2152 k6hpx 559 579 2155 gud dx


