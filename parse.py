from datetime import datetime, timedelta

def commands_from_file(command_file, delim):
    # start at 00:00:00
    start = timedelta(hours=0, minutes=0, seconds=0)
    track_data = []
    
    with open(command_file) as file:
        ## read all those line 
        lines = file.readlines()
    
    for line in lines: 
        # strip off newline
        title, duration = line.rstrip('\n').split(delim)
        # split into minute and secs to build timedelta
        m, s = duration.split(":")
        duration_td = timedelta(minutes=int(m), seconds=int(s))
        # create a list of form [(title, start, end)]
        track_data.append(
            (
                title,
                str(start), 
                str(start + duration_td)
            )
        )
        # increment the start time to the fit the start time of the next song 
        start += duration_td
    print(track_data)
    return track_data
    
