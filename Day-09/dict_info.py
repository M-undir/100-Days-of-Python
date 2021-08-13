
programming_dict = {"Bug": "An error in a program that prevents the program from running as expected.",
                    "Function": "A piece of code that you can easily call over."}


# for i in programming_dict:
#     print(i)
#     print(programming_dict[i])

# Nesting Lists and Dictionaries

# Nesting

# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

# Nesting a List in a Dict

# travel_log = {
#     "France": {'cities_visited': ["Paris", "Dijon", "Marseille"], "total_visits": 5},
#     "England": ["Manchester, Birmingham, Newcastle"]
# }

# Nesting a Dict in a Dict

# travel_log_v2 = {
#     "Yemen": {"Times_visited": 10, "cities_visited": ["Sana'a", "Adan"]}
#
# }

# print(travel_log["France"]["total_visits"])
# print(travel_log_v2["Yemen"]["Times_visited"])

# Nesting a Dict in a List#

# travel_log_v2 = [
#     {
#         "country": "Yemen",
#         "times_visited": 10,
#         "cities_visited": ["Sana'a", "Adan"]
#     },
#     {
#         "country": "Japan",
#         "times_visited": 0,
#         "cities_visited": ["Hokkaido", "Osaka"]
#     }
# ]
#
# print(travel_log_v2[0]["cities_visited"])

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# 🚨 Do NOT change the code above

#
# to be added to the travel_log. 👇


def add_new_country(country_visited, visits_made, cities_visited):
    new_country = {"country": country_visited, "visits" : visits_made, "cities": cities_visited}
    travel_log.append(new_country)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
