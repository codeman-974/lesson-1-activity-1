import random
fname = ['John', 'Jane', 'Corey', 'Travis', 'Dave']
lname = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis']

street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park']
fake_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnydale', 'Bedrock' ]
states = ['AL', 'AK', 'AR', 'AZ', 'CA']

class Name:
    def __init__ (self, num=1):
        self.num = num

    def first_name (self):
        for i in range (self.num):
            last = random.choice(lname)
            print(last)

    def full_name (self):
        for i in range (self.num):
            first = random.choice(fname)
            last = random.choice(lname) 
            print (f'{first}{last}')

    def full_profile (self):
        for i in range (self.num):
            first = random.choice(fname)
            last = random.choice(lname) 
            phone = f'+91-{random.randint(800, 999)} {random.randint(800, 999)} {random.randint(1000, 9999)}'       