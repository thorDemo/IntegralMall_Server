from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication


class RATokenAuthentication(TokenAuthentication):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)


class RASessionAuthentication(SessionAuthentication):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)


class RABasicAuthentication(BasicAuthentication):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
