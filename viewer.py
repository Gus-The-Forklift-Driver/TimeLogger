import datetime
import matplotlib.pyplot as plt
import datetime as dt
import squarify
import pandas as pd

# read apps
data = {}


def timedeltaToStr(duration: datetime.timedelta):
    days, seconds = duration.days, duration.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f'{days} Days, {hours}:{minutes}'


with open('apps.csv', 'r') as file:
    for x in file:
        line = x.split(',')
        app = line[0]
        try:
            start = line[1]
            end = line[2].strip('\n')

        except:
            print('parsing error')
        else:
            duration = dt.datetime.strptime(
                end, "%Y-%m-%d %H:%M:%S")-dt.datetime.strptime(start, "%Y-%m-%d %H:%M:%S")

            if app in data:
                data[app] = data[app] + duration
            else:
                data[app] = duration

for app in list(data):
    duration = data[app]
    if duration < dt.timedelta(minutes=10):
        data.pop(app)
        if 'Other' in data:
            data['Other'] = data['Other'] + duration
        else:
            data['Other'] = duration

values = []
names = []

for key in data:
    print(f'{key}: {timedeltaToStr(data[key])}')
    names.append(f'{key} | {timedeltaToStr(data[key])}')
    values.append(data[key].seconds + data[key].days*86400)

print(names)
print(values)

plt.pie(values, labels=names, labeldistance=1.5)
plt.show()


df = pd.DataFrame({'values': values, 'name': names})
df = df.sort_values(by=['values'])

# plot it
squarify.plot(sizes=df['values'], label=df['name'], alpha=.8)
plt.axis('off')
plt.show()
