used ver 0 as the base model. 

Wanted to change the story like the human inputs first: failed: since RASA id designed to act upon first move from the user. So use UI or the channel to initiate the conversation so that bot responds to the user and user thinks he is greeted first.
Default_session_start option was not working in custom actions. Tried a lot of possibilities.

then the bot asks for satisfaction, if not satisfied, bot greets again, till the user is happy.

Add an out of scope intent too: done; requires a lot more training data to cover everything under the sun other than the weather.

Added Lookup tables as a separate file: city.yml. In such cases, -lookup: <entity_name> is not required in NLU.yml. the lookup table file needs to be in /data folder. Thats all.
Downloaded the entire city database from open weather in json format, used python script to extract city names and another python script to convert to yml file. 
when using lookup tables, use regexfeaturizer and DIET intent classifier(by parameter entity_recognition:false)

For an input"Give me the weather at tokyo", model is considering two entities values: 'Give' and "tokyo". Give is a city in denmark. How to overcome this issue?
Possible option is to instruct the model to consider only the 2nd entity value in this case. But how? But this problem was not there when using DIET classifier. It predicted entity value with city name with 0.999999 confidence value. 
This problem is observed with only the regex entity extractor with lookup tables

Or- since this is one off a case, remove 'give' from lookup tables, and write a separate code only for 'Give'

The same above problem with the word 'is'. What is the weather at tokyo, it is recognizing two entities: 'is' and 'tokyo'

The best solution for the above cases 'Give' and 'Is' would be to consider the second entity for the custom actions. But how to do it?
