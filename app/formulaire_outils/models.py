from django.db import models


class Categories(models.Model):

    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class Media(models.Model):

    image = models.ImageField(upload_to='static/img/outils', unique=True)

    def __str__(self):
        return self.image.name


class Groupe(models.Model):

    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom


class Outils(models.Model):

    nom = models.CharField(max_length=200, blank=True, null=True, default="")

    type = models.CharField(max_length=200)

    taille = models.CharField(max_length=50, blank=True, null=True, default='')

    marque = models.CharField(
        max_length=200, blank=True, null=True, default='')

    categories = models.ManyToManyField(Categories)

    image = models.ForeignKey(
        Media, on_delete=models.PROTECT, related_name="imageBase")

    image_cote = models.ForeignKey(
        Media, on_delete=models.PROTECT, related_name="imageCote", null=True, blank=True)

    nombre = models.IntegerField(blank=True, default=1)

    nombre_hs = models.IntegerField(blank=True, default=0)

    groupe = models.ForeignKey(
        Groupe, blank=True, null=True, on_delete=models.PROTECT)

    commentaire = models.TextField(blank=True, null=True)

    def nom_func(self):
        temps_nom = ""
        if self.nom:
            temps_nom = self.nom
        else:
            temps_nom = "{} {} {}".format(self.type, self.marque, self.taille)
        return temps_nom

    def __str__(self):
        return self.nom_func()
