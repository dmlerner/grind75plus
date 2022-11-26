# https://leetcode.com/problems/accounts-merge/
# but two twenty nine for almost working and slow
# three oh four to make it alrightly fast
# two eighteen - three oh one

from david import show
from collections import defaultdict


def merge_accounts(accounts):
    # account is [str] [name, *emails]
    neighbors_by_email = defaultdict(set)
    name_by_email = {}
    for name, *emails in accounts:
        for email in emails:
            name_by_email[email] = name
        for email1, email2 in zip(emails, emails[1:]):
            neighbors_by_email[email1].add(email2)
            neighbors_by_email[email2].add(email1)

    # print(f'{neighbors_by_email=}')
    # @show
    def get_account(email):
        name = name_by_email[email]
        account = ["", email]
        seen = set([email])

        # @show
        def dfs(email):
            for neighbor in neighbors_by_email[email]:
                # print('neighbor', neighbor)
                if neighbor not in seen:
                    seen.add(neighbor)
                    account.append(neighbor)
                    dfs(neighbor)

        dfs(email)
        account.sort()
        account[0] = name
        return account

    sorted_accounts = []
    seen_emails = set()
    for email, name in name_by_email.items():
        if email in seen_emails:
            continue
        # for name, email, *_ in accounts:
        name, *emails = account = get_account(email)
        if any(map(lambda email: email not in seen_emails, emails)):
            sorted_accounts.append(account)
            seen_emails.update(set(emails))
        # for email in emails:
        #     seen_emails.add(email)
        if len(seen_emails) == len(name_by_email):
            break
    return sorted_accounts


# accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
accounts = [
    ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
    # ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
    # ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
    # ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
    # ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"],
]
expected = [
    # ["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"],
    ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
    # ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"],
    # ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"],
    # ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"],
]
actual = merge_accounts(accounts)
print(*map(len, (accounts, expected, actual)))
for i in expected:
    if i not in actual:
        print("missing")
        print(i)
        print()
for i in actual:
    if i not in expected:
        print("unexpected")
        print(i)
        print()
print(*expected, sep='\n')
print()
print(*actual, sep='\n')
assert expected == actual
