import re


class Data:

    def __init__(self, path):
        self.path = path

    # read txt
    def read_txt(self):
        with open(self.path,"r") as f:
            text = str(f.readlines())

        return text

    # modify text using regex expressions
    def re_mod(self, text):
        # specific
        text = re.sub(r"’","'",text)
        text = re.sub(r" t ","'t ",text)
        text = re.sub(r" s "," ",text)
        text = re.sub(r" n "," ",text)

        text = re.sub(r"won\'t", "will not", text)
        text = re.sub(r"can\'t", "can not", text)

        # general
        text = re.sub(r"n\'t", " not", text)
        text = re.sub(r"\'re", " are", text)
        text = re.sub(r"\'s", " is", text)
        text = re.sub(r"\'d", " would", text)
        text = re.sub(r"\'ll", " will", text)
        text = re.sub(r"\'t", " not", text)
        text = re.sub(r"\'ve", " have", text)
        text = re.sub(r"\'m", " am", text)

        text = re.findall(r"[a-zA-Z]+", text, re.M|re.I)

        return text


    def mod_txt(self):
        mod_txt = self.re_mod(self.read_txt())
        return mod_txt


# line = " Wasn t Trump s Donald Trump Sends Out Embarrassing New Year’s Eve Message it’s that’s you're"

# tex = re_mod(line)
# print(tex)