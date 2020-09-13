'''
   See README.md
'''
#
# OPEN THE INPUT FILE
infile = open("textinput.txt", mode = "r")
# CREATE THE OUPTPUT FILE
outfile = open("adxforimport.adx", mode = "w")
#
# HEADING 
outfile.write('<?xml version="1.0" encoding="UTF-8"?>')
outfile.write("\n")
outfile.write('<ADX>')
outfile.write("\n")
outfile.write("\n")
outfile.write('  <HEADER>'+"\n"+'  </HEADER>'+"\n")
outfile.write("\n")
outfile.write('  <RECORDS>'+"\n")
outfile.write("\n")
#
# PARSE THE LINE INTO SEGMENTS
qso = infile.readline()
while qso:
  checkline = qso.split()[0][0:4]
  if checkline == 'date': 
    qso = infile.readline()
  qsosplit = qso.split()
  #pre-process the comment line
  comment = str(qsosplit[9:]).replace(',','')
  comment = comment.replace('[','')
  comment = comment.replace(']','')
  comment = comment.replace('\'','')
  #pre-process the timeoff line
  time_off = qsosplit[8]
  if(time_off == 't'):
      time_off = qsosplit[4]
  #write the data to the out file
  outfile.write('     <RECORD>'+
                '<QSO_DATE>'+qsosplit[0]+'</QSO_DATE>'+
                '<FREQ>'+str(float(qsosplit[1])/1000)+'</FREQ>'+
                '<MODE>'+qsosplit[2].upper()+'</MODE>'+
                '<TX_PWR>'+qsosplit[3]+'</TX_PWR>'+
                '<TIME_ON>'+qsosplit[4]+'</TIME_ON>'+
                '<CALL>'+qsosplit[5].upper()+'</CALL>'+
                '<RST_RCVD>'+qsosplit[6]+'</RST_RCVD>'+
                '<RST_SENT>'+qsosplit[7]+'</RST_SENT>'+
                '<TIME_OFF>'+time_off+'</TIME_OFF>'+
                '<COMMENT>'+comment.upper()+'</COMMENT>'+
                '</RECORD>'+"\n")
  qso = infile.readline()
  #
outfile.write("\n"+'  </RECORDS>')
outfile.write("\n")
outfile.write("\n")
outfile.write('</ADX>')
