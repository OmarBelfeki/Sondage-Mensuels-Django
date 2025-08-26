from django.shortcuts import render
from .models import Sondage, Participant, Reponse, Question


def sondage(request):
    if request.method == "POST":
        mail = request.POST.get("mail")
        password = request.POST.get("password")
        gener = request.POST.get("gener")

        r1 = request.POST.get("r1")
        r2 = request.POST.get("r2")
        r3 = request.POST.get("r3")

        participant = Participant.objects.filter(Mail=mail, Mdp=password).first()

        question1 = Question.objects.filter(NumQ=1, NumS=1).first()
        question2 = Question.objects.filter(NumQ=2, NumS=1).first()
        question3 = Question.objects.filter(NumQ=3, NumS=1).first()

        questions_and_answers = [
            (question1, r1),
            (question2, r2),
            (question3, r3),
        ]

        if participant:
            for q, rep in questions_and_answers:
                if not q:
                    continue
                response = Reponse.objects.filter(
                    NumQ=q,
                    IdParticipant=participant
                ).first()
                if response:
                    response.Rep = rep
                    response.save()
                else:
                    Reponse.objects.create(
                        NumQ=q,
                        IdParticipant=participant,
                        Rep=rep
                    )
        else:
            participant = Participant.objects.create(
                Mail=mail,
                Mdp=password,
                Genre=gener
            )

            for q, rep in questions_and_answers:
                if q:
                    Reponse.objects.create(
                        NumQ=q,
                        IdParticipant=participant,
                        Rep=rep
                    )

        return render(request, "sondage.html")

    return render(request, "sondage.html")
