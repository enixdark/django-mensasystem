#! /usr/bash
file_manage=`pwd`/manage.py
if [ ! -f $file_manage ];
then
	/usr/bin/crontab -l > mycron
	basedir=`cat mycron | awk 'END{print $7}'`
	file_manage=`dirname $basedir`
	rm -rf mycron
fi
source ~/mensasystem/bin/activate
# echo $file_manage/manage.py
python $file_manage/manage.py cron cron_user
