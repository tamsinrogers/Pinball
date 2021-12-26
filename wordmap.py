#Tamsin Rogers
#November 6, 2019

def main():
	print("input words")
	words = ["this", "is", "the", "list", "of", "words", "for", "the", "dictionary"]
	mapping = {}
	
	for i in words:
		response = input(i)
		mapping[i] = response
	for key in mapping:
		print("key: ", key)
		print("response: ", mapping[key])
		
if __name__ == "__main__":
    main()