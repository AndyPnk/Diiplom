from django.shortcuts import render

def Check_session(request):

    user = request.session.get('user', None)
    print(user)
    if user is not None:
        return True
    else:
        return render(request, 'LogIn.html')
    
def Add_user(request, h_log):
    request.session['user'] = h_log
    return True
