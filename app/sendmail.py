import os
import smtplib
from email.message import EmailMessage

noreplyemail = os.getenv("noreplyemail")
noreplykennwort = os.getenv("noreplykennwort")


def send_mail(to, token, username, email=noreplyemail, kennwort=noreplykennwort):
    msg = EmailMessage()
    msg.add_alternative(
        f"""\
<html>
  <head>

    <title>Document</title>
  </head>
  <body>
    <div id="box">
      <h2>Guten Tag {username}, Ihr Olympiateam heißt Sie herlich Willkommen!</h2> 
        <p> Deine Registrierung wurde erfolgreich! Durch die Aktivierung erklärst du dich einverstanden mit unseren 
            <a href="http://localhost/datenschutz/
            Datenschutzrichtlinien.
            </a>
            <a href="http://olymp.internal:8000/verify/{token}">
                "Einverstanden. Konto aktievieren."
            </a> 
        </p>
      </form>
    </div>
  </body>
</html>

<style>
  #box {{
    margin: 0 auto;
    max-width: 500px;
    border: 1px solid black;
    height: 200px;
    text-align: center;
    background: lightgray;
  }}

  p {{
    padding: 10px 10px;
    font-size: 18px;
  }}

  .inline {{
    display: inline;
  }}

  .link-button {{
    background: none;
    border: none;
    color: blue;
    font-size: 22px;
    text-decoration: underline;
    cursor: pointer;
    font-family: serif;
  }}
  .link-button:focus {{
    outline: none;
  }}
  .link-button:active {{
    color: red;
  }}
</style>
    """,
        subtype="html",
    )

    msg["Subject"] = "Bestätigung deiner Registrierung"
    msg["From"] = noreplyemail
    msg["To"] = to

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(noreplyemail, noreplykennwort)
    server.send_message(msg)
    server.quit()
