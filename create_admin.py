import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'photoprompt.settings')
django.setup()
from django.contrib.auth.models import User

username = 'hacker787ak'
email = 'akshay@example.com'
password = 'Password1234@'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"Superuser {username} created successfully!")
else:
    print(f"Superuser {username} already exists.")
