from datetime import datetime,date,timedelta
from decimal import Decimal
import math
def caculation_time_late(work,time,block):
    # fmt = "%H:%M:%S"
    now = datetime.now().time()
    level = 1

    if work == None:
        if now > time.morning_time_start and now < time.morning_time_end:
            level = (datetime.combine(date.today(),now) - datetime.combine(date.today(),time.morning_time_start)).total_seconds()
        elif now > time.morning_time_end and now < time.afternoon_time_start:
            level = (datetime.combine(date.today(),time.morning_time_end) - datetime.combine(date.today(),time.morning_time_start)).total_seconds()
        elif now > time.afternoon_time_start and now < time.afternoon_time_end:
            level = (datetime.combine(date.today(),now) - datetime.combine(date.today(),time.afternoon_time_start)).total_seconds() \
                    + (datetime.combine(date.today(),time.morning_time_end) - datetime.combine(date.today(),time.morning_time_start)).total_seconds()
    else:
        if work.state == 'morning':
            if now > time.morning_time_start and now < time.afternoon_time_start:
                return Decimal(0)
            if now > time.afternoon_time_start and now < time.afternoon_time_end:
                level = (datetime.combine(date.today(),now) - datetime.combine(date.today(),time.afternoon_time_start)).total_seconds()
    return 1 if block is None or block == 0 else Decimal(math.ceil(level / (60*block)))



def caculation_time_early(work,time,block):
    # fmt = "%H:%M:%S"
    now = datetime.now().time()
    level = 1
    if now > time.afternoon_time_end:
        return Decimal(0)

    if work == None:
        if now > time.morning_time_start and now < time.morning_time_end:
            level = (datetime.combine(date.today(),time.morning_time_end) - datetime.combine(date.today(),now)).total_seconds() \
            + (datetime.combine(date.today(),time.afternoon_time_end) - datetime.combine(date.today(),time.afternoon_time_start)).total_seconds()
        elif now > time.morning_time_end and now < time.afternoon_time_start:
            level = (datetime.combine(date.today(),time.afternoon_time_end) - datetime.combine(date.today(),time.afternoon_time_start)).total_seconds()
        elif now > time.afternoon_time_start and now < time.afternoon_time_end:
            level = (datetime.combine(date.today(),time.afternoon_time_end) - datetime.combine(date.today(),now)).total_seconds()
    else:
        if work.state == 'noon':
            return Decimal(0)
    return 1 if block is None or block == 0 else Decimal(math.ceil(level / (60*block)))


def method_payment(punish,method,exp,level,block,work,time,gen):
    if gen == 'late':
        pay = caculation_time_late(work,time,block)
    else:
        pay = caculation_time_early(work,time,block)
    if method == '*':
        return pay*punish*exp**level
    elif method == '+':
        return punish + exp*pay
    else:
        return 0


