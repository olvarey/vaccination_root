from django.db import models

######################################################################################
# DEPARTMENT
######################################################################################
class Department(models.Model):

    department_name = models.CharField(
        max_length=500,
        verbose_name="Departamento",
        db_column="department_name",
    )

    class Meta:
        db_table = "department"
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        ordering = ["department_name"]

    def __str__(self):
        return self.department_name


######################################################################################
# MUNICIPALITY
######################################################################################
class Municipality(models.Model):
    municipality_name = models.CharField(
        max_length=500,
        verbose_name="Municipio",
        db_column="municipality_name",
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.RESTRICT,
        verbose_name="Departamento",
    )

    class Meta:
        db_table = "municipality"
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"
        ordering = ["department"]

    def __str__(self):
        return f"{self.department} >> {self.municipality_name}"


######################################################################################
# GENDER
######################################################################################
class Gender(models.Model):
    gender_name = models.CharField(
        max_length=500,
        verbose_name="Género",
        db_column="gender_name",
    )

    class Meta:
        db_table = "cat_gender"
        verbose_name = "Género"
        verbose_name_plural = "Generos"
        ordering = ["gender_name"]

    def __str__(self):
        return self.gender_name


######################################################################################
# POSITION
######################################################################################
class Position(models.Model):
    position_name = models.CharField(
        max_length=500,
        verbose_name="Cargo",
        db_column="position_name",
    )

    class Meta:
        db_table = "cat_position"
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
        ordering = ["position_name"]

    def __str__(self):
        return self.position_name


######################################################################################
# PROFESSION
######################################################################################
class Profession(models.Model):
    profession_name = models.CharField(
        max_length=500,
        verbose_name="Profesión",
        db_column="profession_name",
    )

    class Meta:
        db_table = "cat_profession"
        verbose_name = "Profesión"
        verbose_name_plural = "Profesiones"
        ordering = ["profession_name"]

    def __str__(self):
        return self.profession_name


######################################################################################
# ORGANIZATIONAL UNIT
######################################################################################
class OrgUnit(models.Model):
    org_unit_name = models.CharField(
        max_length=500,
        verbose_name="Unidad organizativa",
        db_column="org_unit_name",
    )

    class Meta:
        db_table = "cat_org_unit"
        verbose_name = "Unidad organizativa"
        verbose_name_plural = "Unidades organizativas"
        ordering = ["org_unit_name"]

    def __str__(self):
        return self.org_unit_name


######################################################################################
# VACCINE TYPE
######################################################################################
class VaccineType(models.Model):
    vaccine_type_name = models.CharField(
        max_length=500,
        verbose_name="Nombre de vacuna",
        db_column="vaccine_type_name",
    )

    class Meta:
        db_table = "cat_vaccine_type"
        verbose_name = "Tipo de vacuna"
        verbose_name_plural = "Tipos de vacuna"
        ordering = ["vaccine_type_name"]

    def __str__(self):
        return self.vaccine_type_name


######################################################################################
# EMPLOYEE
######################################################################################
class Employee(models.Model):
    full_name = models.CharField(
        max_length=500,
        verbose_name="Nombre completo",
        db_column="full_name",
    )

    dui = models.CharField(
        max_length=50,
        verbose_name="DUI",
        db_column="dui",
    )

    phone_number = models.CharField(
        max_length=100,
        verbose_name="Teléfono",
        db_column="phone_number",
        null=True,
        blank=True,
    )

    birth_date = models.DateField(
        verbose_name="Fecha de nacimiento",
        db_column="birth_date",
        null=True,
        blank=True,
    )

    address = models.TextField(
        verbose_name="Dirección",
        db_column="address",
        null=True,
        blank=True,
    )

    author = models.ForeignKey(
        "auth.User",
        on_delete=models.RESTRICT,
        verbose_name="Autor",
    )

    gender = models.ForeignKey(
        Gender,
        on_delete=models.RESTRICT,
        verbose_name="Género",
        null=True,
        blank=True,
    )

    position = models.ForeignKey(
        Position,
        on_delete=models.RESTRICT,
        verbose_name="Cargo",
        null=True,
        blank=True,
    )

    profession = models.ForeignKey(
        Profession,
        on_delete=models.RESTRICT,
        verbose_name="Profesión",
        null=True,
        blank=True,
    )

    org_unit = models.ForeignKey(
        OrgUnit,
        on_delete=models.RESTRICT,
        verbose_name="Unidad organizativa",
        null=True,
        blank=True,
    )

    municipality = models.ForeignKey(
        Municipality,
        on_delete=models.RESTRICT,
        verbose_name="Departamento / Municipio",
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "employee"
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name


######################################################################################
# BOOSTER
######################################################################################
class Booster(models.Model):
    booster_date = models.DateField(
        verbose_name="Fecha de dosis",
        db_column="booster_date",
        null=True,
        blank=True,
    )

    vaccine_type = models.ForeignKey(
        VaccineType,
        on_delete=models.RESTRICT,
        verbose_name="Tipo de vacuna",
        null=True,
        blank=True,
    )

    employee = models.ForeignKey(
        Employee,
        on_delete=models.RESTRICT,
        verbose_name="Empleado",
    )

    class Meta:
        db_table = "booster"
        verbose_name = "Dosis"
        verbose_name_plural = "Dosis"
        ordering = ["booster_date"]

    def __str__(self):
        return f"{self.vaccine_type} >> {self.booster_date}"


######################################################################################
# CONFIRMED COVID CASE
######################################################################################
class ConfirmedCovidCase(models.Model):
    inhability_start_date = models.DateField(
        verbose_name="Fecha de inicio incapacidad",
        db_column="inhability_start_date",
        null=True,
        blank=True,
    )

    inhability_end_date = models.DateField(
        verbose_name="Fecha de finalización incapacidad",
        db_column="inhability_to_date",
        null=True,
        blank=True,
    )

    hospitalized = models.BooleanField(
        verbose_name="Hospitalizado",
        db_column="hospitalized",
        null=True,
        blank=True,
    )

    employee = models.ForeignKey(
        Employee,
        on_delete=models.RESTRICT,
        verbose_name="Empleado",
    )

    class Meta:
        db_table = "confirmed_covid_case"
        verbose_name = "Caso COVID confirmado"
        verbose_name_plural = "Casos COVID confirmados"
        ordering = ["inhability_start_date"]

    def __str__(self):
        return f"{self.inhability_start_date} >> {self.inhability_end_date}"


######################################################################################
# SUSPICIOUS COVID CASE
######################################################################################
class SuspiciousCovidCase(models.Model):
    suspicion_start_date = models.DateField(
        verbose_name="Fecha de inicio incapacidad por sospecha",
        db_column="suspicion_start_date",
        null=True,
        blank=True,
    )

    suspicion_end_date = models.DateField(
        verbose_name="Fecha de finalización incapacidad por sospecha",
        db_column="suspicion_end_date",
        null=True,
        blank=True,
    )

    employee = models.ForeignKey(
        Employee,
        on_delete=models.RESTRICT,
        verbose_name="Empleado",
    )

    class Meta:
        db_table = "suspicious_covid_case"
        verbose_name = "Caso COVID sospechoso"
        verbose_name_plural = "Casos COVID sospechosos"
        ordering = ["suspicion_start_date"]

    def __str__(self):
        return f"{self.suspicion_start_date} >> {self.suspicion_end_date}"
