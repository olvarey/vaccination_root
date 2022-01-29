from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportActionMixin
from django.contrib import admin
from .models import (
    Department,
    Municipality,
    Employee,
    Gender,
    Position,
    Profession,
    OrgUnit,
    VaccineType,
    Booster,
    ConfirmedCovidCase,
    SuspiciousCovidCase,
)


class DepartmentResource(resources.ModelResource):
    class Meta:
        model = Department


@admin.register(Department)
class DepartmentAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ["department_name"]
    search_fields = ["department_name"]
    resource_class = DepartmentResource


class MunicipalityResource(resources.ModelResource):
    class Meta:
        model = Municipality


@admin.register(Municipality)
class MunicipalityAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ["municipality_name"]
    search_fields = ["municipality_name"]
    resource_class = MunicipalityResource


class GenderResource(resources.ModelResource):
    class Meta:
        model = Gender


@admin.register(Gender)
class GenderAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ["gender_name"]
    search_fields = ["gender_name"]
    resource_class = GenderResource


class PositionResource(resources.ModelResource):
    class Meta:
        model = Position


@admin.register(Position)
class PositionAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ["position_name"]
    search_fields = ["position_name"]
    resource_class = PositionResource


class ProfessionResource(resources.ModelResource):
    class Meta:
        model = Profession


@admin.register(Profession)
class ProfessionAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ["profession_name"]
    search_fields = ["profession_name"]
    resource_class = ProfessionResource


class OrgUnitResource(resources.ModelResource):
    class Meta:
        model = OrgUnit


@admin.register(OrgUnit)
class OrgUnitAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ["org_unit_name"]
    search_fields = ["org_unit_name"]
    resource_class = OrgUnitResource


class VaccineTypeResource(resources.ModelResource):
    class Meta:
        model = VaccineType


@admin.register(VaccineType)
class VaccineTypeAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ["vaccine_type_name"]
    search_fields = ["vaccine_type_name"]
    resource_class = VaccineTypeResource


class BoosterInlineAdmin(admin.StackedInline):
    model = Booster
    extra = 1
    classes = ("collapse",)


class ConfirmedCovidCaseInlineAdmin(admin.StackedInline):
    model = ConfirmedCovidCase
    extra = 1
    classes = ("collapse",)


class SuspiciousCovidCaseInlineAdmin(admin.StackedInline):
    model = SuspiciousCovidCase
    extra = 1
    classes = ("collapse",)


class EmployeeResource(resources.ModelResource):
    full_name = Field(column_name="Nombre completo", attribute="full_name")
    dui = Field(column_name="DUI", attribute="dui")
    phone_number = Field(column_name="Teléfono", attribute="phone_number")
    birth_date = Field(column_name="Fecha nacimiento", attribute="birth_date")
    address = Field(column_name="Dirección", attribute="address")
    gender = Field(column_name="Género", attribute="gender")
    position = Field(column_name="Cargo", attribute="position")
    profession = Field(column_name="Profesión", attribute="profession")
    num_boosters = Field(column_name="Num. dosis")
    num_positive_cases = Field(column_name="Num. casos positivos")
    num_suspicious_cases = Field(column_name="Num. casos sospechosos")

    class Meta:
        model = Employee
        exclude = (
            "id",
            "author",
            "org_unit",
            "municipality",
        )

    def dehydrate_num_boosters(self, employee):
        return employee.booster_set.count()

    def dehydrate_num_positive_cases(self, employee):
        return employee.confirmedcovidcase_set.count()

    def dehydrate_num_suspicious_cases(self, employee):
        return employee.suspiciouscovidcase_set.count()


@admin.register(Employee)
class EmployeeAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = [
        "full_name",
        "dui",
        "get_num_boosters",
        "get_num_positive_cases",
        "get_num_suspicious_cases",
    ]
    search_fields = ["full_name", "dui"]
    autocomplete_fields = [
        "gender",
        "position",
        "profession",
        "org_unit",
        "municipality",
    ]
    inlines = [
        BoosterInlineAdmin,
        ConfirmedCovidCaseInlineAdmin,
        SuspiciousCovidCaseInlineAdmin,
    ]
    resource_class = EmployeeResource

    def get_num_boosters(self, obj):
        return obj.booster_set.count()

    get_num_boosters.short_description = "Num. dosis"

    def get_num_positive_cases(self, obj):
        return obj.confirmedcovidcase_set.count()

    get_num_positive_cases.short_description = "Num. casos +"

    def get_num_suspicious_cases(self, obj):
        return obj.suspiciouscovidcase_set.count()

    get_num_suspicious_cases.short_description = "Num. sospechosos"


admin.site.site_title = "Base de datos de empleados vacunados"
admin.site.site_header = "Base de datos de empleados vacunados"
admin.site.index_title = "REGISTRO DE EMPLEADOS VACUNADOS"
