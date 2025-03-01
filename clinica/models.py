from django.db import models


class OpocisionDonacion(models.Model):
    idDonacion = models.AutoField(primary_key=True)
    Choise_manifestacion = {
        '01': 'Si',
        '02': 'No',
    }
    manifestacionOpo = models.CharField(max_length=2, choices=Choise_manifestacion)
    fechaDonacion = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'opocisionDonacion'
        verbose_name = 'Oposición Donación'
        verbose_name_plural = 'Oposicion Donaciones'

    def __str__(self):
        return f"{self.idDonacion}, {self.manifestacionOpo} ,{str(self.fechaDonacion),}"

    def get_usuario(self):
        return Usuario.objects.filter(donacion=self).first()

    get_usuario.short_description = 'Usuario'


class ComunidadEtnia(models.Model):
    codComunidadEtnia = models.IntegerField(primary_key=True)
    desComunidad = models.CharField(max_length=50)

    class Meta:
        db_table = 'comunidadEtnia'
        verbose_name = 'Comunidad Etnia'
        verbose_name_plural = 'Comunidades Etnicas'

    def __str__(self):
        return f"{self.desComunidad}"

class Pais(models.Model):
    idPais = models.IntegerField(primary_key=True)
    nomPais = models.CharField(max_length=200)

    class Meta:
        db_table = 'pais'
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.nomPais.__str__()

class Discapacidades (models.Model):
    codDiscapacidad =models.IntegerField(primary_key=True)
    calDiscapacidad = models.CharField(max_length=50)

    class Meta:
        db_table = 'discapacidades'
        verbose_name = 'Discapacidad'
        verbose_name_plural = 'Discapacidades'

    def __str__(self):
        return f"{self.codDiscapacidad}  {self.calDiscapacidad}"

class EntidadSalud(models.Model):
    codEntidad =models.CharField(primary_key=True, max_length=6)
    nomEntidad =models.CharField(max_length=200)

    class Meta:
        db_table = 'entidadSalud'
        verbose_name = 'Entidad Salud'
        verbose_name_plural = 'Entidades de Salud'

    def __str__(self):
        return f"{self.nomEntidad}"


class Ocupacion(models.Model):
    codOcupacion = models.CharField(max_length=4, primary_key=True)
    desOcupacion = models.CharField(max_length=200)
    padre = models.IntegerField(null=True)

    class Meta:
        db_table = 'ocupacion'
        verbose_name = 'Ocupacion'
        verbose_name_plural = 'Ocupaciones'

    def __str__(self):
        return f"{self.codOcupacion} {self.desOcupacion}"

class PrestadoresSalud(models.Model):
    codPrestadorSalud = models.CharField(max_length=12, primary_key=True)
    prestadoresSalud = models.CharField(max_length=12)

    class Meta:
        db_table = 'prestadoresSalud'
        verbose_name = 'Prestador Salud'
        verbose_name_plural = 'Prestadores de Salud'

    def __str__(self):
        return f"{self.prestadoresSalud}"



class VoluntaAnticipada(models.Model):
    VOLUNTAD = [
        ('01', 'Si'),
        ('02', 'No')
    ]
    idVoluntad = models.AutoField(primary_key=True)
    docVoluntad = models.CharField(max_length=200, choices=VOLUNTAD)
    fecha = models.DateField(max_length=10, null=True, blank=True)
    codPrestadorSalud =models.ForeignKey(PrestadoresSalud,max_length=12, on_delete=models.RESTRICT, null=True)

    class Meta:
        db_table = 'voluntaAnticipada'
        verbose_name = 'Voluntad Anticipada'
        verbose_name_plural = 'Voluntades Anticipadas'

    def __str__(self):
        return f"{self.idVoluntad}, {self.docVoluntad} {self.fecha} {self.codPrestadorSalud}"

    def get_usuario(self):
        return Usuario.objects.filter(voluntad=self).first()

class Triage(models.Model):
    TRIAGE = [
        ('01', 'TRIAGE I'),
        ('02', 'TRIAGE II'),
        ('03', 'TRIAGE III'),
        ('04', 'TRIAGE IV'),
        ('05', 'TRIAGE V'),
    ]
    idTriage = models.AutoField(primary_key=True)
    fechaTriage = models.DateField()
    horaTriage = models.TimeField()
    ClasificacionTriage = models.CharField('Clasificacion de triage',max_length=2, choices= TRIAGE )

    class Meta:
        db_table = 'triage'
        verbose_name = 'Triage'
        verbose_name_plural = 'Triages'

    def __str__(self):
        return f"{self.fechaTriage}/{self.horaTriage} - {self.get_ClasificacionTriage_display()}"

    def get_servicio(self):
        return Servicio.objects.filter(triage=self).first()


class Diagnostico(models.Model):
    codDiagnostico = models.CharField(primary_key=True, max_length=4)
    diagnostico = models.CharField(max_length=200)
    padre = models.CharField(max_length=3)

    class Meta:
        db_table = 'diagnostico'
        verbose_name = 'Diagnostico'
        verbose_name_plural = 'Diagnosticos'

    def __str__(self):
        return f"{self.codDiagnostico}-{self.diagnostico}"


class CausaAtencion(models.Model):
    codCausaAtencion = models.IntegerField(primary_key=True)
    causaAtencion = models.CharField(max_length=200)

    class Meta:
        db_table = 'causaAtencion'
        verbose_name = 'Causa Atencion'
        verbose_name_plural = 'Causas de Atención'

    def __str__(self):
        return f"{self.codCausaAtencion}-{self.causaAtencion}"

class TipoDocumentos(models.Model):
    idTipoDocumento = models.CharField(primary_key=True, max_length=2)
    descripcionDocumento = models.CharField(max_length=100)

    class Meta:
        db_table = 'tipoDocumento'
        verbose_name = 'Tipo Documento'
        verbose_name_plural = 'Tipos de Documento'

    def __str__(self):
        return f"{self.descripcionDocumento}"

class DepartamentoMunicipio(models.Model):
    codDepartamentoMunicipio = models.CharField(primary_key=True, max_length=6)
    DepartamentoMunicipio = models.CharField(max_length=100)
    padre = models.CharField(max_length=100)

    class Meta:
        db_table = 'departamentoMunicipio'
        verbose_name = 'Departamento Municipio'
        verbose_name_plural = 'Departamentos Municipios'

    def __str__(self):
        return f"{self.padre} - {self.DepartamentoMunicipio}"

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    tipo_documento = models.ForeignKey(TipoDocumentos, on_delete=models.RESTRICT)
    numero_documento = models.IntegerField()
    primer_nombre = models.CharField(max_length=60)
    segundo_nombre = models.CharField(max_length=60, null=True, blank=True)
    primer_apellido = models.CharField(max_length=60)
    segundo_apellido = models.CharField(max_length=60, null=True, blank=True)
    fecha_nacimiento = models.DateField()
    hora_nacimiento = models.TimeField()
    Choise_Sexo = {
        "01": "Hombre",
        "02": "Mujer",
        "03": "Indeterminado/Intersexsual",
    }
    sexo_biologico = models.CharField(max_length=2, choices=Choise_Sexo)
    Choise_Identidad = {
        "01": "Masculino",
        "02": "Feminino",
        "03": "Transgenero",
        "04": "Neutro",
        "05": "No lo declara"
    }
    ident_genero = models.CharField(max_length=2, choices=Choise_Identidad)
    ocupacion = models.ForeignKey(Ocupacion, on_delete=models.RESTRICT)
    discapacidad = models.ManyToManyField(Discapacidades,related_name='discapacidad_usuario', blank=True)
    donacion = models.ForeignKey(OpocisionDonacion, on_delete=models.RESTRICT)
    voluntad = models.ForeignKey(VoluntaAnticipada, on_delete=models.RESTRICT)
    nacionalidad = models.ManyToManyField(Pais, related_name='nacionalidad_usuario', blank=True)
    pais_residencia = models.ForeignKey(Pais, related_name='pais_usuario', on_delete=models.RESTRICT, null=True)
    departamento_municipio = models.ForeignKey(DepartamentoMunicipio, on_delete=models.RESTRICT)
    comunidad_etnia = models.ForeignKey(ComunidadEtnia, on_delete=models.RESTRICT)
    Choise_Etnia = {
        "01": "Indigena",
        "02": "ROM (Gitanos)",
        "03": "Raizal (San Andrés y Providencia)",
        "04": "Palenquero de San Basillo de Palenque",
        "05": "Negro(a)",
        "06": "Afrocolombiano(a)",
        "99": "Ninguna de las anteriores"
    }
    etnia = models.CharField(max_length=2, choices=Choise_Etnia)
    Choise_Zona = {
        "01": "Urbana",
        "02": "Rural",
    }
    zona_residencia = models.CharField(max_length=2, choices=Choise_Zona)
    entidad = models.ForeignKey(EntidadSalud, on_delete=models.RESTRICT)

    class Meta:
        db_table = 'usuario'
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return (f"{self.primer_nombre} {self.segundo_nombre} {self.primer_apellido} "
                f"{self.segundo_apellido} {self.numero_documento}")

class UsuarioPais(models.Model):
    idUsuarioPais = models.AutoField(primary_key=True)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT)
    idPais = models.ForeignKey(Pais, on_delete=models.RESTRICT)

    class Meta:
        db_table = 'usuario_pais'
        verbose_name = 'Usuario Pais'
        verbose_name_plural = 'Usuarios Pais'

    def __str__(self):
        return f"{self.idUsuario}, {self.idPais}"


class ViaIngresoServicio(models.Model):
    idViaIngresoServicio = models.IntegerField(primary_key=True)
    desIngresoServicio = models.CharField(max_length=99)

    class Meta:
        db_table = 'via_ingreso_servicio'
        verbose_name = 'Via Ingreso Servicio'
        verbose_name_plural = 'Vias Ingresos de Servicio'

    def __str__(self):
        return f"{self.desIngresoServicio}"

class Servicio(models.Model):
    idServicioSalud = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT)
    prestador_salud = models.ForeignKey(PrestadoresSalud, on_delete=models.RESTRICT)
    fecha_atencion = models.DateField()
    hora_atencion = models.TimeField()
    Choise_Modalidad = {
        "01": "Intramural",
        "02": "Extramural unidad móvil",
        "03": "Extramural domiciliaria",
        "04": "Extramural jornada de salud",
        "05": "Extramural (atención pre hospitalaria o transporte asistencial)",
        "06": "Telemedicina interactiva",
        "07": "Telemedicina no interactiva",
        "08": "Telemedicina - Telexperticia",
        "09": "Telemedicina - Telemonitoreo",
    }
    modalidad_servicio = models.CharField(max_length=2, choices=Choise_Modalidad)
    Choise_Grupo = {
        "01": "Consulta Externa",
        "02": "Apoyo diagnóstico y complementación terapéutica",
        "03": "Internación",
        "04": "Quirúrgico",
        "05": "Atención Inmediata",
    }
    grupo_servicio = models.CharField(max_length=2, choices=Choise_Grupo)
    via_ingreso = models.ForeignKey(ViaIngresoServicio, on_delete=models.RESTRICT)
    Choise_Entorno = {
        "01": "Hogar",
        "02": "Comunitario",
        "03": "Escolar",
        "04": "Laboral",
        "05": "Institucional",
    }
    entorno_atencion = models.CharField(max_length=2, choices=Choise_Entorno)
    causa_atencion = models.ForeignKey(CausaAtencion, on_delete=models.RESTRICT)
    triage = models.ForeignKey(Triage, on_delete=models.RESTRICT)
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.RESTRICT)
    Choise_t_diagnostico = {
        "01": "Impresión diagnóstica",
        "02": "Confirmado nuevo",
        "03": "Confirmado repetido",
    }
    t_diagnostico = models.CharField(max_length=2, choices=Choise_t_diagnostico)

    class Meta:
        db_table = 'servicio'
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios de Salud'

    def __str__(self):
        return f"{self.idServicioSalud} - {self.usuario}"
