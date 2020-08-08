## Purpose 

   This is a python3 script to read lines of qso information from a simple text file and parse it into an ADX formatted file for importing into any logging program that accepts adx format.

   The idea is that I often use a very simple handwritten log, and this tool makes it easy to get that handwritten data into a logging file by creating a simple text file as an intermediate step.

   If I have many handwritten contacts I'll have the xyl read the logbook out loud while I type the values into the text file, hitting the spacebar in between the fields. Very fast. 

   I suppose you could also use a dictation program also.

   For the adx format see adif.org website.
   
## Instructions

   The input file which this script reads must be named textinput.txt.

   Each QSO is a single line of the text file following the format of the physical hand-written ARRL Logbook, which is: 

`date/freq/mode/power/time/station worked/report sent/report rec'd/time off/comments`

   Note that with comments, the qth, name, qsl via, qsl s, qsl r are not mapped into the adx, they will remain in the COMMENT data field and you can move them over once they are in your digital log.

## The Deets

   In your text input file:

-Data can be either upper or lower case, the script converts it all to upper case.
-The field should be separated by spaces, and only the Comments can have spaces, all other data should have no spaces within them.
-All 10 fields must be included, but can be "0" if you want to keep it blank
-The date should be entered as 20200730 to represent July 30 2020
-The frequency should be entered in kHz, and can include decimals.
-The script will convert, say 14062.9 to 14.0629 in the adx.
-The time should be entered as 0435 to represent 4:35 UTC.
-The time should be entered as 1422 to represent 14:22 UTC
-The Time Off can be entered as "t" and the program will just use the Time field (Time off will equal time on). I never record the time off, but i probably should :)
   
## Example

   Below are valid text lines for a file:

`20201127 14062 cw 100 1950 kt0a 559 579 t sota w0d/bb-033  8pts`
`20210727 7034 cw 100 2140 ke7bgm 559 559 2145 sota w6/nd-037  8pts` 
`20211027 5332 usb 100 2152 k6hpx 559 579 2155 gud dx`

   Don't put empty lines in the input text file

