from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from django.conf import settings

def send_password_reset_email(user, token):
    subject = "Reset your password"
    to_email = user.email
    context = {
        "user": user,
        "token": token,
        "frontend_url": "your-frontend-url.com",
    }
    print("Email settings:", settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    html_content = render_to_string("reset_password_email.html", context)
    email = EmailMessage(subject, html_content, to=[to_email])
    email.content_subtype = "html"
    email.send()

    print("Password reset email sent to:", to_email)