import time
t_start=time.time()
from prettytable import PrettyTable
import datetime

file = open('testresult.txt','w')

file.write("Query: Enter Query Here\n\n")
file.write("Output Location: Enter location here\n\n")
file.write("Test start time: "+str(datetime.datetime.now())+"\n\n")
t= PrettyTable(['Start Time','Run','No of Records', 'Time(s)','Errors'])

for i in range(10):
    t.add_row([datetime.datetime.now(), str(i+1), 'hey', 'there','0'])
t_end=time.time()
total_execution_time= t_end-t_start


file.write(str(t))
file.write("\nTotal Test Execution Time: "+str(total_execution_time)+" seconds")
file.close()
