from random import shuffle
import time

def personality(choices):
	question_list =[Question("I like to work on many tasks at the same time instead of focusing on one.", "mb", "Disagree", "Agree", 0, "Introvert", "Extrovert"),
					Question("I tend to discuss big decisions with most of my friends.", "mb", "Disagree", "Agree", 0, "Introvert", "Extrovert"),
					Question("I prefer to take some alone time for myself when I can get it.", "mb", "Disagree", "Agree", 0, "Extrovert", "Introvert"),
					Question("At a party, I'd prefer to talk to one close friend rather than a crowd.", "mb", "Disagree", "Agree", 0, "Extrovert", "Introvert"),
					Question("In my free time, I'd choose to go meet with a social group over staying home.", "mb", "Disagree", "Agree", 0, "Introvert", "Extrovert"),
					Question("I like to think through things myself rather than bounce ideas off of lots of people.", "mb", "Disagree", "Agree", 0, "Extrovert", "Introvert"),

					Question("When approaching a new project, I like to see the big picture before considering the details.", "mb", "Disagree", "Agree", 0, "Sensing", "Intuition"),
					Question("I think it's fun to think through a lot different possibilities rather than focus on a single opportunity.", "mb", "Disagree", "Agree", 0, "Sensing", "Intuition"),
					Question("If I'm dealing with a situation I've encountered before, I'd rather just handle it the same way as last time instead of wasting time thining of new solutions.", "mb", "Disagree", "Agree", 0, "Intuition", "Sensing"),
					Question("I notice small details easily.", "mb", "Disagree", "Agree", 0, "Intuition", "Sensing"),
					Question("I'd rather focus on the reality of a situation than play through the possibilities of what could be.", "mb", "Disagree", "Agree", 0, "Intuition", "Sensing"),
					Question("When playing a new game, I usually pick up on the rules pretty quickly just from playing.", "mb", "Disagree", "Agree", 0, "Sensing", "Intuition"),

					Question("I usually understand how people are feeling without having to ask.", "mb", "Disagree", "Agree", 0, "Thinking", "Feeling"),
					Question("I prefer to follow the rules, even when it can adversely affect me.", "mb", "Disagree", "Agree", 0, "Feeling", "Thinking"),
					Question("I tend to trust my head over my heart.", "mb", "Disagree", "Agree", 0, "Feeling", "Thinking"),
					Question("When making a large decision, I make a point of considering how it will affect those around me.", "mb", "Disagree", "Agree", 0, "Thinking", "Feeling"),
					Question("I'd rather make the right choice and hurt someone's feelings a little than make the wrong choice.", "mb", "Disagree", "Agree", 0, "Feeling", "Thinking"),
					Question("I'd rather play a game with my close friends where we all work together than compete to have a winner and losers.", "mb", "Disagree", "Agree", 0, "Thinking", "Feeling"),

					Question("I'd rather have an agenda before agreeing to a trip with coworkers or friends.", "mb", "Disagree", "Agree", 0, "Perceiving", "Judging"),
					Question("I like to leave my schedule open in case something I want to do comes up.", "mb", "Disagree", "Agree", 0, "Judging", "Perceiving"),
					Question("When building something, I try it myself before looking at the included instructions.", "mb", "Disagree", "Agree", 0, "Judging", "Perceiving"),
					Question("I'd rather turn in work on time, even if it's not my best.", "mb", "Disagree", "Agree", 0, "Perceiving", "Judging"),
					Question("I think games can only fun if people play by the rules.", "mb", "Disagree", "Agree", 0, "Perceiving", "Judging"),
					Question("If I'm on my way to dinner at a restaurant I know and see one that my friends have said they love, I'll go there instead of where I planned to go.", "mb", "Disagree", "Agree", 0, "Judging", "Perceiving")]

	answers = []
	results = {"Introvert" : 0, "Extrovert" : 0, "Intuition" : 0, "Sensing" : 0, "Thinking" : 0, "Feeling" : 0, "Judging" : 0, "Perceiving" : 0}
	symbols = {"Introvert" : 'I', "Extrovert" : 'E', "Intuition" : 'N', "Sensing" : 'S', "Thinking" : 'T', "Feeling" : 'F', "Judging" : 'J', "Perceiving" : 'P'}
	types = ['Introvert', 'Extrovert', 'Intuition', 'Sensing', 'Thinking', 'Feeling', 'Judging', 'Perceiving']
	personality_type = {}
	personality_code = ''
	scale = 7

	if choices != None and len(choices) == len(question_list):
		for x in range(len(choices)):
			question_list[x].set_value((choices[x]-1)*(100/(scale-1)))

	else:
		# Shuffle questions
		# shuffle(question_list)

		# Ask each question and record the answer in the question
		for question in question_list:
			print('')
			print(question.get_question())
			print(question.get_left() + '  ' + (''.join(str(x) + '  ' for x in range(1, scale+1))) + question.get_right())
			ans = 0
			while ans == 0:
				choice = input('Choice: ')
				try:
					choice = int(choice)
					ans = 1
				except:
					if choice == 'q':
						print('Have a nice day.')
						return False
					print('Please input a valid response')
					print('')

			print('')
			question.set_value((choice-1)*(100/(scale-1)))
			answers.append(choice)


	# Calculate the percentages for each of the 8 types
	# If the value was greater than 50% use the right trait
	# If it was less, subtract from 100 then use left trait
	# If it was equal to 50%, add 50% to both traits
	for question in question_list:
		value = 0
		if question.value > 50:
			trait = question.right_trait
			value = question.value
			results[trait] += value
			results[question.left_trait] += (100-value)
		elif question.value < 50:
			trait = question.left_trait
			value = 100 - question.value
			results[trait] += value
			results[question.right_trait] += (100-value)
		else:
			trait = str(question.left_trait + " and " + question.right_trait)
			value = 50
			results[question.left_trait] += value
			results[question.right_trait] += value

	# These are the raw score results for each of the categories
	# print(results)

	# Calculate the percentage scores for each of the 8 categories
	for key in results:
		results[key] = results[key]/(len(question_list)/4)

	# Combine the relevant categories into a final set of scores
	i = 0
	while i < 8:
		if results[types[i]] > results[types[i+1]]:
			personality_type[types[i]] = str(results[types[i]]) + '%'
			personality_code = personality_code + symbols[types[i]]
		elif results[types[i+1]] > results[types[i]]:
			personality_type[types[i+1]] = str(results[types[i+1]]) + '%'
			personality_code = personality_code + symbols[types[i+1]]
		else:
			personality_type[str(types[i] + ' ' + types[i+1])] = '50%'
		i += 2

	# Pretend to be calculating :)
	for x in range(50):
		print_progress(x, 50, 'Calculating your results: ')
		time.sleep(.1)


	# Print the individual's results
	print('')
	print('Your Meyers-Briggs personality type is: ' + personality_code)
	print('')
	print('Here are your detailed results: ')
	for key in personality_type:
		print(key + ': ' + personality_type[key])

	print('')
	print('Your choices were: ' + str(answers))

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
    percents = str_format.format(100 * (iteration / float(total)))
    filled_length = int(round(bar_length * iteration / float(total)))
    bar = '█' * filled_length + '-' * (bar_length - filled_length)

    print('\r%s |%s| %s%% %s' % (prefix, bar, percents, suffix), end = '\r'),

    if iteration > total:
        print('\n')

class Question():

	def __init__(self, question, q_type, left_attr, right_attr, value, left_trait, right_trait):
		self.question = str(question)
		self.q_type = q_type
		self.left_attr = str(left_attr)
		self.right_attr = str(right_attr)
		self.value = str(value)
		self.left_trait = left_trait
		self.right_trait = right_trait

	def get_question(self):
		return str(self.question)

	def get_type(self):
		return str(self.q_type)

	def get_left(self):
		return self.left_attr

	def get_right(self):
		return self.right_attr

	def set_value(self, value):
		self.value = value

	def get_value(self):
		return str(self.value) + "%"

	def print(self):
		# TODO
		pass


mrl1_5 = [2, 2, 4, 5, 3, 4, 5, 5, 2, 1, 2, 4, 5, 3, 4, 5, 2, 4, 2, 4, 5, 2, 3, 5]
mrl    = [2, 3, 6, 7, 3, 6, 6, 7, 2, 2, 2, 6, 7, 3, 4, 6, 3, 3, 2, 6, 7, 2, 5, 6]
cozza  = [4, 6, 7, 6, 2, 5, 7, 6, 5, 7, 3, 7, 6, 3, 6, 6, 7, 2, 1, 7, 6, 3, 4, 4]
mal    = [6, 7, 1, 3, 7, 2, 7, 6, 2, 3, 5, 6, 7, 5, 2, 6, 2, 2, 6, 2, 5, 7, 7, 4]
d      = [4, 7, 5, 5, 2, 5, 2, 6, 2, 6, 2, 7, 5, 6, 5, 6, 1, 3, 4, 6, 3, 2, 7, 6]

personality(mrl)
