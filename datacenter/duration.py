def format_duration(td):
    minutes, seconds = divmod(td.seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f'{td.days} days {hours} hours {minutes} minutes'

