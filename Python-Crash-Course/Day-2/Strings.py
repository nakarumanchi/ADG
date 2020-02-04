text = "X-DSPAM-Confidence:    0.8475";
pos = text.find('0')
fl = float(text[pos:])
print(fl)
