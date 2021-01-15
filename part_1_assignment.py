import json 

with open ('precipitation.json') as precipitation_file: 
    precipitation_data= json.load(precipitation_file)

# PART ONE 

total_per_month = [0] * 12

for measurement in precipitation_data:
    if 'GHCND:US1WAKG0038' in measurement['station']: 
        month = int(measurement['date'].split('-')[1])
        list_month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        total_per_month[month - 1] += measurement['value']

print(total_per_month)

# PART TWO

year_precipitation = sum(total_per_month)
print(year_precipitation)

monthly_relative_precipitation = []
for i in range(12): 
    monthly_relative_precipitation.append(100 * total_per_month[i] / year_precipitation)
print(monthly_relative_precipitation)

result = {'Total per month': total_per_month, 'Relative total per month': monthly_relative_precipitation, 'Total': year_precipitation}

with open ('result.json', 'w') as precipitation_month_seattle:
   json.dump(result, precipitation_month_seattle, indent = 4)