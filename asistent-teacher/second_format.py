# simple solution
def format_duration(seconds):
    minutes = seconds//60
    seconds = seconds % 60
    hours = minutes//60
    minutes = minutes % 60
    days = hours//24
    hours = days%24
    months = int(days // 30.428)
    days = int(days%30.428)
    years = months//12
    months = months % 12
    century = years//100
    years = years % 100
    
    return f"{century} asr, {years} yil, {months} oy, {days} kun, {hours} soat, {minutes} minut, {seconds} second"


# fancy solution
def time_format(seconds):
    memo = [
        [1, 'soniya'],
        [60, 'daqiqa'],
        [60, 'soat'],
        [24, 'kun'],
        [30.428, 'oy'],
        [12, 'yil'],
        [100, 'asr']
        # [1, 'end']
    ]
    i = 0
    for ind in range((l := len(memo)) - 1):
        if (time := seconds // memo[ind][0]):
            print(time)
            next_char = time % memo[ind + 1][0]

            memo[ind] = f"{int(next_char)} {memo[ind][1]}"
            seconds = time - next_char
            i = ind
            
    memo = memo[0:i+1]

    return f"{time} asr" + ", ".join(memo[::-1])









duration = int(input("Soniyalarni kiriting:  "))
print(time_format(duration))
print(format_duration(duration))
