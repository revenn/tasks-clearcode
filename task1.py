#!/usr/bin/python

from collections import Counter

def group_by(stream, field, success=None):
    """
    Function parsing stream object
    :param stream: stream object like from open; field: string, 'year' or 'month'; success (default None)
    :rtype: dict
    :return: parsed data
    """
        
    if (field != 'year' and field != 'month'):
        return "Second param should be year on month!"
            
    if(field == 'year'):
        if(success == True):
            result=[line[13:17] for line in stream if (line[13:17].isdigit() == True and line[193:][0] == 'S')]
        elif(success == False):
            result=[line[13:17] for line in stream if (line[13:17].isdigit() == True and line[193:][0] == 'F')]
        else:
            result=[line[13:17] for line in stream if line[13:17].isdigit() == True]
    else:
        if(success == True):
            result=[line[18:21] for line in stream if (line[18:21].istitle() == True and line[193:][0] == 'S')]
        elif(success == False):
            result=[line[18:21] for line in stream if (line[18:21].istitle() == True and line[193:][0] == 'F')]
        else:
            result=[line[18:21] for line in stream if line[18:21].istitle() == True]

    ret = dict(Counter(result))

    return ret

def main():
    file = open("launchlog.txt")
    try:
        result=group_by(file, 'year', success=False)
        print result
    finally:
        file.close()

if __name__ == "__main__":
    main()
