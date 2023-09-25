### Matthew Virgin
### Dr. Sudarshan Chawathe
### COS 554
### 24 September 2023
### Homework 1

## input: myPogos(an array of ints), n (int)
## calls recursive function pogo() which destructively modifies an array
## to produce every combination of ints in myPogos which can add up to n as
## a list of lists (where each list contains ints)
def calcPogos(myPogos, n):
    tmp = []
    ans = []
    myPogos = list(set(myPogos))    # remove duplicates
    if 0 in myPogos:
        myPogos.remove(0)           # pogo that moves you nowhere is invalid
    if myPogos == []:
        return ans
    else:
        pogo(myPogos, tmp, n, ans)
        return ans

## input: myPogos(array of ints), n (int), tmp (array of ints), ans (nested arr)
## destructively modifies ans as described above
## no output
def pogo(myPogos, tmp, n, ans):
    if(n == 0):
        if tmp != []:
            ans.append(list(tmp))
        return
       
    ## Iterate over pogos
    for i in range(0, len(myPogos)):
        ## checking that n does not become negative
        if(n - myPogos[i]) >= 0:
            ## adding element which can contribute to n (the sum)
            tmp.append(myPogos[i])
            newSum = n-myPogos[i]
            pogo(myPogos, tmp, newSum, ans)

            ## backtracking needed because it restores tmp to what
            ## the iteration was called with, so that the next iteration
            ## after a recursive call finishes will have a proper tmp
            tmp.remove(myPogos[i])

def main():
    while True:
        try:
            line = input()
        except EOFError:
            break
        if not line:
            continue

        eles = line.split()
        n = int(eles[0])
        pogos = [int(x) for x in eles[1:]]

        b = calcPogos(pogos, n)

        b.sort()    # lexicographic order

        print(len(b))

        for i in range(len(b)):
            print(*b[i])
        print()

main()

