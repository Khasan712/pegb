from rest_framework.generics import CreateAPIView
from v1.models.users import User, Staff
from v1.serializers.users import StaffRegisterSerializer, UserRegisterSerializer
from v1.utils.permissions import IsSuperUser


class StaffApi(CreateAPIView):
    queryset = Staff.objects.all()
    permission_classes = (IsSuperUser,)
    serializer_class = StaffRegisterSerializer
        

class CustomerRegisterApi(CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()


