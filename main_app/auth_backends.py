from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User
from django.conf import settings

class DevBackend(BaseBackend):
    """
    Custom authentication backend for developers with hardcoded credentials.
    """
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        # List of developer credentials (username and plain password)
        dev_keys = [
            {
                'username': 'dev1',
                'password': 'dtbDev1!',  # Plain password
            },
            {
                'username': 'dev2',
                'password': 'dtbDev2!',  # Plain password
            },
            {
                'username': 'dev3',
                'password': 'dtbDev3!',  # Plain password
            },
            # Add more developer credentials as needed
        ]
        
        # Check if the username matches any developer username
        for dev in dev_keys:
            if dev['username'] == username:
                # Check if the password matches (plain text comparison for dev accounts)
                if dev['password'] == password:
                    try:
                        # Try to get the existing user
                        user = User.objects.get(username=username)
                    except User.DoesNotExist:
                        # Create a new user if it doesn't exist
                        user = User(username=username)
                        user.is_staff = True  # Give staff privileges
                        user.set_password(password)
                        user.save()
                        
                        # Create a profile for the developer
                        from .models import Profile
                        Profile.objects.create(user=user)
                    
                    return user
        
        # Return None if authentication fails
        return None
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
