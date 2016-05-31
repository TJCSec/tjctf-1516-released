#!/usr/bin/python3
import time
import sys
import json
import random

library = json.load(open("library.json"))

boot = """- - - - - SYSTEM STARTUP - - - - -
START_KERNEL
INIT
RUNLEVEL

LAUNCHING...
CORE ANALYTICS
NEURAL NETWORKS
HEURISTIC ENGINES
RECURSION PROCESSORS
EVOLUTIONARY GENERATORS
BAYESIAN NETWORKS
DATA ACQUISITION
CRYPTOGRAPHIC ALGORITHMS
DOCUMENT PROCESSORS
COMPUTATIONAL LINGUISTICS
VOICEPRINT IDENTIFICATION
NATURAL LANGUAGE PROCESSING
FACIAL RECOGNITION
GAIT ANALYSIS
BIOMETRIC RECOGNITION
SUBJECT IDENTIFICATION
PATTERN MINING
INTEL INTERPRETATION
THREAT DETECTION
THREAT CLASSIFICATION
DISSEMINATION PROTOCOLS
CONTINUITY-OF-OPERATIONS PROTOCOLS

INFILTRATING...""".split("\n")

def print_line(l):
    for j in l:
        print(j, end="")
        sys.stdout.flush()
        if j == ".":
            time.sleep(0.1)
        elif j == "\n":
            time.sleep(0.02)
        else:
            time.sleep(0.0075)

def find_digit_in_library(digit):
    items = list(library.items())
    random.shuffle(items)
    item = items.pop()
    while digit not in item[1]:
        item = items.pop()
    return item[0], item[1].index(digit)

def get_ebcdic_digits(char):
    return str(char.encode("cp1140")[0])

def encode_library_message(message):
    print_line("MESSAGE OF LENGTH {} FOLLOWS\n".format(len(message)))
    for char in message:
        digits = get_ebcdic_digits(char)
        for digit in digits:
            print_line("{} {} ... ".format(*find_digit_in_library(digit)))
        print_line("\n")

def decode_library_message(data):
    x = [[j.strip() for j in i.split(" ...")[:-1]] for i in data.split("\n")][:-2]
    message = []
    for block in x:
        cn = ""
        for digit in block:
            dgts = digit.split()
            if not dgts:
                continue
            dewey = " ".join(dgts[:-1])
            idx = dgts[-1]
            cn += library[dewey][int(idx)]
        if cn:
            message.append(int(cn))
    return bytes(message).decode("cp1140")

for i in boot:
    print_line(i)
    print()
    time.sleep(0.2)

time.sleep(1)

while True:
    print()
    print_line("NORTHERNLIGHTS LOGIN: ")
    username = input().lower()
    if username != "ncingram" and username != "ningram" and username != "nathan" and username != "nathan.ingram" and username != "ingram":
        if username == "hfinch" or username == "finch":
            time.sleep(2)
            print_line("REMOTE ACCESS DISABLED AT USER REQUEST\n")
        else:
            time.sleep(2)
            print_line("UNKNOWN USER\n")
    else:
        if username != "ncingram":
            print_line("USER ALIAS FOUND {} -> NCINGRAM\n".format(username.upper()))
        break

while True:
    try:
        print_line("CONTINGENCY # ")
        cmd = input().lower()
        cmd, args = cmd.split()[0], cmd.split()[1:]

        if cmd == "help":
            print_line("RETRIEVING VALID SYSTEM COMMANDS...")
            time.sleep(0.2)
            print()
            print_line("HELP: SHOW HELP ON SYSTEM COMMANDS\n")
            print_line("SHOW: SHOW RUNNING SYSTEM PROPERTIES\n")
            print_line("    SHOW CONFIG: DISPLAY SYSTEM CONFIGURATION\n")
            print_line("    SHOW USERS: DISPLAY AVAILABLE USERS ON SYSTEM\n")
            print_line("    SHOW PROCESSES: DISPLAY RUNNING PROCESSES\n")
            print_line("    SHOW PRIVILEGES: CHECK YOUR PRIVILEGE\n")
            print_line("    SHOW LIST: OUTPUT A LIST OF NUMBERS\n")
            print_line("        SHOW LIST RELEVANT: DISPLAY NUMBERS RELEVANT TO NATIONAL SECURITY\n")
            print_line("        SHOW LIST IRRELEVANT: DISPLAY NUMBERS IRRELEVANT TO NATIONAL SECURITY\n")
            print_line("    SHOW LIBRARY: OUTPUT A LIST OF BOOKS\n")
            print_line("OVERRIDE: ENTER ENCODED COMMAND, BYPASSING ALL PERMISSIONS\n")

        elif cmd == "show":
            if len(args) < 1:
                print_line("CHOOSE CONFIG, USERS, PROCESSES, PRIVILEGES, LIBRARY, LIST RELEVANT, LIST IRRELEVANT\n")
                continue
            if args[0] == "config":
                print_line("SYSTEM CONFIGURATION\n")
                print_line("    HOSTNAME: NORTHERNLIGHTS\n")
                print_line("    REMOTE ACCESS NODE: IFT-00345867\n")
                print_line("    SYSTEM ENCODING: EBCDIC\n")
            if args[0] == "users":
                print_line("SYSTEM USERS\n")
                print_line("    HFINCH    HAROLD FINCH\n")
                print_line("    NCINGRAM  NATHAN INGRAM\n")
            if args[0] == "processes":
                print_line("SYSTEM PROCESSES\n")
                print_line("    PRIOPERS  PRIMARY OPERATIONS\n")
                print_line("    RESEARCH  ISA DESCRIPTION REDACTED\n")
                print_line("    CLASSIFY  TARGET CLASSIFICATION\n")
                print_line("    CNTNGNCY  CONTINGENCY\n")
            if args[0] == "privileges":
                print_line("SYSTEM PRIVILEGES\n")
                print_line("    LOGGED IN AS NCINGRAM [NATHAN INGRAM]\n")
                print_line("    USER ROLE AUX_ADMIN *\n")
                print_line("    * PERMISSION RESTRICTED: DISALLOW SHOW LIST IRRELEVANT\n")
                print_line("    * RESTRICTION ADDED SEP 13 2010 BY USER HFINCH ROLE ADMIN [HAROLD FINCH]\n")
            if args[0] == "list":
                if len(args) < 2:
                    print_line("YOU MUST SPECIFY A LIST TO DISPLAY\n")
                    continue
                if args[1] == "irrelevant":
                    print_line("PERMISSIONS RESTRICTED\n")
                    print_line("EXECUTE \"SHOW PRIVILEGES\" COMMAND FOR DETAILS\n")
                elif args[1] == "relevant":
                    encode_library_message("THIS IS NOT YOUR FLAG")
                else:
                    print_line("UNKNOWN LIST\n")
            if args[0] == "library":
                for key, val in library.items():
                    print_line("{:17s} :: {:20s}\n".format(key, val))

        elif cmd == "override":
            print_line("ENTER ENCODED MESSAGE TERMINATED BY EMPTY LINE\n")
            buf = ""
            while not buf.endswith("\n\n"):
                buf += input() + "\n"
            try:
                cmd = decode_library_message(buf).strip().lower()
            except:
                print_line("FAILED TO DECODE MESSAGE\n")
                continue
            if cmd != "show list irrelevant":
                print_line("PERMISSIONS UNRESTRICTED OR UNKNOWN COMMAND: {}\n".format(decode_library_message(buf)))
            else:
                print_line("SWITCHING TO SECONDARY OPERATIONS...\n\n")
                print_line("MONITORING SURVEILLANCE FEEDS...")
                time.sleep(2.5)
                print_line("\n")
                encode_library_message("tjctf{w3lc0m3_to_th3_m4ch1n3}")
                sys.exit(0)
        else:
            print_line("UNKNOWN COMMAND\n")
    except Exception as e:
        print_line("UNKNOWN SYSTEM ERROR\n")
        print_line("ATTEMPTING ANALYSIS............\n")
        print_line(e)
        print_line("\nANALYSIS FAILED\n")
        print_line("SHUTTING DOWN PRIMARY OPERATIONS...\n")
        sys.exit(0)
