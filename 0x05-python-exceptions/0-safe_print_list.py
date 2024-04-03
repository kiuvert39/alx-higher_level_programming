def safe_print_list(my_list=[], x=0):
    printedElements = 0
    try:
        for i in my_list:
            if printedElements < x:
                print ("{:d}".format(i), end='') 
                printedElements += 1
        pass
    except Exception as e:
        print("An error occurred: {:d}".format(e))
    finally:
        print()
    return printedElements