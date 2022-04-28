def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email


w = 1
while w == 1:
    ask = input("Enter your email id, old domain, new domain :").split(",")
    print(replace_domain(ask[0], ask[1], ask[2]))

    ask_new = input("Do you want to change another mail id? type 'y' to continue.....! :").lower()
    if ask_new != "y":
        w += 1
