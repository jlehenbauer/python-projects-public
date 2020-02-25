import random
import math
def thanos():
	"""

	"""
	while True:
		try:
			population = int(input('What population shall be snapped? '))
			break
		except:
			print('Please enter a valid (whole number) population.\n')
			pass
	superheroes = [random.randint(0, population) for x in range(0, int(population*.0000025))]
	people = []
	killed = []

	becca = Person('North American', 18, 'Female', 'Becca')
	jonah = Person('North American', 14, 'Male', 'Jonah')
	kate = Person('North American', 15, 'Female', 'Kate')
	liam = Person('North American', 15, 'Male', 'Liam')
	owen = Person('North American', 16, 'Male', 'Owen')
	alden = Person('North American', 16, 'Male', 'Alden')
	leah = Person('North American', 17, 'Female', 'Leah')
	henry = Person('North American', 16, 'Male', 'Henry')
	danny = Person('North American', 14, 'Male', 'Danny')
	austen = Person('North American', 15, 'Male', 'Austen')

	students = [becca, jonah, kate, liam, owen, alden, leah, henry, danny, austen]

	generator = random.SystemRandom()

	continents = ['North American', 'South American', 'African', 'European', 'Asian', 'Australian']
	age = [x for x in range(0, 120)]
	sex = ['Male', 'Female']

	pop_by_cont = [[] for x in range(len(continents))]
	pop_by_age = [[] for x in range(len(age))]
	pop_by_sex = [[] for x in range(len(sex))]

	while len(people) < population:
		people.append(Person(
				continents[generator.randrange(len(continents))],
				age[generator.randrange(len(age))],
		 		sex[generator.randrange(len(sex))]))
		pop_by_cont[continents.index(people[-1].continent)].append(people[-1])
		pop_by_age[age.index(people[-1].age)].append(people[-1])
		pop_by_sex[sex.index(people[-1].sex)].append(people[-1])
		if(len(people) in superheroes):
			people[-1].superhero = True
		print_progress(len(people), population, 'Generating population: ')

	for student in students:
		position = generator.randrange(len(people))
		pop_by_cont[continents.index(people[position].continent)].remove(people[position])
		pop_by_age[age.index(people[position].age)].remove(people[position])
		pop_by_sex[sex.index(people[position].sex)].remove(people[position])
		people[position] = student	
		pop_by_cont[continents.index(student.continent)].append(student)
		pop_by_age[age.index(student.age)].append(student)
		pop_by_sex[sex.index(student.sex)].append(student)

	'''
	kill_this_many = population//2
	while len(set(killed)) < kill_this_many:
		killed.append(random.randint(0, population))
		print_progress(len(set(killed)), kill_this_many, 'Deciding who should be killed: ')

	killed = list(set(killed))

	for i in killed:
		people[i].killed = True
		print_progress(i, population, 'Performing snap: ')
	'''
	for i in range(population//2):
		people[i].killed = True
		print_progress(i, population//2, 'Performing snap: ')


	print(str(len(killed)) + ' beings have been killed\n')

	print_people(people)
		
	continent_analysis(pop_by_cont, continents)
	age_analysis(pop_by_age, age)
	sex_analysis(pop_by_sex, sex)
	superhero_analysis(people, superheroes)
	student_analysis(students)


def print_people(people):
	col = 0
	for person in people:
		print(str(person.dead()) + ' ', end='')
		col += 1
		if col >= math.sqrt(len(people)):
			col = 0
			print()

def student_analysis(students):
	for student in students:
		if student.killed:
			print(str(student.name) + ' has been killed.')

def superhero_analysis(people, superheroes):
	if len(superheroes) == 0:
		print('No superheroes existed to be killed.')
		return 0

	kill_count = 0

	for superhero in superheroes:
		if people[superhero].killed:
			kill_count += 1

	print(str(kill_count) + ' superheroes have been killed. Only ' + str(int(kill_count/len(superheroes)*100)) + '% remain.')
	
	return kill_count

def continent_analysis(people, continents):
	killed_by_continent = {x:0 for x in continents}

	for continent in people:
		for person in continent:
			if person.killed:
				killed_by_continent[person.continent] += 1

	for key in killed_by_continent.keys():
		print(str(int(killed_by_continent[key]/len(people[continents.index(key)])*100)) + '% of ' + str(key) + 's have been killed.')
	
	print()

	return killed_by_continent

def age_analysis(people, ages):
	age_ranges = [0, 18, 25, 45, 65, 85, max(ages)]
	stat_dict = {x:0 for x in age_ranges}
	killed_by_age = {x:0 for x in age_ranges}

	i = 0
	a_range = age_ranges[i]
	for age in range(len(people)):
		if age > a_range:
			i += 1
			a_range = age_ranges[i]
		if people[age] != []:
			for person in people[age]:
				stat_dict[a_range] += 1
				if person.killed:
					killed_by_age[a_range] += 1

	for key in range(1, len(age_ranges)):
		print(str(int(killed_by_age[age_ranges[key]]/stat_dict[age_ranges[key]]*100)) + '% of ' + str(age_ranges[key-1]) + ' to ' + str(age_ranges[key]) + ' year olds have been killed.')
	
	print()

	return stat_dict

def sex_analysis(people, sexes):
	stat_dict = {x:0 for x in sexes}

	for demographic in people:
		for person in demographic:
			if person.killed:
				stat_dict[person.sex] += 1

	print(str(int(stat_dict['Male']/len(people[0])*100)) + '% of all males died.')
	print(str(int(stat_dict['Female']/len(people[1])*100)) + '% of all females died.')
	
	print()

	return stat_dict

# Print iterations progress
# Obtained from https://gist.github.com/aubricus/f91fb55dc6ba5557fbab06119420dd6a
def print_progress(iteration, total, prefix='', suffix='', decimals=1, bar_length=50):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        bar_length  - Optional  : character length of bar (Int)
    """
    str_format = "{0:." + str(decimals) + "f}"
    percents = str_format.format(50 * (iteration / float(total)))
    filled_length = int(round(bar_length * iteration / float(total)))
    bar = '█' * filled_length + '-' * (bar_length - filled_length)

    print('\r%s |%s| %s%% %s' % (prefix, bar, filled_length, suffix), end = '\r'),

    if iteration == total:
        print('\n')

class Person(object):
	"""Represents a person in the population to be killed by Thanos."""
	def __init__(self, continent, age, sex, name = None):
		super(Person, self).__init__()
		self.continent = continent
		self.age = age
		self.sex = sex
		self.killed = False
		self.superhero = False
		if name is not None:
			self.name = name

	def dead(self):
		return '░' if self.killed else '█'
		
	def __str__(self):
		return str(self.age) + ' year old ' + str(self.continent) + ' ' +str(self.sex)

thanos()