from rest_framework.permissions import BasePermission

class CanCreateClientPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_commercial()

class CanUpdateOwnClientPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_commercial() and obj.sales_contact == request.user

class CanUpdateOwnContractPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_commercial() and obj.client.sales_contact == request.user

class CanManageCollaboratorsPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_manager()

class CanModifyAllContractsPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_manager()

class CanViewAssignedEventsPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_support()

class CanUpdateOwnEventPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_support() and obj.support_contact == request.user
