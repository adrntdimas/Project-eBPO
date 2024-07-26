from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class StatusEnum(models.TextChoices):
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    DISCONTINUED = 'Discontinued'

class ActivityEnum(models.TextChoices):
    PLACEBO = 'Placebo'
    FORMULATION_1 = 'Formulation 1'
    FORMULATION_2 = 'Formulation 2'
    FORMULATION_3 = 'Formulation 3'

class MasterProduct(models.Model):
    product_code = models.CharField(unique=True, max_length=50)
    generic_name = models.CharField(max_length=250)
    brand_name = models.CharField(max_length=250)
    dosage_form = models.CharField(max_length=100)
    strength = models.DecimalField(max_digits=10, decimal_places=3)
    unit_strength = models.CharField(max_length=25)
    product_status = models.CharField(
        max_length=50,
        choices=StatusEnum.choices,
        default=StatusEnum.INACTIVE
    )
    registration_number = models.CharField(max_length=100)
    registration_owner = models.CharField(max_length=100)
    expired_reg_number = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'master_product'

class MasterFormula(models.Model):
    product_id = models.ForeignKey(MasterProduct, on_delete=models.CASCADE, db_column='product_id')
    formula_code = models.CharField(unique=True, max_length=50)
    aktivitas_formulasi = models.TextField(
        max_length=50,
        choices=ActivityEnum.choices,
        default=ActivityEnum.FORMULATION_1    
    )
    batch_size = models.IntegerField()
    status_formula = models.CharField(
        max_length=50,
        choices=StatusEnum.choices,
        default=StatusEnum.INACTIVE
    )

    class Meta:
        managed = True
        db_table = 'master_formula'

class MasterMaterialPhase(models.Model):
    phase_name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'master_material_phase'

class MasterMaterial(models.Model):
    material_code = models.CharField(unique=True, max_length=50)
    material_name = models.CharField(max_length=255)
    standard = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=50)
    supplier = models.CharField(max_length=255)
    material_status = models.TextField(
        max_length=50,
        choices=StatusEnum.choices,
        default=StatusEnum.ACTIVE
    )

    class Meta:
        managed = True
        db_table = 'master_material'

class BillOfMaterials(models.Model):
    formula_id = models.ForeignKey('MasterFormula', models.CASCADE, db_column='formula_id')
    material_phase_id = models.ForeignKey('MasterMaterialPhase', models.CASCADE, db_column='material_phase_id')
    material_id = models.ForeignKey('MasterMaterial', models.CASCADE, db_column='material_id')
    quantity_per_unit = models.DecimalField(max_digits=10, decimal_places=5)
    quantity_per_batch = models.DecimalField(max_digits=10, decimal_places=5, editable=False)

    class Meta:
        managed = True
        db_table = 'bill_of_materials'

# kalkulasi quantity dalam satu batch
    def save(self, *args, **kwargs):
        self.quantity_per_batch = self.quantity_per_unit * self.formula_id.batch_size
        super(BillOfMaterials, self).save(*args, **kwargs)