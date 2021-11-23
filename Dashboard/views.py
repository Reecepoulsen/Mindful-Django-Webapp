from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render
from plotly.offline import plot
import hw_session
from hw_session.models import Hw_Data, Session_Data
from datetime import datetime
import plotly.express as px
import pandas as pd

today = datetime.now().day

current_hour = str(datetime.now().hour)
current_mins = str(datetime.now().minute)
#full time is the float value of the current hour
full_time = round(int(current_hour) + (int(current_mins)/60),2)

def dash(request):
    y1 = {}

    days = []
    hours = []

    fin1 = []
    hr1 = []

    data_quick = pd.DataFrame(list(Session_Data.objects.all().values()))
    for time in data_quick['finish_time']:
        fin2 = time.date().day
        hr2 = time.hour - 7
        if hr2 < 0:
            hr2 = 24 + hr2
            fin2 = fin2 - 1
        fin1.append(fin2)
        hr1.append(hr2)
    data_quick['date_day'] = fin1
    data_quick['fin_hour'] = hr1

    time_df = pd.DataFrame(data_quick, columns = ['id','date_day','fin_hour','break_interval','time_limit_mins','time_limit_hours'])

    graphs = []
    fig = px.bar(time_df, x='date_day', y='fin_hour', title="how thick the got dang square be",
                    color='fin_hour')
    plot_div = plot({'data': fig}, 
                     output_type='div')

    return render(request, 'Dashboard/page.html',
                context={'plot_div': plot_div})
