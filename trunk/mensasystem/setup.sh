#! /bin/bash 
if [ ! -d ~/mensasystem ]; then
	if [ -f /usr/bin/virtualenv ];
	then
	    /usr/bin/virtualenv ~/mensasystem
	else
	    /usr/local/bin/virtualenv ~/mensasystem
	fi
fi

. ~/mensasystem/bin/activate

# pip install -U django django-contact-form requests django-cronjobs django_countries python-dateutil netifaces
pip install -r requirements.txt
/usr/bin/crontab -l > mycron

cron_text=`pwd`/cron.sh
cron_check_out_text=`pwd`/cron_check_out.sh

if ! grep -q $cron_text mycron;
then
	echo "0 18 * * 1,2,3,4,5 /bin/bash $cron_text" >> mycron
fi

if ! grep -q $cron_check_out_text mycron;
then
	echo "30 18 * * 1,2,3,4,5 /bin/bash $cron_check_out_text" >> mycron
fi

/usr/bin/crontab mycron
if [ ! -f "db.sqlite3" ]; then
	touch db.sqlite3
fi

python manage.py makemigrations
python manage.py migrate
python manage.py runserver


