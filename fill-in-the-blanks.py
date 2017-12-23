# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?


#defining the paragraphs and their solution per each diffculty level

difficult_sample = '''___3___ based on automatically ___1___ the rules can be made more accurate simply 
by supplying more input ___2___. However, ___3___ based on hand-written rules can only be made more accurate 
by increasing the complexity of the rules, which is a much more difficult task. In particular, there is a 
limit to the complexity of ___3___ based on hand-crafted rules, beyond which the ___3___ become more and 
more unmanageable. .'''

normal_sample = '''There are two different phases of ___2___ ___1___: how an ___2___ ___3___ relies on 
planning and control, localization, and  feature vectors to get from a starting location to a destination. 
Two examples: an ___2___ ___3___ trial in Singapore and the potential impact of driverless taxis in 
New York City. Parallel autonomy is when a ___1___ corrects a driver's errors by making small adjustments, 
such as turning the wheel to ensure safety. '''

easy_sample = '''Artificial ___1___ (___2___, also ___3___ ___1___, is ___1___ displayed by ___3___s, in 
contrast with the natural ___1___ displayed by humans and other animals. In computer science ___2___ research 
is defined as the study of "intelligent agents": any device that perceives its environment and 
takes actions that maximize its chance of success at some goal.'''

difficult_sample_result = ["systems", "learning", "data"]
normal_sample_result = ["systems", "autonomous", "vehicle"]
easy_sample_result = ["intelligence", "AI", "machine"]

#the player chooses the level of difficulty 
level_of_difficulty = raw_input("Choose and type easy, normal or difficult")

def sample(level_of_difficulty):
	if level_of_difficulty == difficult:
		return difficult_sample
		if level_of_difficulty == normal:
			return normal_sample
		else: 
			return easy_sample

def sample_result(level_of_difficulty):
	if level_of_difficulty == difficult:
		return difficult_sample_result
		if level_of_difficulty == normal:
			return normal_sample_result
		else: 
			return easy_sample_result
print sample_result

# How many blanks have to be filled and defining a vector with the words in the blanks to be replaced. Assuming only one word per blank.		
list_of_words = sample.split(",")
blank = []
number_of_blanks = 0
index=0

while index<len(list_of_words):
	if list_of_words[index] in ["___1___" ,"___2___", "___3___", "___4___"]:
		blank = blank.append (list_of_words [index]) 
		number_of_blanks = number_of_blanks + 1
	index=index+1

#Replacing the words in the blanks for the answers  

def word_in_pos(word,blank):
	for pos in blank:
		if pos in word:
			return pos
	return None

def play_game(sample,blank):
	replaced = []
	list_of_words = sample.split()
	for word in list_of_words:
		replacement = word_in_pos(word,blank)
		if replacement  != None:
			user_input = raw_input ("Type in your fill-the-blabk word" + replacement + " ")
			if sample_result == user_input:
				word = word.replace(replacement, user_input)
				replaced.append(word)
		else:
			replaced.append(word)
	replaced=" ".join(replaced)
	return replaced




# Creating a vector with the player responses
#player_response = []
#filled_blanks = []
#n = 1
#while n<number_of_blanks:
#	filled_blanks [n] = raw_input ("Write your word here: ")
#	player_response [] = player_response.append (filled_blanks[n])
##and modifying list created from sample
#	if sample_result[] == player_response[]:
#		list_of_words[n[n][1]]= player_response[n]
#finalparagraph = "".join(list_of_words)













