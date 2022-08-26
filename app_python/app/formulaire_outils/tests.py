from formulaire_outils.models import Categories, Groupe, Media, Outils
import os
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.


class FormulaireOutilsTest(TestCase):
    def setUp(self):
        cat = Categories.objects.create(title="Atelier")
        cat2 = Categories.objects.create(title="Impression 3D")
        grp = Groupe.objects.create(nom="Cle Plate")
        image = SimpleUploadedFile(
            name='test_image.jpg',
            content=open(
                './app_python/Imgtest.jpeg', 'rb').read(), content_type='image/jpeg')

        med = Media.objects.create(image=image)

        outil1 = Outils.objects.create(
            type="clé plate",
            taille="12",
            marque="facom",
            image=med,
            image_cote=med,
            nombre=4,
            nombre_hs=0,
            groupe=grp,
            commentaire="ceci est un petit commentaire de test"
        )
        outil2 = Outils.objects.create(
            nom="custom Nom",
            type="clé plate",
            taille="8",
            marque="facom",
            image=med,
            image_cote=med,
            nombre=4,
            nombre_hs=0,
            groupe=grp,
            commentaire="ceci est un petit commentaire de test"
        )
        outil1.categories.set([cat, cat2])

    def tearDown(self):
        os.remove("static/img/outils/test_image.jpg")

    def test_categorie_existe(self):
        categories = Categories.objects.get(pk=1)
        self.assertEqual("Atelier", str(categories))

    def test_group_existe(self):
        grp = Groupe.objects.get(pk=1)
        self.assertEqual("Cle Plate", str(grp))

    def test_media_existe(self):
        med = Media.objects.get(pk=1)
        self.assertEqual("static/img/outils/test_image.jpg", str(med))

    def test_outils_existe(self):
        outil = Outils.objects.get(pk=1)
        self.assertEqual("clé plate facom 12", str(outil))

    def test_outil_custom_name(self):
        outil = Outils.objects.get(pk=2)
        self.assertEqual("custom Nom", str(outil))
    def test(self):
        self.assertEqual(1, 1)
