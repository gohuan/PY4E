#6.5 Write code using find() and string slicing (see section 6.10) to 
#extract the number at the end of the line below. Convert the extracted 
#value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";

colon = text.find(":")
colon1 = text[colon+1:]
colon2 = float(colon1)
print(colon2)