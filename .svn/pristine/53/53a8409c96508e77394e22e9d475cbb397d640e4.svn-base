#! /bin/bash 
if [ ! -d ~/mensasystem ]; then
	/usr/bin/virtualenv ~/mensasystem
fi
source ~/mensasystem/bin/activate
# pip install -U django django-contact-form requests django-cronjobs django_countries python-dateutil netifaces
pip install -r requirements.txt
/usr/bin/crontab -l > mycron

cron_text=`pwd`/cron.sh

if ! grep -q $cron_text mycron;
then 
	echo "0 18 * * 1,2,3,4,5 /bin/bash $cron_text" >> mycron
fi

/usr/bin/crontab mycron
if [ ! -f "db.sqlite3" ]; then
	touch db.sqlite3
fi

python manage.py makemigrations
python manage.py migrate
python manage.py runserver


