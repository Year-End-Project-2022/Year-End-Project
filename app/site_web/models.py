from django.db import models


class ImageGalerie(models.Model):

    titre = models.CharField(max_length=200)

    alt = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to='static/img/galerie')

    def __str__(self):
        return self.titre


class Theme(models.Model):
    titre = models.CharField(max_length=200)

    def __str__(self):
        return self.titre


class Publique(models.Model):
    titre = models.CharField(max_length=200)

    def __str__(self):
        return self.titre


class Niveau(models.Model):
    titre = models.CharField(max_length=200)

    def __str__(self):
        return self.titre


class PersonneDispo(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
        return self.nom


class Atelier(models.Model):

    titre = models.CharField(max_length=200, help_text="titre de l'atelier")

    theme = models.ForeignKey(Theme, on_delete=models.PROTECT,
                              help_text="theme de l'atelier (ex: Modélisation, Programmation...)")

    image = models.ImageField(
        upload_to='static/img/atelier/' + str(titre),
        null=True, help_text="image principale de l'atelier")

    miniature = models.ImageField(
        upload_to='static/img/atelier/' + str(titre),
        null=True, help_text="image de la liste d'atelier")

    objectif = models.TextField(help_text="description global de l'atelier")

    publique = models.ForeignKey(
        Publique, on_delete=models.PROTECT, help_text="type de publics pouvant être intéressé")

    niveau = models.ForeignKey(
        Niveau, on_delete=models.PROTECT, help_text="Niveau de difficulté de l'atelier")

    point_abordes = models.TextField(
        help_text="liste des points importants de l'atelier (retour a la ligne pour les '-')")

    nb_seance_distance = models.IntegerField(
        default=0, help_text="""nombre de séance pouvant être faite a distance
            (uniquement inforamtique)
            les séance a distance peuvent être quand même fait en présentiel""")

    nb_seance_physique = models.IntegerField(
        default=0,
        help_text="""nombre de séance qui ne peuvent que être faite sur place
        (besoins d'une machine sur place)""")

    annimateur_possible = models.ManyToManyField(
        PersonneDispo, help_text="liste des personnes capable de faire le cour   ")

    def __str__(self):
        return self.titre

    def points_list(self):
        return self.point_abordes.split('\n')
