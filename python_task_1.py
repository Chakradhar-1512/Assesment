
import pandas as pd


def generate_car_matrix(df):
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    df = pd.pivot_table(df, values='car', index='id_1', columns='id_2', fill_value=0)
    return df


def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    cars = list(df["car"])
    new_column = []
    for i in cars:
        if i < 15 :
            new_column.append("low")
        elif i >15 and i <= 25 :
            new_column.append("medium")
        else:
            new_column.append("high")
    dict_car_type = {"low":new_column.count('low'), 'high':new_column.count('high'), 'medium':new_column.count('medium')}
    keys = list(dict_car_type)
    keys.sort()
    dict_result = {i:dict_car_type[i] for i in keys}
    dataframe['car_type'] = new_column
    return dict_result


def get_bus_indexes(df):
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    mean = df['bus'].mean()
    bus = df['bus']
    return_index = []
    c = 0
    for i in bus:
        if i > (2 * mean) :
            return_index.append(c)
        else:
            pass
        c+=1
    return return_index


def filter_routes(df):
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    truck = df['truck']
    route = df['route']
    return_list = []
    c = 0
    for i in truck:
        if i > 7 :
            return_list.append(route[c])
        else:
            pass
        c+=1
    return return_list


def multiply_matrix(matrix):
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    index = (matrix.index)
    for i in matrix.columns:
        for j in index:
            if (matrix[i].loc[j] > 20) :
                matrix[i].loc[j] *= 0.75
            else:
                matrix[i].loc[j] *= 1.25
    return matrix.round(1)



def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here

    return pd.Series()
