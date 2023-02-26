from django.shortcuts import render
import pickle

def index(request):
    return render(request, 'index.html')


def recursos(request):
    return render(request, 'recursos.html')


def beneficios(request):
    return render(request, 'beneficios.html')


def about(request):
    return render(request, 'about.html')



def test(request):


    # open the file  / load the model
    vectorizer = pickle.load(open("C:arquivos/pickle/vectorizer_robot.pkl", "rb"))
    model_robot = pickle.load(open("C:arquivos/pickle/model_robot.pkl", "rb"))


    if request.method == 'POST':
        user_input = request.POST.get('input')

        prediction = model_robot.predict(vectorizer.transform([user_input, 'i will not use this']))

        context = {
            'prediction': prediction[0],
            'user_input': user_input
        }

        return render(request, 'results.html', context)
    else:
        return render(request, 'try.html')




