from flask import Flask, render_template, request
from email.message import EmailMessage
import smtplib, ssl
import credentials


my_email =credentials.MY_EMAIL
my_password=credentials.MY_PASSWORD

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

    email_reciever = email
    email_subject = "Thank you for contacting me"
    email_body = f'''
    Thanks a lot of contacting me, I will get back to you as soon as possible.
    in mean time you can check out my github profile, linkedin profile and my resume.

    Thanks and Regards,
    Dheeraj Gajula
    '''

    em = EmailMessage()
    em["Subject"] = email_subject
    em["From"] = my_email
    em["To"] = email_reciever
    em.set_content(email_body)

    em_1 = EmailMessage()
    em_1["Subject"] = "Dheeraj , you've got a new message"
    em_1["From"] = my_email
    em_1["To"] = credentials.PERSONAL_NOTIFICATION
    personal_body = f"Name: {name} tried to you, with email {email} and message is {message}"
    em_1.set_content(personal_body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(my_email, my_password)
        server.sendmail(my_email, email_reciever, em.as_string())
        server.sendmail(my_email, credentials.PERSONAL_NOTIFICATION, em_1.as_string())


    

    
    print(name, email, message)

    return render_template("submit.html")




if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)