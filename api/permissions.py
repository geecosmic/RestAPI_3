from rest_framework.permissions import BasePermission, SAFE_METHODS

# class IsPublicEndpoint(BasePermission):
#     """
#     Allow anyone to list (GET) the members.
#     """
#     def has_permission(self, request, view):
#         return request.method in SAFE_METHODS  # Allow GET, HEAD, OPTIONS


class IsPublicEndpoint(BasePermission):
    def has_permission(self, request, view):
        return True  # Allow all GET requests (public access)
    

class IsAuthenticatedEndpoint(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated  # Allow authenticated users





class IsOwner(BasePermission):
    """
    Custom permission to only allow the owner (yourself) to access the view.
    """

    def has_permission(self, request, view):
        # Only allow access if the user is authenticated and their username matches yours
        return request.user.is_authenticated and request.user.username == 'your_username'  # Replace with your actual username
