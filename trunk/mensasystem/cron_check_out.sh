#!/bin/sh

source ~/mensasystem/bin/activate
cd /home/azureuser/mensasystem/trunk/mensasystem/
python manage.py cron cron_user_check_out
