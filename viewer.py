import datetime
import matplotlib.pyplot as plt
import datetime as dt
import squarify
import pandas as pd

# read apps
data = {}

# display a timedelta in a clean way (doesn't exitst in datetime)


def timedeltaToStr(duration: datetime.timedelta):
    days, seconds = duration.days, duration.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    if days == 0:
        return f'{hours}:{minutes:02d}'
    return f'{days}:{hours:02d}:{minutes:02d}'


# calculate cumulated app usage
with open('apps.csv', 'r') as file:
    for x in file:
        line = x.split(',')
        app = line[0]
        try:
            start = line[1]
            end = line[2].strip('\n')

        except:
            print(f'Parsing error at {x}')
        else:
            duration = dt.datetime.strptime(
                end, "%Y-%m-%d %H:%M:%S")-dt.datetime.strptime(start, "%Y-%m-%d %H:%M:%S")

            if app == 'idle':
                pass
            else:
                if app in data:
                    data[app] = data[app] + duration
                else:
                    data[app] = duration

others = []
print(data)
# remove apps that have a low cumulated time
for app in list(data):
    test = app
    duration = data[app]
    if duration < dt.timedelta(seconds=300):
        data.pop(app)
        if 'Other' in data:
            data['Other'] = data['Other'] + duration
        else:
            data['Other'] = duration
            others.append(test)

values = []
names = []

for key in data:
    print(f'{key}: {timedeltaToStr(data[key])}')
    names.append(f'{key} | {timedeltaToStr(data[key])}')
    values.append(data[key].seconds + data[key].days*86400)


print(others)

plt.pie(values, labels=names, labeldistance=1.5)
plt.show()


df = pd.DataFrame({'values': values, 'name': names})
df = df.sort_values(by=['values'])

# plot it
squarify.plot(sizes=df['values'], label=df['name'], alpha=.8)
plt.axis('off')
plt.show()
