import random, time, sched, names, re

f=open("data.txt", "r")
data=f.read().splitlines()

def random_line(lines):
    return(random.choice(lines))

def send_data(name,ic,date,event):
    print("sending data...")
    
def validate_data(data_line):
    line_list=data_line.split(",")
    print(line_list)
    name=''.join(line_list[0]).replace(" ","")
    ic=''.join(line_list[1].replace(" ",""))
    date=''.join(line_list[2].replace(" ",""))
    event=''.join(line_list[3].replace(" ",""))
    if (name.isalpha()):
        rex=re.compile('S[0-9]{7}[A-Z]')
        if(rex.match(ic)):
            print("match")
            send_data(name,ic,date,event)
        else:
            print("wrong IC format")
    else:
        print("wrong name format. enter alphabets only.")
        
   

s = sched.scheduler(time.time, time.sleep)

def do_something(sc):
    data_line=random_line(data)
    print(data_line)
    validate_data(data_line)
    s.enter(3,1,do_something, (s,))


s.enter(3,1,do_something, (s,))
s.run()
