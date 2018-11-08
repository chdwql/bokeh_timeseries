from bokeh.plotting import figure, show, output_file, gridplot
import pandas as pd


ts = pd.read_csv('test_data.xlsx', index_col=0, parse_dates=True)

p1 = figure(x_axis_type='datetime', title=u'地电场第一装置南北向')
ts1 = ts[(ts['ITEMID'] == 3411) & (ts['STATIONID'] == 370053)]
p1.line(ts1.index, ts1['OBSVALUE'])
p1.yaxis.axis_label = 'mv/km'

p2 = figure(x_axis_type='datetime', title=u'地电场第一装置东西向')
ts2 = ts[(ts['ITEMID'] == 3412) & (ts['STATIONID'] == 370053)]
p2.line(ts1.index, ts2['OBSVALUE'])
p2.yaxis.axis_label = 'mv/km'

p3 = figure(x_axis_type='datetime', title=u'地电场第一装置北东向')
ts3 = ts[(ts['ITEMID'] == 3413) & (ts['STATIONID'] == 370053)]
p3.line(ts1.index, ts3['OBSVALUE'])
p3.yaxis.axis_label = 'mv/km'

p4 = figure(x_axis_type='datetime', title=u'地电场第二装置南北向')
ts4 = ts[(ts['ITEMID'] == 3421) & (ts['STATIONID'] == 370053)]
p4.line(ts1.index, ts4['OBSVALUE'])
p4.yaxis.axis_label = 'mv/km'

p5 = figure(x_axis_type='datetime', title=u'地电场第二装置东西向')
ts5 = ts[(ts['ITEMID'] == 3422) & (ts['STATIONID'] == 370053)]
p5.line(ts1.index, ts5['OBSVALUE'])
p5.yaxis.axis_label = 'mv/km'

p6 = figure(x_axis_type='datetime', title=u'地电场第二装置北东向')
ts6 = ts[(ts['ITEMID'] == 3423) & (ts['STATIONID'] == 370053)]
p6.line(ts1.index, ts6['OBSVALUE'])
p6.xaxis.axis_label = 'Date'
p6.yaxis.axis_label = 'mv/km'

output_file("ele.html")

show(gridplot([[p1], [p2], [p3], [p4], [p5], [p6]], plot_width=1000, plot_height=200))
