import json
from functools import reduce
import csv
from pickletools import decimalnl_short
from statistics import mean
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
for i in range(len(zip_and_neighborhood_filter_list)):
    if zip_and_neighborhood_filter_list[i]['dispatchtime']!='':
        zip_and_neighborhood_filter_list[i]['dispatchtime']=float(zip_and_neighborhood_filter_list[i]['dispatchtime'])
    else:
        zip_and_neighborhood_filter_list[i]['dispatchtime']=0
    if zip_and_neighborhood_filter_list[i]['totalresponsetime']!='':
        zip_and_neighborhood_filter_list[i]['totalresponsetime']=float(zip_and_neighborhood_filter_list[i]['totalresponsetime'])
    else:
        zip_and_neighborhood_filter_list[i]['totalresponsetime']=0
    if zip_and_neighborhood_filter_list[i]['totaltime']!='':
        zip_and_neighborhood_filter_list[i]['totaltime']=float(zip_and_neighborhood_filter_list[i]['totaltime'])
    else:
        zip_and_neighborhood_filter_list[i]['totaltime']=0

 
dispatch_time_list=list(map(lambda x:x['dispatchtime'],zip_and_neighborhood_filter_list))
total_response_time_list=list(map(lambda x:x['totalresponsetime'],zip_and_neighborhood_filter_list))
total_time_list=list(map(lambda x:x['totaltime'],zip_and_neighborhood_filter_list))
sum_dispatch_time=reduce(lambda x, y: x+y, dispatch_time_list)
sum_total_response_time=reduce(lambda x,y: x+y, total_response_time_list)
sum_total_time=reduce(lambda x,y:x+y, total_time_list)
avg_dispatch_time=reduce(lambda x, y: x+y/len(dispatch_time_list), dispatch_time_list,0)
avg_total_response_time=reduce(lambda x,y: x+y/len(total_response_time_list), total_response_time_list,0)
avg_total_time=reduce(lambda x,y:x+y/len(total_time_list), total_time_list,0)
print(f"Average dispatch time is: {sum_dispatch_time/len(dispatch_time_list)}")
print(f"Average total response time is: {sum_total_response_time/len(total_response_time_list)}")
print(f"Average totat time is: {sum_total_time/len(total_time_list)}")
print(avg_dispatch_time)
print(avg_total_response_time)
print(avg_total_time)

neighborhood_set=sorted(set(map(lambda x:x['neighborhood'],zip_and_neighborhood_filter_list)))
neighborhood_dictionary={}
for neighborhood in neighborhood_set:
    neighborhood_dictionary[neighborhood]=list(filter(lambda x:x['neighborhood']==neighborhood, zip_and_neighborhood_filter_list))

for neighborhood in neighborhood_dictionary.keys():
    nh_dispatch_time_list=list(map(lambda x:x['dispatchtime'],neighborhood_dictionary[neighborhood]))
    nh_total_response_time_list=list(map(lambda x:x['totalresponsetime'],neighborhood_dictionary[neighborhood]))
    nh_total_time_list=list(map(lambda x:x['totaltime'],neighborhood_dictionary[neighborhood]))
    nh_avg_dispatch_time=reduce(lambda x, y: x+y/len(nh_dispatch_time_list), nh_dispatch_time_list,0)
    nh_avg_total_response_time=reduce(lambda x,y: x+y/len(nh_total_response_time_list), nh_total_response_time_list,0)
    nh_avg_total_time=reduce(lambda x,y:x+y/len(nh_total_time_list), nh_total_time_list,0)
    print(f"{neighborhood}\n Avg Dispatch:{nh_avg_dispatch_time} Avg Response:{nh_avg_total_response_time} Avg Total:{nh_avg_total_time}")
    print("-------------------------------")
    if neighborhood.find("/")!=-1:
        neighborhood_new=neighborhood.replace("/","&")
    else:
        neighborhood_new=neighborhood
    json_file=open(f'json files\{neighborhood_new}.json','w') # open the file to edit
    json.dump(neighborhood_dictionary[neighborhood],json_file)
    file.close()

# neighborhoods_dictionary_list=[]
# neighborhood_dispatch_time_list=[]
# neighborhood_total_response_time_list=[]
# neighborhood_total_time_list=[]
# for neighborhood in sorted(neighborhood_set):
#     neighborhood_list=list(filter(lambda x:x['neighborhood']==neighborhood, zip_and_neighborhood_filter_list))
#     for i in range(len(neighborhood_list)):
#         if neighborhood_list[i]['dispatchtime']!='':
#             neighborhood_dispatch_time_list.append(float(neighborhood_list[i]['dispatchtime']))
#         else:
#             neighborhood_dispatch_time_list.append(0)
#         if neighborhood_list[i]['totalresponsetime']!='':
#             neighborhood_total_response_time_list.append(float(neighborhood_list[i]['totalresponsetime']))
#         else:
#             neighborhood_total_response_time_list.append(0)
#         if neighborhood_list[i]['totaltime']!='':
#             neighborhood_total_time_list.append(float(neighborhood_list[i]['totaltime']))
#         else:
#             neighborhood_total_time_list.append(0)
#     sum_dispatch_time=reduce(lambda x, y: x+y, neighborhood_dispatch_time_list)
#     avg_dt=sum_dispatch_time/len(neighborhood_dispatch_time_list)
#     sum_total_response_time=reduce(lambda x,y: x+y, neighborhood_total_response_time_list)
#     avg_trt=sum_total_response_time/len(neighborhood_total_response_time_list)
#     sum_total_time=reduce(lambda x,y:x+y, neighborhood_total_time_list)
#     avg_tt=sum_total_time/len(neighborhood_total_time_list)
    
#     neighborhoods_dictionary_list.append({'neighborhood':neighborhood,'average dispatch time':avg_dt,'average total response time':avg_trt,'average total time':avg_tt})
# json_file=open('nieghborhood stats.json','w') # open the file to edit
# json.dump(neighborhoods_dictionary_list,json_file)
# file.close()










