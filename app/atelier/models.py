from django.db import models
from django.utils.html import format_html
from local_user.models import LocalUser


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

class Atelier(models.Model):
    
    publier = models.BooleanField(default=False)
    
    titre = models.CharField(max_length=200, help_text="titre de l'atelier")

    theme = models.ForeignKey(Theme, on_delete=models.PROTECT,
                              help_text="""theme de l'atelier 
                                (ex: Modélisation, Programmation...)""")

    image = models.ImageField(
        upload_to='static/img/atelier/principale',
        null=True, help_text="image principale de l'atelier")

    miniature = models.ImageField(
        upload_to='static/img/atelier/miniatures',
        null=True, help_text="image de la liste d'atelier")

    objectif = models.TextField(help_text="description global de l'atelier")

    publique = models.ForeignKey(
        Publique, on_delete=models.PROTECT,
        help_text="type de publics pouvant être intéressé")

    niveau = models.ForeignKey(
        Niveau, on_delete=models.PROTECT,
        help_text="Niveau de difficulté de l'atelier")

    point_abordes = models.TextField(
        help_text="""liste des points importants de l'atelier
                    (retour a la ligne pour les '-')""")

    nb_seance_distance = models.IntegerField(
        default=0, help_text="""nombre de séance pouvant être faite a distance
            (uniquement informatique)
            les séance a distance peuvent
            être quand même fait en présentiel""")

    nb_seance_physique = models.IntegerField(
        default=0,
        help_text="""nombre de séance qui ne peuvent que être faite sur place
        (besoins d'une machine sur place)""")

    annimateur_possible = models.ManyToManyField(
        LocalUser,
        help_text="liste des personnes capable de faire le cour")
    
    minimum_inscrit = models.IntegerField(default=0,
        help_text="nombre de personnes minimum");

    def points_list(self):
        return self.point_abordes.split('\n')

    def path_img(self):
        return "static/img/atelier/" + self.titre

    def __str__(self):
        return self.titre

    def admin_photo(self):
        return format_html('<img src="{}" width="100" height="100" />'
                           .format(self.miniature.url))

    admin_photo.short_description = 'Miniature'

    admin_photo.allow_tags = True


class Session(models.Model):
    date = models.DateField(help_text="date de la séance")
    
    def __str__(self):
        return self.date.strftime("%d/%m/%Y")
    
    
class Seance(models.Model):
    titre = models.CharField(max_length=200, default="",)
    atelier = models.ForeignKey(Atelier,
                                on_delete=models.PROTECT,
                                default=None,
                                null=True,
                                blank=True)
    
    personne_incrit = models.ManyToManyField(LocalUser,
                                             blank=True)
    
    dates = models.ManyToManyField(Session,blank=True,
                                 default=None,
                                 help_text="date des séances")

    def liste_des_dates(self):
        return ", ".join([str(x) for x in self.dates.all()])
