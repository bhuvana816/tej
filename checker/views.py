from django.shortcuts import render

def check_password(request):
    strength = None
    password = ''
    if request.method == "POST":
        password = request.POST.get('password')
        length = len(password)
        if length < 6 or password.isdigit() or password.isalpha():
            strength = "Weak"
        elif any(c.isdigit() for c in password) and any(c.isalpha() for c in password):
            strength = "Moderate"
        if (any(c.isdigit() for c in password)
            and any(c.isalpha() for c in password)
            and any(c in "!@#$%^&*()_+" for c in password)
            and len(password) >= 8):
            strength = "Strong"
    return render(request, 'checker/index.html', {'strength': strength, 'password': password})
