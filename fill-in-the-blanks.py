# IPND Stage 2 Final Project

#defining the paragraphs and their solution per each diffculty level

difficult_sample = '''___1___ based on automatically ___2___ the rules can be more accurate simply by 
supplying more input ___3___ . However, ___1___ based on hand-written rules can only be made more accurate 
by increasing the complexity of the rules, which is a much more difficult task. In particular, there is a 
limit to the complexity of ___1___ based on hand-crafted rules, beyond which the ___1___ become more and 
more unmanageable. .'''

normal_sample = '''There are two different phases of ___1___ ___2___ : how an ___1___ ___3___ relies on 
planning and control, localization, and  feature vectors to get from a starting location to a destination. 
Two examples: an ___1___ ___3___ trial in Singapore and the potential impact of driverless taxis in 
New York  City. Parallel autonomy is when a ___2___ corrects a driver´s errors by making small adjustments,        
such as turning the wheeel to ensure safety. '''

easy_sample = '''Artificial ___1___ (___2___, also ___3___ ___1___, is ___1___ displayed by ___3___s, in 
contrast with the natural ___1___ displayed by humans and other animals. In computer science ___2___ research 
is defined  as the study of "intelligent agents": any device that perceives its environment and 
takes actions that maximize its chance of success at some goal.'''

difficult_sample_result = ["systems", "learning", "data"]
normal_sample_result = ["autonomous", "systems", "vehicle"]
easy_sample_result = ["intelligence", "AI", "machine"]

#the player chooses the level of difficulty 

level_of_difficulty = raw_input("Type difficulty level: easy, normal or difficult:")

if level_of_difficulty == "difficult":
	sample = difficult_sample
if level_of_difficulty == "normal":
	sample = normal_sample
if level_of_difficulty == "easy": 
	sample = easy_sample

if level_of_difficulty == "difficult":
	sample_result = difficult_sample_result
if level_of_difficulty == "normal":
	sample_result = normal_sample_result
if level_of_difficulty == "easy":
	sample_result = easy_sample_result

print
print "The paragraph where you have to fill the blanks is"
print
print sample

# How many blanks have to be filled and defining a vector (blank) with the words in the blanks to be replaced. Assuming only one word per blank.		
list_of_words = sample.split()
blank = []
number_of_blanks = 0
index = 0

while index<len(list_of_words):
	if list_of_words[index] in ["___1___" ,"___2___","___3___","___4___"]:
		number_of_blanks = number_of_blanks + 1
		blank.append(list_of_words[index])
	index=index+1

#Eliminating repetitions from the vector and creating a new one without repetitions and ordered by the number in the blank (uniqueblankvector) 
def onlyoneblanks(blank):
  output = []
  for x in blank:
    if x not in output:
      output.append(x)
  return output

uniqueblankvector= sorted (onlyoneblanks(blank))
uniqueblanks = len(list(set(blank)))

#Replacing the words in the blanks for the answers. 
#As some words filled several blanks  we check where in the paragraph the blanks with the same word can be located to replace all of them simultaneously  
def word_in_pos(word,blank):
	for pos in blank:
		if pos in word:
			return pos
	return None

def play_game(sample,uniqueblankvector):
	replaced = []
	list_of_words = sample.split()
	i = 1
	k = 1
#defining number of attempts per word
	maximum_number_of_attempts = 5
	remaining_attempts = maximum_number_of_attempts
	while i <= uniqueblanks:
		for word in uniqueblankvector:
			remaining_attempts = maximum_number_of_attempts	
			k = k + 1		
			replacement = word_in_pos(word,list_of_words)
			if replacement != None:
#now the player will be prompted to play each word at a time
				user_input = raw_input ("Type in your fill-the-blank word" + replacement + " ")
				while user_input != sample_result[i-1]: 
					if k == maximum_number_of_attempts:
#when the player has used all the attemps he will get a Game Over message
						print
						print "Game Over. You exhausted your ", maximum_number_of_attempts,  " attempts"
						print "The solution for your choosen level_of_difficulty _was ", sample_result
						return "Choose a diffenrent difficulty level and Play Again"
					else:
						remaining_attempts = remaining_attempts -1
						print
						print "try again, you still have ", remaining_attempts, " attempts" 
						user_input = raw_input ("Type in your fill-in-the-blank word" + replacement + " ")
				print
				print "The word is correct"
				print
			sample = sample.replace(replacement,user_input)
			i=i+1
	return sample
print
print play_game(sample,uniqueblankvector)
print
print "Everything correct"
print
print "The right solution is ", sample_result, "as you have typed"













