from flask import Flask, render_template, request, redirect, url_for
import os
import smtplib

app = Flask(__name__)

user_email = "YOUR_EMAIL"
password = "YOUR PASSWORD"


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['Name']
        email = request.form['Email']
        subject = request.form['Subject']
        message = request.form['Message']
        send_email(name=name, email=email, subject=subject, message=message)
        return redirect(url_for('home'))
    return render_template('index.html')


def send_email(name, email, subject, message):
    email_message = f"Subject:{subject}\n\nName: {name}\nEmail: {email}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=user_email, password=password)
        connection.sendmail(from_addr=user_email, to_addrs=email,
                            msg=email_message)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
