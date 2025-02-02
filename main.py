def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        #print(word_count)
        char_count = count_chars(file_contents)
        #print(char_count)
        report = generate_report(count_chars(file_contents), file_contents)
        print(report)

def count_words(bookStr):
    book_list = bookStr.split()
    return len(book_list)

def count_chars(bookStr):
    char_dict = {}
    for i in bookStr:
        lower_str = i.lower()
        if lower_str in char_dict:
            char_dict[lower_str] += 1
        else:
            char_dict[lower_str] = 1
    return char_dict

def sort_by(dict):
    return dict['name']

def turn_into_sorted_list(normal_dict):
    cur_list = []
    for key, value in normal_dict.items():
        if(key.isalpha()):
            cur_list.append({'name': key, 'num': value})
    cur_list.sort(key=sort_by)
    return cur_list

def generate_report(normal_dict, file_contents):
    sorted_list = turn_into_sorted_list(normal_dict)
    word_count = count_words(file_contents)
    report_str = f"--- Begin report of books/frankenstein.txt ---\n{word_count} words found in the document\n"
    for elm in sorted_list:
        report_str = f"{report_str} \n The '{elm['name']}'  character was found {elm['num']} times"
    return f"{report_str}\n--- End report ---"

main()