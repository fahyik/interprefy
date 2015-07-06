import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'interprefy.settings')

import django
django.setup()

from tbox.models import TokBox


def init_tokbox_acct():

	api_key = "45268672"
	api_secret = "7b6716858e83a131e479edf6b5b0ddf5b924a340"
	create = TokBox.objects.get_or_create(api_key=api_key, api_secret=api_secret)[0]
	create.save()
	print api_key
	print api_secret
	print "Done!"

# Start execution here!
if __name__ == '__main__':
    print "creating tokbox account details..."
    init_tokbox_acct()