def add():
    try:
        contact_name = input("Enter contact name\n")

        contact_phone = input("Enter contact phone number\n")

    except EOFError as exception:
        # print "You entered end of file. Contact not added"
        raise exception
    except KeyboardInterrupt as exception:
        # print "Keyboard interrupt. Contact not added"
        raise exception
    contact_file=open("contacts.txt", 'w')
    contact_file.write(contact_name)
    contact_file.write(str(contact_phone))
    contact_file.close()
add()
