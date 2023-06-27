from django.shortcuts import render
from .utils import helper_functions
from django.contrib import messages
import random
import string

# # Create your views here.
def team_generator(request):
    if request.method == 'POST':
        names = request.POST.get('names').split(',')  # Get names from POST request
        names = [i.strip() for i in names if i.strip() != '']  # Remove leading/trailing whitespace and empty items
        request.session['names'] = names
        num_teams = int(request.POST.get('num_teams'))  # Get number of teams from POST request
        num_names = len(names)  # Get length of names list

        invalid_chars = ['.', ' ', '/', '\n', ';', ':']
        if any(any(char in name for char in invalid_chars) for name in names):
            error_message = 'Please enter valid names separated by commas (",")'
            messages.error(request, error_message)
            return render(request, 'team_app/form.html')

        teams = helper_functions.create_teams(num_teams=num_teams, num_names=num_names, names=names)  # Team creation

        # Saving data in session variables for future rerolls
        request.session['num_teams'] = num_teams
        request.session['num_names'] = num_names

        return render(request, 'team_app/result.html', {'teams': teams})

    return render(request, 'team_app/form.html')

def reroll(request): # Reroll teams with previously given names
    if request.method == 'GET':

        names = request.session.get('names')
        num_teams = request.session.get('num_teams')
        num_names = request.session.get('num_names')\

        teams = helper_functions.create_teams(num_teams=num_teams, num_names=num_names, names=names)

        return render(request, 'team_app/result.html', {'teams':teams})


def cointoss(request):
    if request.method == 'POST':
        num_tosses = request.POST.get('num_tosses')
        if num_tosses:
            try:
                num_tosses = int(num_tosses)
                if num_tosses > 0:
                    results = []
                    heads_count = 0
                    tails_count = 0

                    for _ in range(num_tosses):
                        toss_result = random.choice(['Heads', 'Tails'])
                        results.append(toss_result)
                        if toss_result == 'Heads':
                            heads_count += 1
                        else:
                            tails_count += 1
                    return render(request, 'team_app/cointoss.html',
                                  {'results': results, 'heads_count': heads_count, 'tails_count': tails_count})
                else:
                    error_message = 'Number of tosses must be greater than 0.'
            except ValueError:
                error_message = 'Invalid input. Please enter a valid number of tosses.'
        else:
            error_message = 'Please enter the number of tosses.'
    else:
        error_message = None
    return render(request, 'team_app/cointoss.html', {'error_message': error_message})


def random_pass(request):
    if request.method == 'POST':
        password_length = int(request.POST.get('password_length'))

        # Validate password length
        if password_length < 8 or password_length > 12:
            error_message = 'Please enter a password length between 8 and 12 characters.'
            return render(request, 'team_app/random_pass.html', {'error_message': error_message})

        password = generate_random_password(password_length)

        return render(request, 'team_app/random_pass.html', {'password': password})

    return render(request, 'team_app/random_pass.html')


def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password