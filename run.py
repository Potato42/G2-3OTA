import kacpaw

# construct a User object representing T#1B12P
tn1b12p = kacpaw.User.from_username("tn1b12p")

print(tn1b12p.name)

# this is the POTATO! program
potato_program = kacpaw.Program("5495235907551232")

print(potato_program.title, "at", potato_program.url)

# print out all the comments (please no encoding issues, please...)
for comment in potato_program.get_replies():
    print(comment.text_content)