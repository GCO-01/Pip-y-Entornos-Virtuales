import utils
import read_csv
import chart

#Solución con GPT
'''
def run():
    data = read_csv.read_csv('./app/data.csv')
    country = input('Type Country: ')
    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        labels, values = utils.percentage_by_country(data)
        chart.generate_bar_chart(labels, values)
        chart.generate_pie_chart(labels, values)
'''

#Solución Clase
def run():
    data = read_csv.read_csv('data.csv')
    #Se agrega un filtro por continente
    data = list(filter(lambda item: item['Continent'] == 'South America', data))

    countries = list(map(lambda x:x['Country/Territory'], data))
    percentages = list(map(lambda x:x['World Population Percentage'], data))
    chart.generate_pie_chart(countries, percentages)

    country = input('Type Country -> ')

    result = utils.population_by_country(data,country)

    if len(result) > 0: 
        country = result[0]
        labels, values = utils.get_population(country)
        chart.generate_bar_chart(country['Country/Territory'], labels, values)


if __name__ == '__main__':
    run()