from django.db import models


# Create your models here.
class Tipus(models.Model):
    desc_tipus = models.CharField(max_length=300)


class Tematica(models.Model):
    desc_tematica = models.CharField(max_length=500)


class Pais(models.Model):
    nom_pais = models.CharField(max_length=75)
    desc_pais = models.CharField(max_length=200)


class Carrer(models.Model):
    pais = models.ForeignKey(Pais)
    nom_carrer = models.CharField(max_length=150)
    num = models.TextField()
    desc_carrer = models.CharField(max_length=300)


class Ubicacio(models.Model):
    carrer = models.ForeignKey(Carrer)
    nom_ubicacio = models.CharField(max_length=100)
    desc_ubicacio = models.CharField(max_length=300)
    aforament_max = models.IntegerField()


class Persona(models.Model):
    doc_identificatiu = models.CharField(max_length=10)
    nom = models.CharField(max_length=30)
    cognom1 = models.CharField(max_length=50)
    cognom2 = models.CharField(max_length=50)
    telf = models.CharField(max_length=14)
    email = models.EmailField()


class Administrador(models.Model):
    persona = models.ForeignKey(Persona)
    password = models.CharField(max_length=30)
    rol = models.CharField(max_length=30)


class Gestor(models.Model):
    persona = models.ForeignKey(Persona)
    password = models.CharField(max_length=30)
    rol = models.CharField(max_length=30)
    data_inici_contracte = models.DateField()
    data_fi_contracte = models.DateField()


class Event(models.Model):
    nom = models.CharField(max_length=75)
    descripcio = models.CharField(max_length=300)
    aforament = models.IntegerField()
    gestor = models.ForeignKey(Gestor)
    tipus = models.ForeignKey(Tipus)
    tematica = models.ForeignKey(Tematica)
    pais = models.ForeignKey(Pais)
    carrer = models.ForeignKey(Carrer)
    ubicacio = models.ForeignKey(Ubicacio)
    data_inici = models.DateField()
    data_fi = models.DateField()
    publicat = models.BooleanField(default=False)


class Usuari(models.Model):
    persona = models.ForeignKey(Persona)
    password = models.CharField(max_length=30)
    rol = models.CharField(max_length=30)
    actiu = models.BooleanField(default=False)
    ponencia = models.ManyToManyField(Event)


class Ponent(models.Model):
    persona = models.ForeignKey(Persona)
    password = models.CharField(max_length=30)
    rol = models.CharField(max_length=30)
    salari = models.FloatField(default=0)
    ponencia = models.ManyToManyField(Event)


class Informacio(models.Model):
    event = models.ForeignKey(Event)
    titol_informacio = models.CharField(max_length=75)
    desc_informacio = models.CharField(max_length=300)


class Forum(models.Model):
    ''' Clase que representa un foro donde se intercanviaran los usuarios
    mensajes
    '''
    event = models.ForeignKey(Event)
    nom_forum = models.CharField(max_length=75)
    desc_forum = models.CharField(max_length=300)


class Missatge(models.Model):
    forum = models.ForeignKey(Forum)
    titol_missatge = models.CharField(max_length=75)
    desc_missatge = models.CharField(max_length=300)
    usuari = models.ForeignKey(Usuari)
    pare = models.ForeignKey('self', related_name='missatge_pare')
    fill = models.ForeignKey('self', related_name='missatge_fill')
