#ejemplo 1 funcion filter()
numbers=[1,2,3,4,5]
#en nueva lista new_numbers se almacenan numeros pares
new_numbers=list(filter(lambda x:x%2==0,numbers))
print(new_numbers)


#ejemplo 2 lista con diccionarios
matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

new=list(filter(lambda item:item["home_team_result"]=="Win",matches))

print(new)
print(len(new))
print(matches)
print(len(matches))

#Con filter no hay problema en modificar el estado original