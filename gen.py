import random
import secrets

# Define usable characters
alpha = "abcdefghjkmnpqrstuvwxyz"
# Excluded the characters: ijlo
ALPHA = "ABCDEFGHJKMNPQRSTUVWXYZ"
# Excluded the characters: IJLO
NUM = "0123456789"
SYM = "@#$&"

# Combine all usable characters into one variable
chars = "".join([alpha, ALPHA, NUM, SYM])

# Randomly select at least one character from each character set defined above
rand_alpha = secrets.choice(alpha)
rand_ALPHA = secrets.choice(ALPHA)
rand_NUM = secrets.choice(NUM)
rand_SYM = "".join(secrets.choice(SYM) for i in range(2))

# Set the first_char variable to a random lowercase letter
first_char = secrets.choice(alpha)

# Combine the randomly selected characters from above
temp_pass = rand_alpha + rand_ALPHA + rand_NUM + rand_SYM

# At this stage, the password only contains 5 characters (alpha, ALPHA, & NUM x1, plus SYM x2),
# but we want X amount (length defined by user) of characters in the password

# Prompt user for the desired length (with 18 being the default) of the password
PWD_LEN = int(input("Length (default: 18) of the password? ") or "18")

# Now that we have a randomly selected lowercase letter for the first character (first_char)
# and at least one character from each set of characters, we fill in the remaining length of the
# password with a random collection of characters from the combined list (i.e., chars)
for i in range(PWD_LEN - 6):
	temp_pass = temp_pass + secrets.choice(chars)

# Next, we need to convert the "temp_pass" string to a list of characters,
# so that we can shuffle the list of characters
temp_list = list(temp_pass)
random.shuffle(temp_list)

# Create the "password" variable, which contains the "first_char" and the shuffled list of characters (temp_list)
password = first_char + "".join(temp_list)

print(password)
