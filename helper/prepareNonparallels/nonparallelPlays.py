def nonParallelCorpora():
	parallelCap = {
		"Antony and Cleopatra", 
		"As You Like It", 
		"Comedy of Errors", 
		#"Coriolanus", 
		"Hamlet", 
		#"Henry IV, Part I", 
		#"Henry IV, Part II", 
		"Henry V", 
		"Julius Caesar", 
		"King Lear",
		"Macbeth", 
		#"Measure for Measure", 
		"Merchant of Venice", 
		"Midsummer Night's Dream", 
		"Much Ado About Nothing", 
		"Othello", 
		#"Richard II", 
		"Richard III", 
		"Romeo and Juliet", 
		#"Sonnets", 
		"Taming of the Shrew", 
		"Tempest", 
		"Twelfth Night"
		#"Two Gentlement of Verona", 
		#"The Winter's Tale"
	}

	completeCap = {
		"All's Well That Ends Well",
		"As You Like It",
		"Comedy of Errors",
		"Love's Labour's Lost",
		"Measure for Measure",
		"Merchant of Venice",
		"Merry Wives of Windsor",
		"Midsummer Night's Dream",
		"Much Ado about Nothing",
		"Taming of the Shrew",
		"Tempest",
		"Twelfth Night",
		"Two Gentlemen of Verona",
		"Winter's Tale",
		"Henry IV, Part I",
		"Henry IV, Part II",
		"Henry V",
		"Henry VI, Part I",
		"Henry VI, Part II",
		"Henry VI, Part III",
		"Henry VIII",
		"King John",
		"Pericles",
		"Richard II",
		"Richard III",
		"Antony and Cleopatra",
		"Coriolanus",
		"Cymbeline",
		"Hamlet",
		"Julius Caesar",
		"King Lear",
		"Macbeth",
		"Othello",
		"Romeo and Juliet",
		"Timon of Athens",
		"Titus Andronicus",
		"Troilus and Cressida"
	}

	complete = set()
	for item in completeCap:
		complete.add(item.lower())

	parallel = set()
	for item in parallelCap:
		parallel.add(item.lower())

	print(len(parallel))
	print(len(complete))
	noParallel = complete - parallel
	print(len(noParallel))
	return noParallel

if __name__ == "__main__":
	nonparallel = nonParallelCorpora()
	with open("nonparallels.txt", "w") as f:
		for line in nonparallel:
			f.write(line + "\n")
	#print(nonparallel)
