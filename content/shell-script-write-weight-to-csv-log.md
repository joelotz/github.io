Title: Shell Script to Write Your Weight to a csv Log File
Date: 2020-06-11
Tags: Bash
Author: Joe
Keywords: ubuntu 20.4, weight logging shell script, log from terminal
Version: OS, Ubuntu 20.04 LTS, Bash, 5.0.16(1)-release

I've been exercising lately and I wanted to see the progress of my weight loss; so I write a stupid little script to log my weight from the terminal. I'm posting it because I learned a couple tricks in the writing of the shell script and thought someone else may as well. 

First, it can be placed anywhere but I recommend somewhere in your PATH so that you can execute it from anywhere. A good place is `/usr/local/bin/`. 

Type `logweight --help` to see the usage syntax and examples.
```shell
Usage:

  logweight input [option]

Input:
        -w, --weight      Weight value desired to log in pounds (lbs)

Simple Examples:
        logweight --weight=200
        logweight -w=200

Options:
        -d, --date        Log date in valid 'YYYY-MM-DD' format. If not specified the current UTC date is used.
        -f, --file        Log file path and name. The default is /mnt/DataDrive/Documents/WeightLog.txt.
        -k, --kilograms   Save weight value as kilogram units. Default is standard pounds.
        -c, --convert     Assumes the input weight is in kilograms but converst the value and logs in pounds.
        -l, --pounds      Save weight value as standard pound units. This is the default.
        -p, --print       Prints to the terminal the data that is written into log file.
        -v, --version     Prints the version of this shell script.
        -h, --help        Displays this help message.
        -b, --debug       Does not write to file - but prints the data that would be written

Examples:
        logweight --weight=200.6 --date=2020-01-01     Creates a log entry on a specific day
        logweight --weight=200.6 --kilograms           Creates a log entry in kilograms on the current date
        logweight -w=200.6 -p                          Creates a log entry on the current date and prints the values in terminal
```

Here is the raw file that you can use.
```shell
#!/bin/sh

# A shell script to log personal body weights into /mnt/DataDrive/Documents/WeightLog.txt file
# Written by: Joe Lotz
# License: MIT 
# Last updated: 2020/June/11
#
# logweight --help
# --------------------------------------------------------------

# Set vars
VERS="0.1"
UNITS="lbs"
NOW=$( date -u '+%F' )
FILE="/mnt/DataDrive/Documents/WeightLog.txt"

# Parse input arguments
for i in "$@"
do
case $i in
    -w=*|--weight=*)
    WEIGHT="${i#*=}"
    ;;
    -d=*|--date=*)
    DATE="${i#*=}"
    # Check if valid date input
    if [ "`date '+%Y-%m-%d' -d $DATE 2>/dev/null`" = "$DATE" ]
    then NOW=$DATE
    else printf "\n\e[91m-------ERROR-------\e[0m\nInput date ${DATE} is not valid, specify as: 'YYYY-MM-DD'\n"; exit 1
    fi
    ;;
    -f=*|--file=*)
    FILE="${i#*=}"
    ;;
    -l|--pounds)
    UNITS=lbs
    ;;
    -k|--kilograms)
    UNITS=kgs
    ;;
    -c|--convert)
    if [ "$WEIGHT" & "$UNITS" == "kgs" ] 
    then :
    elif [ "$WEIGHT" ]
    then 
    	WEIGHT=$(echo "$WEIGHT * 2.20462"|bc -l | xargs printf "%.1f")
	UNITS=kgs
    else printf "\n\e[91m-------ERROR-------\e[0m\nWEIGHT value is empty, specify as:\n    'logweight 200 -c' or\n    'logweight --weight=200 --convert' or\n    'logweight -w 200 -c'\n"; exit 1
    fi
    ;;    
    -v|--version)                                   
    printf "Version: ${VERS}\n"
    exit 0         
    ;;
    -b|--debug)
    DEBUG=1
    ;;
    -p|--print)
    VERBOSE=1
    ;;
    -h|--help)
    printf "\nUsage:\n\n  logweight input [option]\n\nInput:\n        -w, --weight      Weight value desired to log in pounds (lbs)\n\nSimple Examples:\n        logweight --weight=200\n        logweight -w=200\n\nOptions:\n        -d, --date        Log date in valid 'YYYY-MM-DD' format. If not specified the current UTC date is used.\n        -f, --file        Log file path and name. The default is ${FILE}.\n        -k, --kilograms   Save weight value as kilogram units. Default is standard pounds.\n        -c, --convert     Assumes the input weight is in kilograms but converst the value and logs in pounds.\n        -l, --pounds      Save weight value as standard pound units. This is the default.\n        -p, --print       Prints to the terminal the data that is written into log file.\n        -v, --version     Prints the version of this shell script.\n        -h, --help        Displays this help message.\n        -b, --debug       Does not write to file - but prints the data that would be written\n\nExamples:\n        logweight --weight=200.6 --date=2020-01-01     Creates a log entry on a specific day\n        logweight --weight=200.6 --kilograms           Creates a log entry in kilograms on the current date\n        logweight -w=200.6 -p                          Creates a log entry on the current date and prints the values in terminal\n\n"
    
    exit 0
    ;;
    *)
    printf "\n\e[91m-------ERROR-------\e[0m\nUnknown input argument, check your syntax.\nSee help file by typing  'logweight --help'\n"
    exit 1
    ;;
esac
done

if [ -z "$WEIGHT" ]
then
    printf "\n\e[91m-------ERROR-------\e[0m\nWEIGHT value is empty, specify as:\n    'logweight 200' or\n    'logweight --weight=200' or\n    'logweight -w 200'\n"
    exit 1
else
    OUTPUT="${NOW}, ${WEIGHT}, ${UNITS}"
    if [ "$VERBOSE" ]; then echo "Log file: ${FILE}\nEntry: ${OUTPUT}"; fi
    if [ -z "$DEBUG" ]; then echo $OUTPUT >>$FILE; fi
fi
```
