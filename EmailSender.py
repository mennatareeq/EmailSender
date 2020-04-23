


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

''' ------------------------
This is the account i created for the purpose of this project you can use it to test
from is the sender address
to is the reciever you can add multiple recepient just by adding a comma between them 
also there is a CC and BCC here thy are commented if you want them just uncomment them 
------------------------
'''
fromaddr = "ls4373182@gmail.com"
toaddr = "swalk10@gmail.com" 
toCC = "scwalk10@gmail.com"

#toCC = "ghi@gmail.com,jkl@hotmail.com,mnopq@yahoo.com" # Write all the email ids that you want to be present in CC, separated by commas.

#toBCC = "ghi@gmail.com,jkl@hotmail.com,mnopq@yahoo.com" # Bcc as CC


''' ------------------------ Uncomment the CC and BCC if needed ------------------------ '''
toaddrs = [toaddr]  # + toCC.split(",") # +toBCC.split(",")

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
#msg['CC'] = toCC
#msg['BCC'] = toBCC


''' ---------------------------------------------- Subject And Body ----------------------------------------------'''
msg['Subject'] = "Test Subject"
body = '''Dear Scott ,
This is a sample code to send email.
Thanks,
Python
'''


''' ------------------------ attachement ------------------------ '''
msg.attach(MIMEText(body, 'plain'))

#C:\EPSData
filename = 'C:/EPSData/sp-500-eps-est-2018-12-20.xlsx' #Please Enter Your Location Here
f = open(filename)
attachment = MIMEText(f.read())
attachment.add_header('Content-Disposition', 'attachment', filename=filename)           
msg.attach(attachment)


import smtplib

''' Setting the server to send the email '''
server = smtplib.SMTP(host='smtp.gmail.com', port=587) 
server.ehlo()
server.starttls()
server.ehlo()
server.login("ls4373182@gmail.com", "Hqc4ba9kw") #Give your id and password here'''
text = msg.as_string()
server.sendmail(fromaddr, toaddrs, text)
server.quit()