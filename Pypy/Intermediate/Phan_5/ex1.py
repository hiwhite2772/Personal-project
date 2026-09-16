import requests

res = requests.get("https://jsonplaceholder.typicode.com/users")

user = res.json()

def information(user):
    max_name = max(len(u['name']) for u in user)
    for i in range(len(user)):
        n = user[i]['name']
        m = user[i]['address']['city']
        print(f"{n:<{max_name+1}} - {m:<10}")

# information(user)

def company_name(user):
    username = [u['name'] for u in user]
    loc_company = [u['company']['name'] for u in user if "Group" in u['company']['name']]
    for i, (a, b) in enumerate(zip(username, loc_company)):
        print(f"{i+1:<3} | {a:^15} | {b:<10}")

# company_name(user)

def sort_name(user):
    n = [(u['name'].split()) for u in user]
    
    for i in range(len(n)):
        for j in range(len(n)): 
            if n[j][-1] > n[j-1][-1]:
                n[j-1][-1] = n[j][-1]
            n[i][-1], n[j-1][-1] = n[j-1][-1], n[i][-1]
    # print(sorted(u['name'] for u in user))
        print(n[i])

sort_name(user)