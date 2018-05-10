#Palindromy!
 
###A Python Based Service for analysing palindromes in Strings

Given an input file containing text lines where some of them are JSON parsable strings containing a key named “key”.
Identify all the lines with a palindrome as the value of “key” and print out the count of matching lines.

#####Example

If the input below is analysed by this tool, it will yield 'racecar'
and the total number of palindromes will be one, in this case

`{"foo":"bar"}
{"key":"racecar"}
{"key":"not a palindrome","word":"sentence"}`


####Command Line Client

The commandline client can be run locally by calling 

``$ command_line_app.py $path_to_file_with_json``
where $path_to_file_with_json is the fully qualified path to the file
to be read and analysed

####Restful API

A REST service that exposes two endpoints that calls the component created above:

`GET:/palindromes`

Returns a list of all the values that are palindromes, one per line

`GET:/palindromes/count`

Returns the sum of the number of lines containing palindromes

###Observation

At the moment, the restful application works by just reading the
content from sample_data/jsons.jsons, this was done to keep it simple at a first
version, and allow the Rest API to be quickly exposed. 

The suggestion is to create new Endpoints ->

POST requests where it is possible to post a full body with tons of JSON object to be 
analysed

Perhaps:

`POST:/palindromes`



`POST:/palindromes/count`

