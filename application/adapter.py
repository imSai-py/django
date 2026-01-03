from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request, sociallogin):
        """
        Checks whether signup is allowed.
        If the user clicked 'Sign in' from the Login page (indicated by cookie),
        we block the signup of a new account to match the behavior:
        'If account exists -> login, if not -> error'.
        """
        # If the user is already authenticated, signup isn't happening (it's a connect), so this check is skipped by allauth logic usually.
        # But for an anonymous user triggering a new social login:
        
        # Check the cookie set by the button click
        auth_action = request.COOKIES.get('auth_action')
        
        # If they came from Login page, strict check:
        if auth_action == 'login':
            return False # Blocks signup, treating it as "Account doesn't exist"
            
        return True # Default allow (e.g. from Register page)
