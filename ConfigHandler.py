# Useful Fx for grabing config values
def GrabConfigValue(key, fileName):
    with open(fileName, mode='r') as config:
        for row in config:
            if key in row:
                split = row.split('=')
                value = split[1]
                
                return value.rstrip()


