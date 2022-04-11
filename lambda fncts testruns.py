import json
from functools import reduce
import csv
from pickletools import decimalnl_short
file=open(r"C:\Users\willi\Downloads\911_Calls_for_Service_(Last_30_Days).csv",'r')
reader = csv.DictReader(file)
data_dictionary_list=[]
for row in reader:
    data_dictionary_list.append(row)

int_test=2
print(type(int_test))
file.close()
print(data_dictionary_list[1].keys())
zip_filter_list = list(filter(lambda x:x['zip_code']!='0', data_dictionary_list))
zip_and_neighborhood_filter_list = list(filter(lambda x:x['neighborhood']!='',zip_filter_list))

dispatch_time_list=[]
total_response_time_list=[]
total_time_list=[]
for i in range(len(zip_and_neighborhood_filter_list)):
    if zip_and_neighborhood_filter_list[i]['dispatchtime']!='':
        dispatch_time_list.append(float(zip_and_neighborhood_filter_list[i]['dispatchtime']))
    else:
        dispatch_time_list.append(0)
    if zip_and_neighborhood_filter_list[i]['totalresponsetime']!='':
        total_response_time_list.append(float(zip_and_neighborhood_filter_list[i]['totalresponsetime']))
    else:
        total_response_time_list.append(0)
    if zip_and_neighborhood_filter_list[i]['totaltime']!='':
        total_time_list.append(float(zip_and_neighborhood_filter_list[i]['totaltime']))
    else:
        total_time_list.append(0)
 

sum_dispatch_time=reduce(lambda x, y: x+y, dispatch_time_list)
sum_total_response_time=reduce(lambda x,y: x+y, total_response_time_list)
sum_total_time=reduce(lambda x,y:x+y, total_time_list)
print(f"Average dispatch time is: {sum_dispatch_time/len(dispatch_time_list)}")
print(f"Average total response time is: {sum_total_response_time/len(total_response_time_list)}")
print(f"Average totat time is: {sum_total_time/len(total_time_list)}")















