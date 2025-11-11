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




        chart = QChart()
        chart.setTitle("Aktienkurs")
        chart.addAxis(axis_date_time, Qt.AlignmentFlag.AlignBottom)
        chart.addAxis(axis_euro, Qt.AlignmentFlag.AlignLeft)



        self.setChart(chart)