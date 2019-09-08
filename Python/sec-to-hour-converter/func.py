def timeConverter(seconds):
    from datetime import timedelta
    formated = timedelta(seconds=seconds)
    return formated

seconds = float(input('Segundos: '))
timeConverter(seconds)