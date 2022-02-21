from rest_framework import serializers

from company.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        # fields = "__all__"
        fields = ('id', 'name', 'created_at', 'updated_at', 'status')

    def validate_name(self, value):
        if not value.isalnum():
            raise serializers.ValidationError('Name Company must have not special character.')
        return value

    def create(self, validated_data):
        company = Company.objects.create(**validated_data)
        company.save()
        return company

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
