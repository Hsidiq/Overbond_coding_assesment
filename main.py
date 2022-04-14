import matplotlib
import matplotlib.pyplot as plt
import numpy as np

"""
Converts date string YYYYMMDD to the format 'YYYY-<month name>-DD'
"""


def date_converter(ds):
    year = ds[0:4]
    m = ds[4:6]
    month = ""
    day = ds[6:]

    if m == "01":
        month = "Jan"
    if m == "02":
        month = "Feb"
    if m == "03":
        month = "Mar"
    if m == "04":
        month = "Apr"
    if m == "05":
        month = "May"
    if m == "06":
        month = "Jun"
    if m == "07":
        month = "Jul"
    if m == "08":
        month = "Aug"
    if m == "09":
        month = "Sep"
    if m == "10":
        month = "Oct"
    if m == "11":
        month = "Nov"
    if m == "12":
        month = "Dec"

    return year + "-" + month + "-" + day


"""
Identifies date value in raw data using prefix tag 'DIs'

"""


def find_date(s):
    if ";DIs" in s:
        new = s.split(";DIs")
        final = new[1].split(";")
        return date_converter(final[0])

    return None


"""

Identifies CleanBid numerical value using prefix tag 'BPr'

"""


def find_clean_bid(s):
    if ";BPr" in s:
        new = s.split(";DIs")
        final = new[1].split(";")
        return float(final[0])

    return None


"""

Identifies CleanBid numerical value using prefix tag 'APl'

"""


def find_clean_ask(s):
    if ";APl" in s:
        new = s.split(";APl")
        final = new[1].split(";")
        return float(final[0])

    return None


"""

Identifies CleanBid numerical value using prefix tag 'Pl'

"""


def find_last_price(s):
    if ";Pl" in s:
        new = s.split(";Pl")
        final = new[1].split(";")
        return float(final[0])

    return None


"""
This function essentially creates and populates a dictionary containing 
keys as issuance dates and values as dictionaries where each key here is
either CleanBid, CleanAsk or Last Price and values as the respective numerical
values for each key.

return value is the aforementioned dictionary itself

"""


def create_dict():
    i = 1
    curr = ""
    lis = []
    d = {}

    with open('data.txt') as f:
        lines = f.readlines()

    for line in lines:
        if (i % 10) == 0:
            curr += line
            date_key = find_date(curr)
            cb = find_clean_bid(curr)
            ca = find_clean_ask(curr)
            lp = find_last_price(curr)

            if date_key is not None:
                d[date_key] = {}
                if cb is not None:
                    d[date_key]["CleanBid"] = find_clean_bid(curr)

                if ca is not None:
                    d[date_key]["CleanAsk"] = find_clean_ask(curr)

                if lp is not None:
                    d[date_key]["Last Price"] = find_last_price(curr)

            curr = ""

        curr += line
        i += 1

    return d


"""
The function creates x axis and y axis points where x axis points are
the issuance dates and the y axis points are all the numerical values
each of which are either CleanBid, CleanAsk or Last Price. With the axis
points, a scatter graph is created and shown with each of the aforementioned
three having different colored points.

"""


def create_plot():
    d = create_dict()
    x_points = list(d.keys())
    y_points = []
    indices = []
    for dic in list(d.values()):
        y_points.append(list(dic.values()))
    for name in list(d.keys()):
        if name == "CleanBid":
            indices.append(0)
        if name == "CleanAsk":
            indices.append(1)
        if name == "Last Price":
            indices.append(2)
    x = np.array(x_points, dtype=object)
    y = np.array(y_points, dtype=object)
    colors = ["blue", "orange", "gray"]
    colmap = matplotlib.colors.ListedColormap(colors)

    plt.scatter(x, y, c=indices, cmap=colmap)
    plt.show()

    return None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_plot()
