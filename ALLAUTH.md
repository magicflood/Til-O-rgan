# django allauth

# in settings
'allauth',
'allauth.account',
'allauth.socialaccount',
'allauth.socialaccount.providers.google',




SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_VERIFICATION = "none"




# in middleware
'allauth.account.middleware.AccountMiddleware',


# in urls
path('accounts/', include('allauth.urls')),

# in google
client secret - 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
client id - 941066841101-d0a3fqub2lj8roc8tl1l6stelav8peiq.apps.googleusercontent.com

pip install requests
pip install jwt

1. go to - https://console.cloud.google.com/
2. create project
3. turn on "OAuth consent screen" (externaal)
4. Credentials → Create Credentials → OAuth Client ID
5. Authorized redirect URIs - http://127.0.0.1:8000/accounts/google/login/callback/
6. http://127.0.0.1:8000/admin
7. Social applications → Add
Provider: Google
Name: Google
Client id
Secret key
save
8. project/
│
├── templates/
│   └── account/
│       ├── login.html
│       ├── signup.html
│       └── logout.html

9. {% load socialaccount %}
{% load account %}

10. in login.html
    {% load socialaccount %}
    <a href="{% provider_login_url 'google' %}">Войти через Google</a>

    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Войти по email</button>
    </form>

11. <a href="{% url 'account_login' %}">Log in</a>