http_status = 404

if http_status == 200 or http_status == 201:
    print("Request was successful.")
elif http_status == 404:
    print("Request failed: Resource not found.")
elif http_status == 500 or http_status == 502 or http_status == 503:
    print("Request failed: Internal server error.")
elif http_status == 403:
    print("Request failed: Forbidden.")
else:
    print("Request failed.")

match http_status:
    case 200 | 201:
        print("Request was successful.")
    case 404:
        print("Request failed: Resource not found.")
    case 500 | 502 | 503:
        print("Request failed: Internal server error.")
    case 403:
        print("Request failed: Forbidden.")
    case _:
        print("Request failed.")


