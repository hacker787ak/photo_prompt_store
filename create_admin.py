import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'photoprompt.settings')
django.setup()
from django.contrib.auth.models import User
if not User.objects.filter(username='hacker787ak').exists():
    User.objects.create_superuser('hacker787ak', 'akshay@example.com', 'Password123@')
    print("Admin created successfully!")
else:
    print("Admin already exists.")
