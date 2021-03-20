import sys



def main(args=None):
    """
        This program that parses the command line, creates a
        Student, and prints a description of the student to
        standard out by invoking its toString method.
    """

    if args is None:
        args = sys.argv[1:]
    parse_cli_argv(args)

    print (args)
    print(f"Missing command line arguments")

def parse_cli_argv(argv):
    print(argv)
    if '-README' in argv:
        print(usage)()
        exit(0)

    is_print_opt_set = False
    print_option_counter = 0
    for argv in argv:
        if argv == '-print':
            print_option_counter +=1

    if print_option_counter!=1:
        print("only one -print option is allowed.")
        print(usage)()
        return

    if "-print" in argv and print_option_counter==1 and argv[1]=='-print':
        is_print_opt_set=True

    arg_indx =0
    if is_print_opt_set:
        arg_indx = 1

    customer = argv[arg_indx]
    arg_indx +=1
    caller = argv[arg_indx]

def usage():
    description = 'usage: project2 [options] <args> are (in this order):'\
                  '\n\tcustomer\tPerson whose phone bill we❜re modeling'\
                  '\n\tcallerNumber\tPhone number of caller'\
                  '\n\tcalleeNumber\tPhone number of person who was called'\
                  '\n\t\tstartTime\tDate and time call began (24-hour time)'\
                  '\n\tendTime\t\tDate and time call ended (24-hour time)'\
                  '\noptions are (options may appear in any order):'\
                  '\n\t-print\t\tPrints a description of the new phone call'\
                  '\n\t-README\t\tPrints a README for this project and exits'\

    return description

def _str_(self):
    newstr=self.customer+""+self.callerNumber+""+self.callerNumber+""+self.startTime+""+self.endTime
    return newstr

def main():
    myObj=PhoneCall(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
    print(myObj)
    print("DESCRIPTION")
main(parse_cli_argv())

    
if __name__ == "__main__":
    main()