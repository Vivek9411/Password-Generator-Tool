from random import randint, choice, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nr_letters = 6
nr_numbers = 3
nr_symbols = 3



class PasswordGenerator:
    def __init__(self):
        self.password_list = []
        self.password = ""
        self.generate_password()



    def generate_password(self):
        for n in range(0, nr_letters):
            self.password_list.append(choice(letters))

        for n in range(0, nr_numbers):
            self.password_list.append(choice(numbers))

        for n in range(0, nr_symbols):
            self.password_list.append(choice(symbols))


        shuffle(self.password_list)
        self.password = "".join(self.password_list)
        # for n in range(0, len(self.password_list)):
        #     char_ = random.choice(self.password_list)
        #     self.password += char_
        #     self.password_list.remove(char_)


