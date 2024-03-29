from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class IsSupporterOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        #allow read access for any object by any user
        if request.method in permissions.SAFE_METHODS:
            return True
            # only allow write access if the object is owned by the logged in user
        return obj.supporter == request.user