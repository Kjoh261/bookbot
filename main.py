import re
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path) #load file
    num_words = get_num_words(text) #count words
    letter_count = get_letter_count(text) 
    

    print(f"Begin report of{book_path}")
    print(f"{num_words} words found in the document")
    most_common_letter(letter_count) #print results
#################################  #load file #################################
def get_book_text(path): 
    with open(path) as f:
        return f.read()
    
################################# #count words #################################
def get_num_words(text): 
    words = text.split()
    return len(words)

################################# #count letters, returned dict #################################
def get_letter_count(text):
    letter_list = re.findall("[a-z]", text)
    letter_count = {}
    for llist in letter_list:
        if llist in letter_count:
            letter_count[llist] += 1
        else:
            letter_count[llist] = 1

    myKeys = list(letter_count.keys())
    myKeys.sort()
    sorted_dict = {i: letter_count[i] for i in myKeys}
    return sorted_dict
################################# #sort and print letter count, no return #################################
def most_common_letter(letter_dict):
    # takes a dict, sorts them in reverse order by value and then converts it into a list of tuples and then to a dict but ordered
    sorted_letter_count = dict(sorted(letter_dict.items(), key=lambda x:x[1], reverse=True))
    
    for k , v in sorted_letter_count.items(): # key value pair of a dict
        print(f"The {k} character was found {v} times")
    print(" - - End Report - - ")
    



main()