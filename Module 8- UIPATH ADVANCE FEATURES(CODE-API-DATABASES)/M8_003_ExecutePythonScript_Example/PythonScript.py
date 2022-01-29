def Welcome(user,country):
    if user is '':
	    user = 'stranger'
    print ('Hello{0}, how is {1} ', user,country)
    return 'Hello '+user+', how is '+country+"?"
