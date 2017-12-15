
import string

def caesar(plaintext,shift):

	alphabet=string.ascii_lowercase

	#Create our substitution dictionary
	dic={}
	for i in range(0,len(alphabet)):
		dic[alphabet[i]]=alphabet[(i+shift)%len(alphabet)]

	#Convert each letter of plaintext to the corrsponding
	#encrypted letter in our dictionary creating the cryptext
	ciphertext=""
	for l in plaintext.lower():
		if l in dic:
			l=dic[l]
		ciphertext+=l

	return ciphertext

frequency = {
	'a': 8.167,
	'b': 1.492,
	'c': 2.782,
	'd': 4.253,
	'e': 12.702,
	'f': 2.228,
	'g': 2.015,
	'h': 6.094,
	'i': 6.966,
	'j': 0.153,
	'k': 0.772,
	'l': 4.025,
	'm': 2.406,
	'n': 6.749,
	'o': 7.507,
	'p': 1.929,
	'q': 0.095,
	'r': 5.987,
	's': 6.327,
	't': 9.056,
	'u': 2.758,
	'v': 0.978,
	'w': 2.360,
	'x': 0.150,
	'y': 1.974,
	'z': 0.074,
}

results = { }

text = input()

for x in range(1, 26):
	error = 0
	cipherText = caesar(text, x)
	for y in string.ascii_lowercase:
		error += abs(100*(cipherText.count(y)/len(cipherText))-frequency[y])
		#print(abs(cipherText.count(y)/len(cipherText)-frequency[y]))
		#print(cipherText.count(y)/len(cipherText))
		#print(cipherText.count(y),len(cipherText))
	results[x] = error

print(caesar(text, min(results, key=results.get)))
print(min(results, key=results.get))
