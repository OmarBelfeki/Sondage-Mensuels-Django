from django.db import models


class Sondage(models.Model):
    NumS = models.AutoField(primary_key=True)
    Theme = models.CharField(max_length=50)
    DateDebut = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.NumS}"


class Question(models.Model):
    NumQ = models.IntegerField()
    NumS = models.ForeignKey(Sondage, on_delete=models.CASCADE)
    Content = models.CharField(max_length=150)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["NumQ", "NumS"],
                name="unique_mesure_pk"
            )
        ]

    def __str__(self):
        return f"{self.NumQ}"


class Participant(models.Model):

    class GenderChoices(models.TextChoices):
        M = "M", "Masculin"
        F = "F", "Feminin"

    IdParticipant = models.AutoField(primary_key=True)
    Mail = models.CharField(max_length=50)
    Mdp = models.CharField(max_length=6)
    Genre = models.CharField(max_length=1, choices=GenderChoices.choices)



    def __str__(self):
        return f"{self.IdParticipant}"


class Reponse(models.Model):

    class RepChoices(models.TextChoices):
        O = "O", "Oui"
        N = "N", "Non"
        S = "S", "Sans avis"

    NumQ = models.ForeignKey(Question, on_delete=models.CASCADE)
    NumS = models.ForeignKey(Sondage, on_delete=models.CASCADE)
    IdParticipant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    Rep = models.CharField(max_length=1, choices=RepChoices.choices)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["NumQ", "NumS", "IdParticipant"],
                name="unique_mesure_pk2"
            )
        ]