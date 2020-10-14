import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from_addr = 'debjitbhowmik807@gmail.com'
to_addr= ['dipakbhaumik12@gmail.com', 'debjitbhowmik1998@gmail.com']
msg= MIMEMultipart()
msg['From'] = from_addr
msg['To']= ",".join(to_addr)
msg['subject']= 'Test Mail'

body= 'Hi there!, This is the test mail which I am sending to check'

msg.attach(MIMEText(body, 'plain'))

email = "debjitbhowmik807"
password = "Enter your Password"

mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login(email, password)
text = msg.as_string()
mail.sendmail(from_addr, to_addr, text)
mail.quit()