from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Colaborador(models.Model):
    id = models.BigAutoField(primary_key=True)
    apelido = models.CharField(unique=True, max_length=30)
    cargo = models.IntegerField(blank=True, null=True)
    ctps = models.CharField(unique=True, max_length=30)
    dtadmisao = models.DateTimeField(db_column='dtAdmisao')  # Field name made lowercase.
    imagem = models.TextField(blank=True, null=True)
    nome = models.CharField(unique=True, max_length=120)
    salario = models.DecimalField(max_digits=19, decimal_places=2)
    situacao = models.TextField()  # This field type is a guess.
    lojalocado = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='lojaLocado_id', blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'colaborador'


class ConfigSituacaoCadastro(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'config_situacao_cadastro'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empresa(models.Model):
    id = models.BigAutoField(primary_key=True)
    classificacaojuridica = models.IntegerField(db_column='classificacaoJuridica', blank=True,
                                                null=True)  # Field name made lowercase.
    situacaocadastro = models.ForeignKey(ConfigSituacaoCadastro, models.DO_NOTHING, db_column='situacaoCadastro_id',
                                         blank=True, null=True)  # Field name made lowercase.
    cnpj = models.CharField(max_length=14)
    ie = models.CharField(max_length=14, blank=True, null=True)
    razao = models.CharField(max_length=120)
    fantasia = models.CharField(max_length=80)
    cliente = models.TextField()  # This field type is a guess.
    fornecedor = models.TextField()  # This field type is a guess.
    transportadora = models.TextField()  # This field type is a guess.
    usuariocadastro = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuarioCadastro_id', blank=True,
                                        null=True, related_name='usuariocadastroempresa')  # Field name made lowercase.
    datacadastro = models.DateTimeField(db_column='dataCadastro')  # Field name made lowercase.
    usuarioatualizacao = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuarioAtualizacao_id', blank=True,
                                           null=True,
                                           related_name='usuarioatualizacaoempresa')  # Field name made lowercase.
    dataatualizacao = models.DateTimeField(db_column='dataAtualizacao', blank=True,
                                           null=True)  # Field name made lowercase.
    inscricaosuframa = models.CharField(db_column='inscricaoSuframa', max_length=9, blank=True,
                                        null=True)  # Field name made lowercase.
    inscricaomunicipal = models.CharField(db_column='inscricaoMunicipal', max_length=15, blank=True,
                                          null=True)  # Field name made lowercase.
    observacoes = models.CharField(max_length=1500, blank=True, null=True)
    limite = models.DecimalField(max_digits=19, decimal_places=2)
    prazopadrao = models.IntegerField(db_column='prazoPadrao')  # Field name made lowercase.
    diautilprazo = models.TextField(db_column='diaUtilPrazo')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'empresa'


class EmpresaEndereco(models.Model):
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_id')  # Field name made lowercase.
    enderecolist = models.OneToOneField('Endereco', models.DO_NOTHING,
                                        db_column='enderecoList_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa_endereco'


class Endereco(models.Model):
    id = models.BigAutoField(primary_key=True)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=8)
    complemento = models.CharField(max_length=80, blank=True, null=True)
    enderecotipo = models.IntegerField(db_column='enderecoTipo', blank=True, null=True)  # Field name made lowercase.
    logradouro = models.CharField(max_length=120)
    numero = models.CharField(max_length=10)
    referencia = models.CharField(max_length=80, blank=True, null=True)
    municipio = models.ForeignKey('Municipio', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'endereco'


class MenuPrincipal(models.Model):
    id = models.BigAutoField(primary_key=True)
    icomenu = models.CharField(db_column='icoMenu', max_length=120, blank=True, null=True)  # Field name made lowercase.
    menu = models.CharField(max_length=45)
    menulabel = models.CharField(db_column='menuLabel', max_length=45)  # Field name made lowercase.
    menupai_id = models.IntegerField(db_column='menuPai_id')  # Field name made lowercase.
    tabpane = models.TextField(db_column='tabPane')  # Field name made lowercase. This field type is a guess.
    teclaatalho = models.CharField(db_column='teclaAtalho', max_length=45, blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'menu_principal'


class Municipio(models.Model):
    id = models.BigAutoField(primary_key=True)
    capital = models.TextField()  # This field type is a guess.
    ddd = models.CharField(max_length=2)
    descricao = models.CharField(max_length=80)
    ibge_codigo = models.CharField(unique=True, max_length=7)
    uf = models.ForeignKey('Uf', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipio'


class Telefone(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=11)
    principal = models.TextField()  # This field type is a guess.
    operadora = models.ForeignKey('TelefoneOperadora', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'telefone'


class TelefoneOperadora(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=30)
    webservice_id = models.CharField(db_column='webService_id', max_length=5, blank=True,
                                     null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'telefone_operadora'


class Uf(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'uf'


class Usuario(models.Model):
    email = models.CharField(max_length=150)
    senha = models.CharField(max_length=128)
    id = models.OneToOneField(Colaborador, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = 'usuario'
