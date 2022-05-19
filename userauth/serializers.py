from rest_framework import serializers
# from django.contrib.auth.models import User
from userauth.models import userAccount

# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ('user', 'image', 'phone', 'location')

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    # phone = ProfileSerializer()
    class Meta:
        model = userAccount
        fields = ('username', 'email','phone', 'password', 'password2')
        extra_kwargs = {
            'password':{'write_only':True}
        }
    def save(self):
        user = userAccount(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            phone=self.validated_data['phone'],
            
        )
        password = self.validated_data['password']
        password2 =self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'Password must match'})
        user.set_password(password)
        user.save()
        return user