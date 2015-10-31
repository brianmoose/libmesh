#!/usr/bin/env python
from github_traffic_base import *

# Construct an instance of the PlotData class for plotting clones.
class PlotClones(PlotData):
  """
  Plot the weekly git clones and unique cloners.
  """
  def __init__(self):
    super(PlotData, self).__init__()
    self.left_axis_label = 'Clones per Week'
    self.right_axis_label = 'Avg. Daily Unique Clones'
    self.weekly_plot_filename = 'weekly_github_clones.pdf'
    self.monthly_plot_filename = 'monthly_github_clones.pdf'
    self.title_string1 = 'Total Clones:'
    self.title_string2 = 'Avg. Daily Unique Cloners:'
    self.data_array = [
      '2014-Aug-03', 0,   0,
      '2014-Aug-04', 10,  6,
      '2014-Aug-05', 7,   7,
      '2014-Aug-06', 21, 14,
      '2014-Aug-07', 11,  9,
      '2014-Aug-08', 9,   8,
      '2014-Aug-09', 2,   2,
      '2014-Aug-10', 2,   2,
      '2014-Aug-11', 8,   6,
      '2014-Aug-12', 9,   8,
      '2014-Aug-13', 19, 11,
      '2014-Aug-14', 9,   7,
      '2014-Aug-15', 5,   5,
      '2014-Aug-16', 5,   2,
      '2014-Aug-17', 5,   5,
      '2014-Aug-18', 10,  8,
      '2014-Aug-19', 9,   8,
      '2014-Aug-20', 3,   3,
      '2014-Aug-21', 12,  8,
      '2014-Aug-22', 3,   3,
      '2014-Aug-23', 2,   2,
      '2014-Aug-24', 3,   3,
      '2014-Aug-25', 8,   5,
      '2014-Aug-26', 7,   7,
      '2014-Aug-27', 9,   8,
      '2014-Aug-28', 19, 12,
      '2014-Aug-29', 18, 14,
      '2014-Aug-30', 1,   1,
      '2014-Aug-31', 1,   1,
      '2014-Sep-01', 6,   5,
      '2014-Sep-02', 9,   8,
      '2014-Sep-03', 5,   4,
      '2014-Sep-04', 9,   8,
      '2014-Sep-05', 3,   3,
      '2014-Sep-06', 1,   1,
      '2014-Sep-07', 2,   2,
      '2014-Sep-08', 9,   9,
      '2014-Sep-09', 16, 10,
      '2014-Sep-10', 9,   8,
      '2014-Sep-11', 9,   7,
      '2014-Sep-12', 5,   3,
      '2014-Sep-13', 5,   5,
      '2014-Sep-14', 9,   7,
      '2014-Sep-15', 8,   7,
      '2014-Sep-16', 12,  8,
      '2014-Sep-17', 19, 11,
      '2014-Sep-18', 15, 11,
      '2014-Sep-19', 16,  8,
      '2014-Sep-20', 0,   0,
      '2014-Sep-21', 4,   4,
      '2014-Sep-22', 4,   3,
      '2014-Sep-23', 19, 14,
      '2014-Sep-24', 13, 11,
      '2014-Sep-25', 26, 15,
      '2014-Sep-26', 10,  9,
      '2014-Sep-27', 1,   1,
      '2014-Sep-28', 1,   1,
      '2014-Sep-29', 10,  9,
      '2014-Sep-30', 11,  5,
      '2014-Oct-01', 15, 13,
      '2014-Oct-02', 14, 13,
      '2014-Oct-03', 15, 13,
      '2014-Oct-04', 7,   7,
      '2014-Oct-05', 2,   2,
      '2014-Oct-06', 10,  8,
      '2014-Oct-07', 38, 24,
      '2014-Oct-08', 19, 16,
      '2014-Oct-09', 27, 14,
      '2014-Oct-10', 30, 18,
      '2014-Oct-11', 8,   7,
      '2014-Oct-12', 10,  8,
      '2014-Oct-13', 20, 17,
      '2014-Oct-14', 22, 14,
      '2014-Oct-15', 22, 14,
      '2014-Oct-16', 25, 17,
      '2014-Oct-17', 15,  9,
      '2014-Oct-18', 7,   5,
      '2014-Oct-19', 7,   5,
      '2014-Oct-20', 19, 14,
      '2014-Oct-21', 26, 18,
      '2014-Oct-22', 31, 16,
      '2014-Oct-23', 16, 13,
      '2014-Oct-24', 11,  9,
      '2014-Oct-25', 4,   3,
      '2014-Oct-26', 8,   8,
      '2014-Oct-27', 11,  8,
      '2014-Oct-28', 9,   8,
      '2014-Oct-29', 19, 16,
      '2014-Oct-30', 10,  8,
      '2014-Oct-31', 8,   7,
      '2014-Nov-01', 8,   6,
      '2014-Nov-02', 5,   5,
      '2014-Nov-03', 15, 14,
      '2014-Nov-04', 16, 13,
      '2014-Nov-05', 7,   7,
      '2014-Nov-06', 6,   6,
      '2014-Nov-07', 8,   8,
      '2014-Nov-08', 9,   7,
      '2014-Nov-09', 4,   4,
      '2014-Nov-10', 12, 10,
      '2014-Nov-11', 15, 13,
      '2014-Nov-12', 18, 12,
      '2014-Nov-13', 13,  8,
      '2014-Nov-14', 16, 13,
      '2014-Nov-15', 6,   4,
      '2014-Nov-16', 5,   4,
      '2014-Nov-17', 17, 12,
      '2014-Nov-18', 11,  9,
      '2014-Nov-19', 19, 12,
      '2014-Nov-20', 25, 16,
      '2014-Nov-21', 14, 10,
      '2014-Nov-22', 7,   5,
      '2014-Nov-23', 4,   4,
      '2014-Nov-24', 11,  8,
      '2014-Nov-25', 8,   6,
      '2014-Nov-26', 19, 13,
      '2014-Nov-27', 3,   3,
      '2014-Nov-28', 12,  7,
      '2014-Nov-29', 5,   4,
      '2014-Nov-30', 7,   7,
      '2014-Dec-01', 15, 11,
      '2014-Dec-02', 11,  8,
      '2014-Dec-03', 7,   6,
      '2014-Dec-04', 7,   6,
      '2014-Dec-05', 13, 11,
      '2014-Dec-06', 8,   7,
      '2014-Dec-07', 2,   2,
      '2014-Dec-08', 15, 11,
      '2014-Dec-09', 9,   4,
      '2014-Dec-10', 4,   3,
      '2014-Dec-11', 8,   7,
      '2014-Dec-12', 15,  9,
      '2014-Dec-13', 7,   4,
      '2014-Dec-14', 4,   3,
      '2014-Dec-15', 27, 13,
      '2014-Dec-16', 15, 11,
      '2014-Dec-17', 27, 17,
      '2014-Dec-18', 18, 14,
      '2014-Dec-19', 19, 16,
      '2014-Dec-20', 6,  5,
      '2014-Dec-21', 3,  3,
      '2014-Dec-22', 4,  4,
      '2014-Dec-23', 7,  7,
      '2014-Dec-24', 5,  4,
      '2014-Dec-25', 1,  1,
      '2014-Dec-26', 4,  3,
      '2014-Dec-27', 6,  4,
      '2014-Dec-28', 1,  1,
      '2014-Dec-29', 3,  3,
      '2014-Dec-30', 2,  2,
      '2014-Dec-31', 1,  1,
      '2015-Jan-01', 5,  2,
      '2015-Jan-02', 5,  5,
      '2015-Jan-03', 4,  4,
      '2015-Jan-04', 2,  2,
      '2015-Jan-05', 10, 10,
      '2015-Jan-06', 20, 17,
      '2015-Jan-07', 13, 11,
      '2015-Jan-08', 14, 8,
      '2015-Jan-09', 18, 11,
      '2015-Jan-10', 3,  2,
      '2015-Jan-11', 2,  1,
      '2015-Jan-12', 28, 14,
      '2015-Jan-13', 22, 15,
      '2015-Jan-14', 19, 15,
      '2015-Jan-15', 13, 11,
      '2015-Jan-16', 13, 11,
      '2015-Jan-17', 4,  3,
      '2015-Jan-18', 8,  8,
      '2015-Jan-19', 16, 7,
      '2015-Jan-20', 34, 21,
      '2015-Jan-21', 28, 20,
      '2015-Jan-22', 24, 14,
      '2015-Jan-23', 11, 9,
      '2015-Jan-24', 5,  4,
      '2015-Jan-25', 5,  5,
      '2015-Jan-26', 27, 12,
      '2015-Jan-27', 25, 19,
      '2015-Jan-28', 45, 20,
      '2015-Jan-29', 39, 26,
      '2015-Jan-30', 26, 19,
      '2015-Jan-31', 8,  6,
      '2015-Feb-01', 10, 6,
      '2015-Feb-02', 11, 8,
      '2015-Feb-03', 22, 17,
      '2015-Feb-04', 16, 13,
      '2015-Feb-05', 25, 18,
      '2015-Feb-06', 14, 10,
      '2015-Feb-07', 3,  3,
      '2015-Feb-08', 5,  5,
      '2015-Feb-09', 16, 15,
      '2015-Feb-10', 16, 12,
      '2015-Feb-11', 18, 15,
      '2015-Feb-12', 24, 18,
      '2015-Feb-13', 16, 11,
      '2015-Feb-14', 16, 8,
      '2015-Feb-15', 6,  5,
      '2015-Feb-16', 17, 11,
      '2015-Feb-17', 13, 9,
      '2015-Feb-18', 22, 17,
      '2015-Feb-19', 31, 19,
      '2015-Feb-20', 13, 10,
      '2015-Feb-21', 14, 7,
      '2015-Feb-22', 7,  5,
      '2015-Feb-23', 19, 10,
      '2015-Feb-24', 21, 11,
      '2015-Feb-25', 12, 7,
      '2015-Feb-26', 13, 9,
      '2015-Feb-27', 10, 10,
      '2015-Feb-28', 10, 6,
      '2015-Mar-01', 4,  4,
      '2015-Mar-02', 13, 13,
      '2015-Mar-03', 14, 12,
      '2015-Mar-04', 23, 18,
      '2015-Mar-05', 30, 17,
      '2015-Mar-06', 14, 12,
      '2015-Mar-07', 4,  4,
      '2015-Mar-08', 5,  5,
      '2015-Mar-09', 9,  7,
      '2015-Mar-10', 7,  6,
      '2015-Mar-11', 16, 12,
      '2015-Mar-12', 15, 13,
      '2015-Mar-13', 15, 12,
      '2015-Mar-14', 10, 9,
      '2015-Mar-15', 3,  2,
      '2015-Mar-16', 11, 9,
      '2015-Mar-17', 16, 13,
      '2015-Mar-18', 8,  7,
      '2015-Mar-19', 13, 11,
      '2015-Mar-20', 9,  8,
      '2015-Mar-21', 3,  3,
      '2015-Mar-22', 2,  1,
      '2015-Mar-23', 13, 12,
      '2015-Mar-24', 24, 19,
      '2015-Mar-25', 18, 14,
      '2015-Mar-26', 13, 9,
      '2015-Mar-27', 8,  8,
      '2015-Mar-28', 7,  5,
      '2015-Mar-29', 2,  2,
      '2015-Mar-30', 19, 15,
      '2015-Mar-31', 21, 14,
      '2015-Apr-01', 15, 12,
      '2015-Apr-02', 9,  8,
      '2015-Apr-03', 7,  6,
      '2015-Apr-04', 7,  6,
      '2015-Apr-05', 2,  2,
      '2015-Apr-06', 19, 9,
      '2015-Apr-07', 21, 13,
      '2015-Apr-08', 10, 10,
      '2015-Apr-09', 12, 8,
      '2015-Apr-10', 4,  4,
      '2015-Apr-11', 2,  2,
      '2015-Apr-12', 4,  4,
      '2015-Apr-13', 8,  6,
      '2015-Apr-14', 10, 10,
      '2015-Apr-15', 11, 10,
      '2015-Apr-16', 10, 6,
      '2015-Apr-17', 9,  7,
      '2015-Apr-18', 0,  0,
      '2015-Apr-19', 7,  5,
      '2015-Apr-20', 2,  2,
      '2015-Apr-21', 13, 8,
      '2015-Apr-22', 18, 11,
      '2015-Apr-23', 15, 10,
      '2015-Apr-24', 13, 8,
      '2015-Apr-25', 4,  4,
      '2015-Apr-26', 4,  4,
      '2015-Apr-27',    9,    7,
      '2015-Apr-28',    6,    6,
      '2015-Apr-29',   12,    8,
      '2015-Apr-30',   15,   14,
      '2015-May-01',   13,   10,
      '2015-May-02',    5,    4,
      '2015-May-03',    3,    3,
      '2015-May-04',   14,   10,
      '2015-May-05',   12,   10,
      '2015-May-06',   10,    6,
      '2015-May-07',   11,    8,
      '2015-May-08',   11,    8,
      '2015-May-09',    0,    0,
      '2015-May-10',    4,    4,
      '2015-May-11',   17,   13,
      '2015-May-12',   24,   10,
      '2015-May-13',   18,   15,
      '2015-May-14',   10,    7,
      '2015-May-15',   13,    8,
      '2015-May-16',    6,    4,
      '2015-May-17',    3,    3,
      '2015-May-18',   11,   10,
      '2015-May-19',   20,   15,
      '2015-May-20',   15,    9,
      '2015-May-21',   11,   11,
      '2015-May-22',   11,   10,
      '2015-May-23',    3,    3,
      '2015-May-24',    5,    4,
      '2015-May-25',    4,    3,
      '2015-May-26',   22,   18,
      '2015-May-27',   20,   14,
      '2015-May-28',    8,    6,
      '2015-May-29',   10,    8,
      '2015-May-30',    6,    6,
      '2015-May-31',    3,    3,
      '2015-Jun-01',   14,   13,
      '2015-Jun-02',   21,   17,
      '2015-Jun-03',   26,   17,
      '2015-Jun-04',   14,    8,
      '2015-Jun-05',   25,   16,
      '2015-Jun-06',    3,    3,
      '2015-Jun-07',    6,    5,
      '2015-Jun-08',   26,   12,
      '2015-Jun-09',   20,   16,
      '2015-Jun-10',   37,   24,
      '2015-Jun-11',   15,   15,
      '2015-Jun-12',   15,   13,
      '2015-Jun-13',    3,    3,
      '2015-Jun-14',    7,    6,
      '2015-Jun-15',   21,   19,
      '2015-Jun-16',   34,   25,
      '2015-Jun-17',   15,   12,
      '2015-Jun-18',   22,   16,
      '2015-Jun-19',   12,   11,
      '2015-Jun-20',    7,    6,
      '2015-Jun-21',   13,    9,
      '2015-Jun-22',   26,   17,
      '2015-Jun-23',   43,   28,
      '2015-Jun-24',   36,   16,
      '2015-Jun-25',   29,   16,
      '2015-Jun-26',   12,   11,
      '2015-Jun-27',    4,    4,
      '2015-Jun-28',    2,    2,
      '2015-Jun-29',   16,   15,
      '2015-Jun-30',   35,   22,
      '2015-Jul-01',   45,   22,
      '2015-Jul-02',   32,   15,
      '2015-Jul-03',    9,    5,
      '2015-Jul-04',    7,    5,
      '2015-Jul-05',    4,    4,
      '2015-Jul-06',   43,   18,
      '2015-Jul-07',   44,   22,
      '2015-Jul-08',   20,   16,
      '2015-Jul-09',   35,   19,
      '2015-Jul-10',    9,    6,
      '2015-Jul-11',   10,   10,
      '2015-Jul-12',    2,    2,
      '2015-Jul-13',   38,   18,
      '2015-Jul-14',   26,   16,
      '2015-Jul-15',   19,   15,
      '2015-Jul-16',   56,   21,
      '2015-Jul-17',   24,   16,
      '2015-Jul-18',    4,    4,
      '2015-Jul-19',    1,    1,
      '2015-Jul-20',   26,   17,
      '2015-Jul-21',   40,   27,
      '2015-Jul-22',   36,   18,
      '2015-Jul-23',   16,   12,
      '2015-Jul-24',    9,    5,
      '2015-Jul-25',    5,    5,
      '2015-Jul-26',    8,    4,
      '2015-Jul-27',   16,   14,
      '2015-Jul-28',   12,   10,
      '2015-Jul-29',   29,   20,
      '2015-Jul-30',   18,   10,
      '2015-Jul-31',   16,   10,
      '2015-Aug-01',    4,    3,
      '2015-Aug-02',    4,    4,
      '2015-Aug-03',   17,   12,
      '2015-Aug-04',   19,   12,
      '2015-Aug-05',   24,   16,
      '2015-Aug-06',   17,   14,
      '2015-Aug-07',   12,   10,
      '2015-Aug-08',    6,    3,
      '2015-Aug-09',    6,    6,
      '2015-Aug-10',   15,   10,
      '2015-Aug-11',   39,   21,
      '2015-Aug-12',   24,   18,
      '2015-Aug-13',   20,   14,
      '2015-Aug-14',   40,   19,
      '2015-Aug-15',    5,    5,
      '2015-Aug-16',    3,    3,
      '2015-Aug-17',   19,   16,
      '2015-Aug-18',   26,   20,
      '2015-Aug-19',   52,   34,
      '2015-Aug-20',   45,   30,
      '2015-Aug-21',    9,    6,
      '2015-Aug-22',   15,   13,
      '2015-Aug-23',   13,    7,
      '2015-Aug-24',   26,   19,
      '2015-Aug-25',   39,   18,
      '2015-Aug-26',   28,   14,
      '2015-Aug-27',   18,   13,
      '2015-Aug-28',   29,   22,
      '2015-Aug-29',    9,    7,
      '2015-Aug-30',    5,    4,
      '2015-Aug-31',   30,   17,
      '2015-Sep-01',   32,   18,
      '2015-Sep-02',   30,   16,
      '2015-Sep-03',   27,   19,
      '2015-Sep-04',    8,    6,
      '2015-Sep-05',    7,    6,
      '2015-Sep-06',    9,    9,
      '2015-Sep-07',   11,    9,
      '2015-Sep-08',   19,   16,
      '2015-Sep-09',   19,   16,
      '2015-Sep-10',   32,   16,
      '2015-Sep-11',   71,   24,
      '2015-Sep-12',    7,    6,
      '2015-Sep-13',    4,    4,
      '2015-Sep-14',   57,   24,
      '2015-Sep-15',   22,   15,
      '2015-Sep-16',   29,   16,
      '2015-Sep-17',   63,   27,
      '2015-Sep-18',   36,   14,
      '2015-Sep-19',    6,    6,
      '2015-Sep-20',    6,    4,
      '2015-Sep-21',   56,   22,
      '2015-Sep-22',   62,   23,
      '2015-Sep-23',   52,   21,
      '2015-Sep-24',   51,   19,
      '2015-Sep-25',   41,   20,
      '2015-Sep-26',    9,    7,
      '2015-Sep-27',    7,    6,
      '2015-Sep-28',   21,   18,
      '2015-Sep-29',   38,   26,
      '2015-Sep-30',   25,   16,
      '2015-Oct-01',   28,   17,
      '2015-Oct-02',    7,    7,
      '2015-Oct-03',   11,    7,
      '2015-Oct-04',    4,    4,
      '2015-Oct-05',    3,    2, # We probably missed some data on Monday, Oct. 5.  Github switched to providing only 1 week of traffic data.
      '2015-Oct-06',   51,   19,
      '2015-Oct-07',   43,   23,
      '2015-Oct-08',   56,   16,
      '2015-Oct-09',   52,   23,
      '2015-Oct-10',   33,    9,
      '2015-Oct-11',    6,    5,
      '2015-Oct-12',   10,    6,
      '2015-Oct-13',   31,   15,
      '2015-Oct-14',   29,   16,
      '2015-Oct-15',   77,   21,
      '2015-Oct-16',   31,   18,
      '2015-Oct-17',   19,    6,
      '2015-Oct-18',    1,    1,
      '2015-Oct-19',   29,   17,
      '2015-Oct-20',  150,   25,
      '2015-Oct-21',   96,   23,
      '2015-Oct-22',   69,   22,
      '2015-Oct-23',   53,   36,
      '2015-Oct-24',   16,    5,
      '2015-Oct-25',    7,    6,
      '2015-Oct-26',   56,   21,
      '2015-Oct-27',   48,   17,
      '2015-Oct-28',   19,   10,
    ]

# Local Variables:
# python-indent: 2
# End: