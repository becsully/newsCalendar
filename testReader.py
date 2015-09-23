__author__ = 'bsullivan'




def reader(txtfile):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday",
            "yesterday", "today", "tomorrow", "this week", "next week", "this month", "this weekend",
            "Jan.", "Feb.", "March", "April", "May", "June", "July", "Aug.", "Sept.", "Oct.", "Nov.", "Dec."]
    intensifiers = ["deadline", "by", "on", "expire", ]
    # negatives = past tense verbs
    with open(txtfile, "r") as story:
        for line in story:
            if line == "\n":
                pass
            else:
                if any(day in line for day in days):
                    print line

    #return a dictionary with the date, the thing that's happening on the date, the story URL, and a summary of some kind (Headline? lead graf?)


def test():
    print reader("story2.txt")



if __name__ == "__main__":
    test()