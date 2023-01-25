from extensions import jalali
from django.utils import timezone
from datetime import date, timedelta


def persian_numbers_converter(mystr):
    
    numbers = {
        "0": "۰",
        "1": "۱",
        "2": "۲",
        "3": "۳",
        "4": "۴",
        "5": "۵",
        "6": "۶",
        "7": "۷",
        "8": "۸",
        "9": "۹",
    }

    for e, p in numbers.items():
        mystr = mystr.replace(e, p)
    return mystr



    

def date_convert(time):

    time = timezone.localtime(time)
    today = date.today()
    time_today = '{},{},{}'.format(today.year, today.month, today.day)
    
    # yesterday = date.today()-timedelta(1)
    
    time_to_str = '{},{},{}'.format(time.year, time.month, time.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    
    if time_today == time_to_str:
        mystr = '{} {}:{}'.format('امروز', time.hour, time.minute)
        return persian_numbers_converter(mystr)

    
  
    mystr = '{}-{}-{}'.format(
        time_to_tuple[0],
        time_to_tuple[1],
        time_to_tuple[2],
      
    )

    return persian_numbers_converter(mystr)
