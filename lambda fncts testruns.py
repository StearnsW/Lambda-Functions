import json
from functools import reduce
import csv
from pickletools import decimalnl_short
file=open(r"C:\Users\willi\Downloads\911_Calls_for_Service_(Last_30_Days).csv",'r')
reader = csv.DictReader(file)
data_dictionary_list=[]
for row in reader:
    data_dictionary_list.append(row)

file.close()
zip_filter_list = list(filter(lambda x:x['zip_code']!='0', data_dictionary_list))
zip_and_neighborhood_filter_list = list(filter(lambda x:x['neighborhood']!='',zip_filter_list))

dispatch_time_list=[]
total_response_time_list=[]
total_time_list=[]
neighborhood_set=set()
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
    neighborhood_set.add(zip_and_neighborhood_filter_list[i]['neighborhood'])

 

sum_dispatch_time=reduce(lambda x, y: x+y, dispatch_time_list)
sum_total_response_time=reduce(lambda x,y: x+y, total_response_time_list)
sum_total_time=reduce(lambda x,y:x+y, total_time_list)
print(f"Average dispatch time is: {sum_dispatch_time/len(dispatch_time_list)}")
print(f"Average total response time is: {sum_total_response_time/len(total_response_time_list)}")
print(f"Average totat time is: {sum_total_time/len(total_time_list)}")

neighborhoods_dictionary_list=[]
neighborhood_dispatch_time_list=[]
neighborhood_total_response_time_list=[]
neighborhood_total_time_list=[]
for neighborhood in sorted(neighborhood_set):
    neighborhood_list=list(filter(lambda x:x['neighborhood']==neighborhood, zip_and_neighborhood_filter_list))
    for i in range(len(neighborhood_list)):
        if neighborhood_list[i]['dispatchtime']!='':
            neighborhood_dispatch_time_list.append(float(neighborhood_list[i]['dispatchtime']))
        else:
            neighborhood_dispatch_time_list.append(0)
        if neighborhood_list[i]['totalresponsetime']!='':
            neighborhood_total_response_time_list.append(float(neighborhood_list[i]['totalresponsetime']))
        else:
            neighborhood_total_response_time_list.append(0)
        if neighborhood_list[i]['totaltime']!='':
            neighborhood_total_time_list.append(float(neighborhood_list[i]['totaltime']))
        else:
            neighborhood_total_time_list.append(0)
    sum_dispatch_time=reduce(lambda x, y: x+y, neighborhood_dispatch_time_list)
    avg_dt=sum_dispatch_time/len(neighborhood_dispatch_time_list)
    sum_total_response_time=reduce(lambda x,y: x+y, neighborhood_total_response_time_list)
    avg_trt=sum_total_response_time/len(neighborhood_total_response_time_list)
    sum_total_time=reduce(lambda x,y:x+y, neighborhood_total_time_list)
    avg_tt=sum_total_time/len(neighborhood_total_time_list)
    
    neighborhoods_dictionary_list.append({'neighborhood':neighborhood,'average dispatch time':avg_dt,'average total response time':avg_trt,'average total time':avg_tt})
json_file=open('nieghborhood stats.json','w') # open the file to edit
json.dump(neighborhoods_dictionary_list,json_file)
file.close()










