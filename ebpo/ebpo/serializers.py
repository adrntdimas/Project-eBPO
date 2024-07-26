from rest_framework import serializers
from .models import *

class MasterProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterProduct
        fields = '__all__'

class MasterFormulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterFormula
        fields = '__all__'

class MasterMaterialPhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterMaterialPhase
        fields = '__all__'

class MasterMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterMaterial
        fields = '__all__'

class BillOfMaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillOfMaterials
        fields = '__all__'
