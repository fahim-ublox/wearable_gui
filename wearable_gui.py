from tkinter import *
from json import *
from wearable_serial import *
from threading import Thread


printable_list = []

master = Tk()

canvas_width = 256
canvas_height = 128
w = Canvas(master, 
           width=canvas_width,
           height=canvas_height)
w.pack()

def append(my_dict ):
    if my_dict['type'] == 'hash':
        w.create_line(my_dict['column'], my_dict['row'],my_dict['column'] + my_dict['size'], my_dict['row'], fill="black",  width=1)
    else:
        w.create_line(my_dict['column'], my_dict['row'],my_dict['column'] + my_dict['size'], my_dict['row'], fill="green",  width=1)
    printable_list.append(my_dict)
    

def display_data(serial = True):

    while 1:

        if serial == False:
            my_file = open("putty.text", "r") 
            a = my_file.read()
        else:
            a = serial_read_data()
            

        
        newline_count = 0 
        first_sequence = 0
        last_sequence = 0

        for i in range(len(a)):
            if a[i] == 'H':
                first_sequence = i+1
                print first_sequence
                break

        last_sequence = len(a) # backup
    ##    for i in range(first_sequence, len(a)):
    ##        if a[i] == 'H':
    ##            last_sequence = i
    ##            print last_sequence
    ##            break
                
        my_print_screen = a[first_sequence:last_sequence]

        data_file = open("data.text", "w")
        dump(my_print_screen, data_file)

        #print my_print_screen
        #return
        hash_seq = False
        space_seq  = False
        column = 0
        row = 0

        hash_list = {}
        space_list = {}
        
        for i in range(len(my_print_screen)):
            if my_print_screen[i] == '#':
                if hash_seq == False:
                    hash_list['type'] = 'hash'
                    hash_list['column'] = column
                    hash_list['row'] = row
                    hash_seq = True
                    if space_seq == True :
                        space_list['size'] = column - space_list['column']
                        append(space_list)
                        #print space_list
                        space_seq = False
                else:
                    pass
                    
            elif my_print_screen[i] == ' ':
                if space_seq == False:
                    space_list['type'] = 'space'
                    space_list['column'] = column
                    space_list['row'] = row
                    space_seq = True
                    if hash_seq == True :
                        hash_list['size'] = column - hash_list['column']
                        append(hash_list)
                        #print hash_list 
                        hash_seq = False
                    
            if my_print_screen[i] == '\n':
                if hash_seq == True:
                    hash_list['size'] = column - hash_list['column'] 
                    append(hash_list)
                    #print hash_list
                if space_seq == True :
                    space_list['size'] = column - space_list['column']
                    append(space_list)
                    #print space_list
                space_seq = False
                hash_seq = False
                row = row + 1
                column = 0
            else:
                column = column + 1

    

        


if __name__ == "__main__":
    
    thread = Thread(target = display_data, args = (True, ))
    thread.start()
    #thread.join()




##    for i in range(len(printable_list)):
##        #w.create_line(printable_list[i]['column'], printable_list[i]['row'],printable_list[i]['column'] + printable_list[i]['size'], printable_list[i]['row'], fill="#476042",  width=1)
##        #w.create_line(printable_list[i]['row'], printable_list[i]['column'],printable_list[i]['row'] + printable_list[i]['size'], printable_list[i]['column'], fill="#476042",  width=1)
##        pass
##
##    output_file = open("output.text", "w")
##    dump(printable_list, output_file)


    mainloop()
