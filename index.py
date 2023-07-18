import smtplib
import random


def send_otp_email(receiver_email, receiver_name, otp):
    sender_email = "pindisandeep28@gmail.com"  # Replace with your email address
    sender_password = "ztkmhxifwcyiaqsw"  # Replace with your email password

    subject = "OTP Verification"
    message = f" Dear{receiver_name}, \n\nYour OTP is: {otp}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(
            sender_email, receiver_email, f"Subject: {subject}\n\n{message}"
        )
        server.quit()
        print("OTP sent successfully!")
    except smtplib.SMTPException as e:
        print("Error occurred while sending OTP:", e)


def generate_otp():
    digits = "0123456789"
    otp = ""
    for _ in range(6):
        otp += random.choice(digits)
    return otp


def verify_otp(entered_otp, otp):
    return entered_otp == otp


# Simulate user entering the email address
receiver_email = input("Enter your email: ")
receiver_name = input("Enter your name: ")

# Generate and send OTP
otp = generate_otp()
send_otp_email(receiver_email, receiver_name, otp)

# Simulate user entering the OTP
entered_otp = input("Enter the OTP: ")

# Verify the entered OTP
if verify_otp(entered_otp, otp):
    print("OTP verification successful!")
else:
    print("OTP verification failed!")
