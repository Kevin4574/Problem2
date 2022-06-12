import pandas as pd
import plotly, json
import plotly.graph_objs as go

def clean_data():
    df = pd.read_csv(r'D:\金融股票\Udacity\Data Science\2. Software Engineering\6. Web Development\HTML\Back-End\9 Flask with Pandas and Plotly demo\data\API_SP.RUR.TOTL.ZS_DS2_en_csv_v2_9948275.csv',
                     skiprows=4)
    # Filter for 1990 and 2015, top 10 economies
    df = df[['Country Name','1990', '2015']]
    countrylist = ['United States', 'China', 'Japan', 'Germany', 'United Kingdom', 'India', 'France', 'Brazil', 'Italy', 'Canada']
    df = df[df['Country Name'].isin(countrylist)]

    # melt year columns  and convert year to date time
    df_melt = df.melt(id_vars='Country Name', value_vars = ['1990', '2015'])
    df_melt.columns = ['country','year', 'variable']
    df_melt['year'] = df_melt['year'].astype('datetime64[ns]').dt.year

    # add column names
    df_melt.columns = ['country', 'year', 'percentrural']

    # prepare data into x, y lists for plotting
    df_melt.sort_values('percentrural', ascending=False, inplace=True)

    data = []
    for country in countrylist:
        x_val = df_melt[df_melt['country'] == country].year.tolist()
        y_val =  df_melt[df_melt['country'] == country].percentrural.tolist()
        data.append((country, x_val, y_val))

    return data

def plot1():
    # read in data
    data = clean_data()
    print('===data===')
    print(data[0])

    country1 = data[0][0]
    x1 = data[0][1]
    y1 = data[0][2]

    # set up chart with plotly, this is setup is very similar with plotly setup in HTML
    graph1 = [go.Scatter(x = x1,
                         y = y1,
                         mode = 'lines',
                         name = country1)]
    print('===graph===')
    print(graph1)

    layout = dict(title = 'change in hectares land per person 1990 to 2015',
                  xaxis = dict(title = 'year',
                               autotick = False,
                               tick0 = 1990,
                               dtick = 25),
                  yaxis = dict(title = 'Hectares')
                  )
    print('===layout===')
    print(layout)

    figure = []
    figure.append(dict(data = graph1,layout = layout))
    print('===figure===')
    print(figure)


    # convert the plotly figure to Json for java-script and html template
    figure_json = json.dumps(figure,
                             cls=plotly.utils.PlotlyJSONEncoder)
    print('===json figure===')
    print(figure_json)

    #create plot ids for html id tag
    ids = ['figure-{}'.format(i) for i,_ in enumerate(figure)]
    print('===ids===')
    print(ids)

    return ids,figure_json
