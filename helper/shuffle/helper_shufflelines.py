import codecs
import random

def shuffleParallelLines(og_file, mod_file):
    with codecs.open(og_file, 'r', 'utf-8') as f:
        ogdata = f.read()
        oglines = ogdata.split("\n")

    with codecs.open(mod_file, 'r', 'utf-8') as f2:
        moddata = f2.read()
        modlines = moddata.split("\n")

    zipped = list(zip(oglines, modlines))

    random.shuffle(zipped)

    ogs, mods = zip(*zipped)

    with codecs.open("shuffled." + og_file, 'w', 'utf-8') as output:
        for line in ogs:
            output.write(line)
            output.write("\n")
    with codecs.open("shuffled." + mod_file, 'w', 'utf-8') as output2:
        for line in mods:
            output2.write(line)
            output2.write("\n")

def redistributeData(og_tr, mod_tr, og_val, mod_val, og_t, mod_t):
    with codecs.open(og_tr, "r", "utf-8") as f:
        trData = f.read()
        trLines = trData.split("\n")

    with codecs.open(og_val, "r", "utf-8") as f1:
        valData = f1.read()
        valLines = valData.split("\n")

    with codecs.open(og_t, "r", "utf-8") as f2:
        tData = f2.read()
        tLines = tData.split("\n")

    with codecs.open(mod_tr, "r", "utf-8") as f3:
        modTrData = f3.read()
        modTrLines = modTrData.split("\n")

    with codecs.open(mod_val, "r", "utf-8") as f4:
        modValData = f4.read()
        modValLines = modValData.split("\n")

    with codecs.open(mod_t, "r", "utf-8") as f5:
        modTData = f5.read()
        modTLines = modTData.split("\n")

    allOgLines = trLines + valLines + tLines
    allModLines = modTrLines + modValLines + modTLines

    with codecs.open("allLines.original.nltktok", "w", "utf-8") as oAll, \
        codecs.open("allLines.modern.nltktok", "w", "utf-8") as modAll:
        for line in allOgLines:
            oAll.write(line) 
            oAll.write("\n")
        for line_ in allModLines:
            modAll.write(line_)
            modAll.write("\n")
            
    zipped = list(zip(allOgLines, allModLines))

    random.shuffle(zipped)

    ogShuffled, modShuffled = zip(*zipped)

    print("boolean printline")
    print(ogShuffled[:100] == modShuffled[:100])

    delim1 = int(len(ogShuffled)*.64)
    delim2 = int(len(ogShuffled)*.80)

    with codecs.open("redistributed.train.original.nltktok", 'w', 'utf-8') as oTr, \
        codecs.open("redistributed.valid.original.nltktok", 'w', 'utf-8') as oVal, \
        codecs.open("redistributed.test.original.nltktok", "w", "utf-8") as oTest:
        for line in ogShuffled[:delim1]:
            oTr.write(line)
            oTr.write("\n")
        for line in ogShuffled[delim1:delim2]:
            oVal.write(line)
            oVal.write("\n")
        for line in ogShuffled[delim2:]:
            oTest.write(line)
            oTest.write("\n")

    with codecs.open("redistributed.train.modern.nltktok", 'w', 'utf-8') as mTr, \
        codecs.open("redistributed.valid.modern.nltktok",  'w', 'utf-8') as mVal, \
        codecs.open("redistributed.test.modern.nltktok", "w", "utf-8") as mTest:
        for line in modShuffled[:delim1]:
            mTr.write(line)
            mTr.write("\n")
        for line in modShuffled[delim1:delim2]:
            mVal.write(line)
            mVal.write("\n")
        for line in modShuffled[delim2:]:
            mTest.write(line)
            mTest.write("\n")

    print("second boolean printline")
    print(mTr == oTr)
    print(mVal == oVal)
    print(mTest == oTest)

if __name__ == '__main__':
    splits = ["train", "valid", "test"]
    for split in splits:
        shuffleParallelLines(split + ".original.nltktok", split + ".modern.nltktok")

    redistributeData("shuffled.train.original.nltktok", "shuffled.train.modern.nltktok", 
                        "shuffled.valid.original.nltktok", "shuffled.valid.modern.nltktok", 
                        "shuffled.test.original.nltktok", "shuffled.test.modern.nltktok")
