from rest_framework import viewsets
from .models import *
from .serializers import *

class MasterProductViewSet(viewsets.ModelViewSet):
    queryset = MasterProduct.objects.all()
    serializer_class = MasterProductSerializer

class MasterFormulaViewSet(viewsets.ModelViewSet):
    queryset = MasterFormula.objects.all()
    serializer_class = MasterFormulaSerializer

class MasterMaterialPhaseViewSet(viewsets.ModelViewSet):
    queryset = MasterMaterialPhase.objects.all()
    serializer_class = MasterMaterialPhaseSerializer

class MasterMaterialViewSet(viewsets.ModelViewSet):
    queryset = MasterMaterial.objects.all()
    serializer_class = MasterMaterialSerializer

class BillOfMaterialsViewSet(viewsets.ModelViewSet):
    queryset = BillOfMaterials.objects.all()
    serializer_class = BillOfMaterialsSerializer
