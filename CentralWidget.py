from PyQt6.QtCharts import QChartView, QChart, QLineSeries, QValueAxis, QScatterSeries, QDateTimeAxis
from PyQt6.QtCore import Qt, QDateTime, QDate, QTime
from PyQt6.QtGui import QColor


class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        axis_date_time = QDateTimeAxis()
        axis_date_time.setTitleText("Datum")
        axis_date_time.setFormat("dd.MM.yyyy")
        date_time_start = QDateTime(2025, 2, 6, 0, 0, 0)
        date_time_end = QDateTime(2025, 3, 10, 0, 0, 0)
        axis_date_time.setRange(date_time_start, date_time_end)

        axis_euro = QValueAxis()
        axis_euro.setTitleText("Wert in €")
        axis_euro.setRange(95.0, 140.0)


#1
        line_series_boersenstart = QLineSeries()
        line_series_boersenstart.setName('Börsenstart')

#2
        line_series_tageshoch = QLineSeries()
        line_series_tageshoch.setName('Tageshoch')

        line_series_tagestief = QLineSeries()
        line_series_tagestief.setName('Tagestief')

        line_series_boersenschluss = QLineSeries()
        line_series_boersenschluss.setName('Börsenschluss')

        #Falls Farbe des Graph geändert werden muss
        pen = line_series_boersenschluss.pen()
        pen.setColor(QColor(Qt.GlobalColor.green))
        line_series_boersenschluss.setPen(pen)




        chart = QChart()
        chart.setTitle("Aktienkurs")
        chart.addSeries(line_series_boersenstart)
        chart.addSeries(line_series_tageshoch)
        chart.addSeries(line_series_tagestief)
        chart.addSeries(line_series_boersenschluss)
        chart.addAxis(axis_date_time, Qt.AlignmentFlag.AlignBottom)
        chart.addAxis(axis_euro, Qt.AlignmentFlag.AlignLeft)


        line_series_boersenstart.attachAxis(axis_date_time)
        line_series_tageshoch.attachAxis(axis_euro)
        line_series_tagestief.attachAxis(axis_euro)
        line_series_boersenschluss.attachAxis(axis_euro)



        self.setChart(chart)