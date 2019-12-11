import re

rawfile = "shakespeare_nonparallels_sans_stagedirections.txt"
outfile = "shakespeare_nonparallels_dialog.nltktok"

def main():
    with open(rawfile, "r") as f:
        lines = f.read().splitlines()

    sentences = []
    for line in lines:
        sentences.extend(re.split('(?<=[!.?;:])', line))
   
    dialog = []

    with open(outfile, "w") as dialogfile:

        for sentence in sentences:
            sent = sentence.split(" ")
            if len(sent) > 0:
                if not sentence.isspace():
                    if sent[0].lower() != "act":
                        if sent[0].lower() != "scene":
                            if any(char.islower() for char in sentence): # check not all caps
                                dialogfile.write(sentence)
                                dialogfile.write("\n")
                
    print("printing sentences")
    print(dialog[:50])


if __name__ == "__main__":
    main()