from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from clinica.models import (Diagnostico, DepartamentoMunicipio, ComunidadEtnia, Pais, Triage, Ocupacion,
                            EntidadSalud, PrestadoresSalud, TipoDocumentos, Discapacidades, CausaAtencion,
                            OpocisionDonacion, VoluntaAnticipada, Usuario, UsuarioPais,
                            Servicio, ViaIngresoServicio)


admin.site.site_header = "Administrador IPS"

admin.site.site_title = "Administrador IPS"

admin.site.index_title = "Panel de Administración"

# Register your models here.
class DiagnosticoResource(resources.ModelResource):
    class Meta:
        model = Diagnostico
        fields = ("codDiagnostico", "diagnostico", "padre")
        import_id_fields = ("codDiagnostico",)

class OcupacionResource(resources.ModelResource):
    class Meta:
        model = Ocupacion
        fields = ("codOcupacion", "desOcupacion", "padre")
        import_id_fields = ("codOcupacion",)

class PaisResource(resources.ModelResource):
    class Meta:
        model = Pais
        fields = ("idPais", "nomPais")
        import_id_fields = ("idPais",)

class DepartamentoMunicipioResource(resources.ModelResource):
    class Meta:
        model = DepartamentoMunicipio
        fields = ("codDepartamentoMunicipio", "DepartamentoMunicipio", "padre")
        import_id_fields = ["codDepartamentoMunicipio"]

class EntidadSaludResource(resources.ModelResource):
    class Meta:
        model = EntidadSalud
        fields = ("codEntidad", "nomEntidad")
        import_id_fields = ("codEntidad",)

class PrestadoresSaludResource(resources.ModelResource):
    class Meta:
        model = PrestadoresSalud
        fields = ("codPrestadorSalud", "prestadoresSalud")
        import_id_fields = ("codPrestadorSalud",)


class PaisAdmin(ImportExportModelAdmin):
    resource_class = PaisResource
    list_display = ["idPais", "nomPais"]
    search_fields = ["nomPais"]

class OcupacionAdmin(ImportExportModelAdmin):
    list_display = ["codOcupacion", "desOcupacion", "padre"]
    resource_class = OcupacionResource
    search_fields = ["codOcupacion", "desOcupacion"]
    list_filter = ["desOcupacion", "padre", "codOcupacion"]

class DiagnosticoAdmin(ImportExportModelAdmin):
    list_display = ["codDiagnostico", "diagnostico", "padre"]
    resource_class = DiagnosticoResource
    search_fields = ["codDiagnostico", "diagnostico", "padre"]

class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ["idTipoDocumento", "descripcionDocumento"]

class DiscapacidadAdmin(admin.ModelAdmin):
    list_display = ["codDiscapacidad", "calDiscapacidad"]

class DepartamentoMunicipioAdmin(ImportExportModelAdmin):
    resource_class = DepartamentoMunicipioResource
    list_display = ["codDepartamentoMunicipio", "DepartamentoMunicipio", "padre"]

class ComunidadEtniaAdmin(admin.ModelAdmin):
    list_display = ["codComunidadEtnia","desComunidad"]

class EntidadSaludAdmin(ImportExportModelAdmin):
    resource_class = EntidadSaludResource
    list_display = ["codEntidad", "nomEntidad"]
    search_fields = ["nomEntidad"]

class PrestadorSaludAdmin(ImportExportModelAdmin):
    resource_class = PrestadoresSaludResource
    list_display = ["codPrestadorSalud", "prestadoresSalud"]
    search_fields = ["codPrestadorSalud", "prestadoresSalud"]

class OposicionAdmin(admin.ModelAdmin):
    list_display = ["idDonacion", "manifestacionOpo", "fechaDonacion","get_usuario"]

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["primer_nombre", "segundo_nombre", "primer_apellido", "segundo_apellido", "tipo_documento", "numero_documento",
                    "mostrarDiscapacidad", "fecha_nacimiento", "entidad", "mostrarNacionalidad"]
    search_fields = ["entidad__nomEntidad", "primer_nombre", "segundo_nombre", "primer_apellido", "segundo_apellido",
                     "nacionalidad__nomPais"]

    def mostrarNacionalidad(self, obj):
        return ",".join([pais.nomPais for pais in obj.nacionalidad.all()])

    def mostrarDiscapacidad(self, obj):
        return ",".join([discapacidades.calDiscapacidad for discapacidades in obj.discapacidad.all()])

    mostrarDiscapacidad.short_description = "Discapacidades"
    mostrarNacionalidad.short_description = "Nacionalidad"

class ViaIngresoAdmin(admin.ModelAdmin):
    list_display = ["idViaIngresoServicio", "desIngresoServicio"]

class CausaAtencionAdmin(admin.ModelAdmin):
    list_display = ["codCausaAtencion", "causaAtencion"]

class ServicioAdmin(admin.ModelAdmin):
    list_display = ["prestador_salud","usuario","fecha_atencion","hora_atencion","modalidad_servicio","grupo_servicio","diagnostico","entorno_atencion","triage","causa_atencion"]

class VoluntadAdmin(admin.ModelAdmin):
    list_display = ["idVoluntad", "docVoluntad", "fecha", "codPrestadorSalud", "get_usuario"]

class TriageAdmin(admin.ModelAdmin):
    list_display = ["idTriage","fechaTriage","horaTriage","ClasificacionTriage","get_servicio"]


admin.site.register(Diagnostico, DiagnosticoAdmin)
admin.site.register(DepartamentoMunicipio, DepartamentoMunicipioAdmin)
admin.site.register(ComunidadEtnia, ComunidadEtniaAdmin)
admin.site.register(Pais, PaisAdmin)
admin.site.register(Triage, TriageAdmin)
admin.site.register(Ocupacion, OcupacionAdmin)
admin.site.register(EntidadSalud, EntidadSaludAdmin)
admin.site.register(PrestadoresSalud, PrestadorSaludAdmin)
admin.site.register(TipoDocumentos, TipoDocumentoAdmin)
admin.site.register(Discapacidades, DiscapacidadAdmin)
admin.site.register(CausaAtencion, CausaAtencionAdmin)
admin.site.register(OpocisionDonacion, OposicionAdmin)
admin.site.register(VoluntaAnticipada, VoluntadAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(ViaIngresoServicio, ViaIngresoAdmin)

