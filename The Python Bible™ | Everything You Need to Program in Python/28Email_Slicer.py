# Get user email address
email = input("What is your email address?: ").strip()

# Slice out username
user = email[:email.index("@")]

# Slice out domain name
domain = email[email.index("@") + 1:]

# Format output message
output = "Your username is {} and your domain name is {}".format(user, domain)

# Display output message
print(output)
