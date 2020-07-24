# import libraries
import smtplib
from email.message import EmailMessage
import imghdr

# email id and password credentials
email_address = input('Enter your email address')
print('Note: please provide generated app password ')
password = input('Enter your password')  # Enter your app password or make yor email as less secure apps
to_address = input('Enter email address of receiver')

msg = EmailMessage()
msg['Subject'] = input('Enter Subject of your mail')
msg['From'] = email_address
msg['To'] = to_address
msg.set_content(input('Enter body of your mail'))

# ask user for is any Sattachments
is_attachment = ''
while is_attachment not in ('Y', 'N'):
    is_attachment = input('Do you want to attach any files ( Y or N)').upper()
# we can add images and documents is attchment
if is_attachment == 'Y':
    print('yes')
    number_of_files = ''
    while True:
        try:
            number_of_files = int(input('Enter number of files to attach :'))
            if number_of_files > 0:
                break
            else:
                continue
        except ValueError:
            continue
    files = []
    for i in range(0, number_of_files):
        while True:
            try:
                input_name = input('enter file name with extension :')
                test = open(input_name, 'rb')
            except FileNotFoundError:
                print('file not exist')
                continue
            else:
                files.append(input_name)
                print(f'{i+1} files added')
                break
    for file in files:
        if file.endswith('.jpg', -4, -1) or file.endswith('.png', -4, -1):
            with open(file, 'rb') as f:
                file_data = f.read()
                file_type = imghdr.what(f.name)
                file_name = f.name

            msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
        else:
            with open(file, 'rb') as f:
                file_data = f.read()
                file_name = f.name
                msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
    print('Sending mail ......')


elif is_attachment == 'N':
    print('Sending email without attachments.....')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    while True:
        try:
            smtp.login(email_address, password)
        except smtplib.SMTPAuthenticationError:
            print('Authentication failed')
            email_address = input('Please re enter your email ID')
            password = input('please re enter your password')
            continue
        else:
            break

    try:
        smtp.send_message(msg)
    except smtplib.SMTPRecipientsRefused:
        print('The Recipient address is not valid')
    else:
        print('Success')
