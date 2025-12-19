def get_population(country_dict):
    population_dict = {
        '2022': int(country_dict['2022 Population']),
        '2020': int(country_dict['2020 Population']),
        '2015': int(country_dict['2015 Population']),
        '2010': int(country_dict['2010 Population']),
        '2000': int(country_dict['2000 Population']),
        '1990': int(country_dict['1990 Population']),
        '1980': int(country_dict['1980 Population']),
        '1970': int(country_dict['1970 Population'])
    }
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values

def population_by_country(data, country):
    result = list(filter(lambda item: item['Country/Territory'] == country, data))
    return result

def percentage_by_country(data):
    labels = []
    values = []

    for row in data: 
        country_name = row['Country/Territory']
        percentage = float(row['World Population Percentage'])
        labels.append(country_name)
        values.append(percentage)

    return labels, values
