import random
import string

# password generation application
class PasswordGenerator:
    def __init__(self, length, use_uppercase, use_lowercase, use_digits, use_special):
        self.length = length
        self.use_uppercase = use_uppercase
        self.use_lowercase = use_lowercase
        self.use_digits = use_digits
        self.use_special = use_special

    def generate_password(self):
        characters = ''
        if self.use_uppercase:
            characters += string.ascii_uppercase
        if self.use_lowercase:
            characters += string.ascii_lowercase
        if self.use_digits:
            characters += string.digits
        if self.use_special:
            characters += string.punctuation

        if not characters:
            raise ValueError("At least one character type must be selected.")


        password_chars = []
        if self.use_uppercase:
            password_chars.append(random.choice(string.ascii_uppercase))
        if self.use_lowercase:
            password_chars.append(random.choice(string.ascii_lowercase))
        if self.use_digits:
            password_chars.append(random.choice(string.digits))
        if self.use_special:
            password_chars.append(random.choice(string.punctuation))


        while len(password_chars) < self.length:
            password_chars.append(random.choice(characters))

        random.shuffle(password_chars)
        return ''.join(password_chars)

    def generate_variation(self, original_password):

        characters = ''
        if self.use_uppercase:
            characters += string.ascii_uppercase
        if self.use_lowercase:
            characters += string.ascii_lowercase
        if self.use_digits:
            characters += string.digits
        if self.use_special:
            characters += string.punctuation


        variation = []
        for char in original_password:
            if random.choice([True, False]):

                new_char = random.choice(characters)
                variation.append(new_char)
            else:
                variation.append(char)

        return ''.join(variation)


def main():
    print("Welcome to the Enhanced Password Generator!")


    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    try:
        generator = PasswordGenerator(length, use_uppercase, use_lowercase, use_digits, use_special)


        password = generator.generate_password()
        print(f"Generated password: {password}")


        if input("Do you want to generate a variation of an existing password? (y/n): ").lower() == 'y':
            original_password = input("Enter the original password: ")
            variation = generator.generate_variation(original_password)
            print(f"Generated variation: {variation}")

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
