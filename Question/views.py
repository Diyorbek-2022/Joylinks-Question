from django.shortcuts import get_object_or_404
from environs import Env
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import User_Serializer, Certificate_Serializer

env = Env()
env.read_env()


@api_view(['POST'])
def Create_User(request):
    if request.method == 'POST':
        serializer = User_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"user_id": serializer.data['user_id']}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def score_calculation(test: dict):
    correct_answers = {
        "1": env.str("q1_"),
        "2": env.str("q2_"),
        "3": env.str("q3_"),
        "4": env.str("q4_"),
        "5": env.str("q5_"),
        "6": env.str("q6_"),
        "7": env.str("q7_"),
        "8": env.str("q8_"),
        "9": env.str("q9_"),
        "10": env.str("q10_")}
    count_true = int()
    count_false = int()
    for key, value in test.items():
        true_answer = correct_answers.get(key)
        if str(true_answer) == "":
            count_false += 1
            continue
        elif true_answer == str(value):
            count_true += 1
        else:
            count_false += 1
    return count_true, count_false


@api_view(['POST'])
def Finish_User(request):
    if request.method == 'POST':
        try:
            user = get_object_or_404(User, user_id=request.data['user_id'])
        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

        count_true, count_false = score_calculation(test=request.data['test'])

        if count_true < 6:
            return Response(
                data={"true_answer": count_true, "false_answer": count_false, "score": count_true * 10,
                      "status": False},
                status=status.HTTP_200_OK)
        serializer = Certificate_Serializer(user, data={"correct_answer": count_true, "wrong_answer": count_false,
                                                        "score": count_true * 10})

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"true_answer": count_true, "false_answer": count_false, "score": count_true * 10, "status": True},
                status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
