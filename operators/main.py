# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
# Spain info!
spain_language = 'Spanish'
spain_religion = 'Roman Catholic'
spain_capital_len = len('Madrid')
spain_gdp = 1393351000000
spain_population = 47222613
spain_population_growth = 0.12

# Switzerland info!
switzerland_language = 'German'
switzerland_religion = 'Roman Catholic'
switzerland_capital_len = len('Bern')
switzerland_gdp = 731502000000
switzerland_population = 8563760
switzerland_population_growth = 0.64

# Spain vs Switzerland
print(spain_language == switzerland_language)
print(spain_religion == switzerland_religion)
print(spain_capital_len != switzerland_capital_len)
print(switzerland_gdp > spain_gdp)
print(spain_population_growth < 1 and switzerland_population_growth < 1)
print(spain_population > 10000000 or switzerland_population > 10000000)
print((spain_population > 10000000) != (switzerland_population > 10000000))
