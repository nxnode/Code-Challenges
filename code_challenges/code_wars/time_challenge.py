def readable_time(seconds):
    hours = seconds // 3600
    new_seconds = seconds - (hours * 3600)
    minutes = new_seconds // 60
    new_seconds = new_seconds - (minutes * 60)
    return f"{pad(hours)}:{pad(minutes)}:{pad(new_seconds)}"


def pad(number):
    if len(str(number)) < 2:
        return f"0{number}"
    return f"{number}"
