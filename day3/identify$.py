#${identifier}
template=Template('That $noun looks ${noun}y')
string= template.safe_substitute(noun='fish')
print(string)