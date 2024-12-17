def create_bar_chart(temperatures):
  """
  Creates a bar chart of temperatures for given cities.

  Args:
    temperatures: A dictionary where keys are city names 
                  and values are their temperatures.

  Returns:
    None
  """

  cities = list(temperatures.keys())
  temperatures_values = list(map(lambda city: temperatures[city], cities))

  # Create a visual representation of the bar chart
  print("\nBar Chart:")
  max_temp = max(temperatures_values)
  for temp in temperatures_values:
    bars = "*" * int((temp / max_temp) * 20)  # Adjust scale as needed
    print(f"{bars} {temp:.1f}°C")

create_bar_chart({"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3})