from exa_py import Exa

# the api key to be generated from the exa dashboard
exa = Exa('YOUR_API_KEY_HERE')

# takes input from user and store in search_query
search_query = input('What do you want to search: ')
print()

# search method to search for the query
response = exa.search(
    search_query,
    num_results=3,
    type='keyword',
    include_domains=['https://youtube.com'],
)

# print only Title and link to video
for data in response.results:
    print(f"Title: {data.title}")
    print(f"URL: {data.url}\n")

# search results unfiltered
# print(response)
