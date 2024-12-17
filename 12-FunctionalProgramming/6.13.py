def create_bar_chart(medal_data):
  """
  Creates a bar chart of total medals won by each country.

  Args:
    medal_data: A list of dictionaries, where each dictionary 
                represents a country's medal count.

  Returns:
    None
  """

  countries = list(map(lambda x: x["country"], medal_data))
  total_medals = list(map(lambda x: x["gold"] + x["silver"] + x["bronze"], medal_data))

  # Create a visual representation of the bar chart
  print("\nBar Chart of Total Medals Won")
  max_medals = max(total_medals)
  for country, medals in zip(countries, total_medals):
    bars = "*" * int((medals / max_medals) * 20)  # Adjust scale as needed
    print(f"{country}: {bars} ({medals})")

# Sample medal data
medal_data = [
    {"country": "Denmark", "gold": 2, "silver": 4, "bronze": 6},
    {"country": "Finland", "gold": 5, "silver": 0, "bronze": 4},
    {"country": "USA", "gold": 12, "silver": 5, "bronze": 11},
    {"country": "Peru", "gold": 0, "silver": 1, "bronze": 7}
]

create_bar_chart(medal_data)