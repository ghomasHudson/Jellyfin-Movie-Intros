import requests

def find_movie(server_url, user_id, title, year=None, headers=None):
    params = {
        "searchTerm": title,
        "includeItemTypes": "Movie",
        "Recursive": "true",
        "enableTotalRecordCount": "false",
        "enableImages": "false",
    }
    if year is not None:
        params["years"] = year
    while True:
        try:
            res = requests.get(f'{server_url}/Users/{user_id}/Items',headers=headers, params=params)
            if len(res.json()["Items"]) > 0:
                return res.json()["Items"][0]
            else:
                return None
        except:
            return find_movie(server_url, user_id, search_str, movie_year, headers=headers)
