import os

# 1. Settings.py ko fix karna
with open('photoprompt/settings.py', 'r') as f:
    lines = f.readlines()

with open('photoprompt/settings.py', 'w') as f:
    for line in lines:
        if "INSTALLED_APPS +=" in line:
            # Sirf kaam ke apps rakhna, allauth poora gayab
            f.write("    INSTALLED_APPS += ['store', 'crispy_forms', 'bootstrap5']\n")
        elif "AUTHENTICATION_BACKENDS" in line:
            # Is line ko poora delete kar dena
            continue
        else:
            f.write(line)

# 2. Urls.py ko fix karna
with open('photoprompt/urls.py', 'r') as f:
    urls = f.read()

urls = urls.replace("path('accounts/', include('allauth.urls')),", "")

with open('photoprompt/urls.py', 'w') as f:
    f.write(urls)

print("✅ Google Login aur Security module poori tarah delete ho gaya!")
